"""Self-contained HTML report for the gold-standard auditor."""
import html as _h

LENS_META = {"website":("🌐","Website","#2563c4"),"seo":("🔍","SEO","#2e8b57"),
             "geo":("🤖","GEO","#7b1fa2"),"trust":("💛","Lead-gen / Trust","#c08f33"),
             "quality":("✨","Quality","#c0392b")}
GRADE_COLOR = {"A":"#2e8b57","B":"#5b9c3f","C":"#c08f33","D":"#d9822b","E":"#c0392b","F":"#a01b0b"}

def _bar(label, score, color, sub=""):
    if score is None:
        return f'<div class="row"><span class="lbl">{_h.escape(label)}</span><span class="na">not measurable</span></div>'
    return (f'<div class="row"><span class="lbl">{_h.escape(label)}</span>'
            f'<span class="track"><i style="width:{score}%;background:{color}"></i></span>'
            f'<span class="val">{score}</span></div>{f"<div class=sub>{_h.escape(sub)}</div>" if sub else ""}')

def _page_block(r):
    g = r["grade"]; gc = GRADE_COLOR.get(g,"#888")
    lenses = "".join(_bar(f"{LENS_META[l][0]} {LENS_META[l][1]}", v["score"], LENS_META[l][2],
                          f"coverage {v['coverage']}% · {v['measured']}/{v['total']} checks")
                     for l,v in r["lenses"].items())
    caps = ("".join(f'<li><b>{_h.escape(c["title"])}</b> → score capped at {c["cap"]}. {_h.escape(c["fix"])}</li>'
                    for c in r["caps"])) or "<li>None — no penalty caps triggered.</li>"
    # per-check detail grouped by lens
    detail = ""
    for l,(ic,name,col) in LENS_META.items():
        items = [c for c in r["checks"] if c["lens"]==l]
        rows = ""
        for c in items:
            sc = "—" if c["score"] is None else f"{int(c['score']*100)}"
            badge = "✓verified" if c["kind"]=="verified" else "~heuristic"
            ok = "ok" if (c["score"] or 0)>=0.7 else ("warn" if (c["score"] or 0)>=0.4 else "bad") if c["score"] is not None else "na"
            rows += (f'<tr class="{ok}"><td>{_h.escape(c["title"])}</td><td class="c">{sc}</td>'
                     f'<td class="c"><span class="tier">{c["tier"]}</span></td><td class="c">{badge}</td>'
                     f'<td>{_h.escape(c["detail"])}</td></tr>')
        detail += (f'<h4>{ic} {name}</h4><table class="chk"><thead><tr><th>Check</th><th>%</th>'
                   f'<th>Tier</th><th>Type</th><th>Detail</th></tr></thead><tbody>{rows}</tbody></table>')
    fixes = "".join(f'<li>{"<span class=crit>CRITICAL</span> " if f.get("critical") else ""}'
                    f'<span class="fl" style="background:{LENS_META[f["lens"]][2]}">{LENS_META[f["lens"]][1]}</span> '
                    f'<b>{_h.escape(f["fix"])}</b> <span class="muted">— {_h.escape(f["detail"])}</span></li>'
                    for f in r["top_fixes"])
    ba = r.get("brief_alignment")
    ba_html = ""
    if ba:
        rows = "".join(f'<tr><td>{_h.escape(k.replace("_"," "))}</td><td class="c">{"—" if v is None else int(v*100)}</td></tr>'
                       for k,v in ba["checks"].items())
        cls = "onstrat" if ba["on_strategy"] else "offstrat"
        ba_html = (f'<div class="ba {cls}"><b>Brief alignment: {ba["alignment"]}/100 '
                   f'{"✓ ON-STRATEGY" if ba["on_strategy"] else "✗ OFF-STRATEGY"}</b>'
                   f'<div class="muted">brief: “{_h.escape(ba["keyword"] or "")}” · intended <b>{ba["want_type"]}</b>, '
                   f'detected <b>{ba["got_type"]}</b> · fear: {_h.escape((ba["customer_fear"] or "")[:80])}</div>'
                   f'<table class="chk"><tbody>{rows}</tbody></table></div>')
    pl = _h.escape(r.get("profile_label","")); cf = r.get("critical_fails",[])
    cf_html = (f'<div class="cfbar">⚠ Critical for a <b>{pl}</b> page, currently weak: '
               + ", ".join(_h.escape(x) for x in cf) + '</div>') if cf else ""
    return f"""
    <div class="card">
      <div class="hdr">
        <div class="grade" style="background:{gc}">{g}</div>
        <div><div class="score">{r['score']}<span>/100</span></div>
        <div class="muted"><span class="ptype">{pl}</span> · raw {r['raw']} · {r['confidence']} confidence · coverage {r['coverage']}% (verified {r['verified_coverage']}%)</div>
        <div class="url">{_h.escape(r['url'])}</div></div>
      </div>
      {ba_html}
      {cf_html}
      <div class="lenses">{lenses}</div>
      <h3>⚑ Risk caps</h3><ul class="caps">{caps}</ul>
      <h3>🎯 Top fixes (highest leverage)</h3><ol class="fixes">{fixes}</ol>
      <h3>All checks</h3>{detail}
    </div>"""

def render_report(data, site=False):
    if site:
        body = (f'<h1>Site audit — {_h.escape(data["site"])}</h1>'
                f'<p class="lead">Average score <b>{data["score"]}/100</b> across {data["count"]} pages.</p>')
        for r in sorted(data["pages"], key=lambda x:x["score"]):
            body += _page_block(r)
    else:
        body = f'<h1>Page audit</h1>' + _page_block(data)
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Gold-standard audit</title><style>
:root{{--ink:#1f2733;--muted:#5d6a78;--line:#e7ddcb;--bg:#f6f8fb}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 'Inter',system-ui,Segoe UI,sans-serif;padding:24px}}
h1{{font-family:'Plus Jakarta Sans',sans-serif;margin:.2rem 0}}.lead{{color:var(--muted)}}
.card{{background:#fff;border:1px solid var(--line);border-radius:16px;padding:22px;margin:18px 0;box-shadow:0 14px 32px -22px rgba(16,33,60,.3);max-width:920px}}
.hdr{{display:flex;gap:16px;align-items:center;border-bottom:1px solid var(--line);padding-bottom:14px;margin-bottom:14px}}
.grade{{width:64px;height:64px;border-radius:14px;color:#fff;display:grid;place-items:center;font:800 2rem 'Plus Jakarta Sans',sans-serif}}
.score{{font:800 2rem 'Plus Jakarta Sans',sans-serif}}.score span{{font-size:1rem;color:var(--muted)}}
.url{{font-size:.8rem;color:var(--muted);word-break:break-all}}.muted{{color:var(--muted);font-size:.85rem}}
.row{{display:flex;align-items:center;gap:10px;margin:7px 0}}.lbl{{width:190px;font-weight:600}}
.track{{flex:1;height:10px;background:#eef1f4;border-radius:6px;overflow:hidden}}.track i{{display:block;height:100%}}
.val{{width:38px;text-align:right;font-weight:700}}.na{{color:var(--muted);font-style:italic}}
.sub{{margin:-2px 0 6px 200px;font-size:.78rem;color:var(--muted)}}
h3{{font-family:'Plus Jakarta Sans',sans-serif;margin:18px 0 6px;font-size:1.05rem}}
h4{{margin:14px 0 4px;font-size:.95rem}}
.caps li{{margin:3px 0}}.fixes li{{margin:6px 0}}.fl{{color:#fff;font-size:.7rem;padding:2px 7px;border-radius:6px;margin-right:6px}}
.ptype{{background:#1a365d;color:#fff;border-radius:5px;padding:1px 8px;font-weight:600}}
.crit{{background:#c0392b;color:#fff;font-size:.66rem;font-weight:700;padding:1px 6px;border-radius:5px;margin-right:4px}}
.cfbar{{background:#fdf0ee;border:1px solid #f3c9c0;color:#7a2820;border-radius:10px;padding:8px 12px;margin:0 0 12px;font-size:.86rem}}
.ba{{border-radius:10px;padding:10px 14px;margin:0 0 12px}}
.ba.onstrat{{background:#eef6f0;border:1px solid #cfe6d8}}.ba.offstrat{{background:#fff6e8;border:1px solid #f3d9ad}}
.ba table{{max-width:360px}}
table.chk{{width:100%;border-collapse:collapse;font-size:.85rem;margin:4px 0}}
.chk th{{text-align:left;color:var(--muted);font-weight:600;border-bottom:1px solid var(--line);padding:4px 6px}}
.chk td{{padding:4px 6px;border-bottom:1px solid #f1f3f6;vertical-align:top}}.chk td.c{{text-align:center;white-space:nowrap}}
.tier{{background:#eef1f4;border-radius:4px;padding:1px 5px;font-size:.72rem}}
tr.ok td:nth-child(2){{color:#2e8b57;font-weight:700}}tr.warn td:nth-child(2){{color:#d9822b;font-weight:700}}
tr.bad td:nth-child(2){{color:#c0392b;font-weight:700}}tr.na td{{opacity:.55}}
</style></head><body>{body}
<p class="muted" style="max-width:920px">Scores are structured judgments from on-page signals (evidence-tiered, verified-vs-heuristic). Not-measurable checks are excluded, never zeroed. Coverage shows how much of the rubric was measurable. See audit/README.md for methodology.</p>
</body></html>"""
