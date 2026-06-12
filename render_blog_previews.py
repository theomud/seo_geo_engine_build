#!/usr/bin/env python3
"""Render the de-branded blog JSONs into standalone STYLED preview pages (not the production site).
Output -> dist/pawroute/preview/ (served by the running localhost:8000), using the engine theme."""
import json, glob, os, shutil, html as H
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "blogs-for-david"
OUT = ROOT / "dist/pawroute/preview"
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "images").mkdir(exist_ok=True)
for im in (SRC / "images").glob("*"):
    shutil.copy(im, OUT / "images" / im.name)

def e(x): return H.escape(str(x or ""))
def safe(x): return str(x or "")  # content already trusted (our own)

def head(title, desc):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{e(title)}</title><meta name="description" content="{e(desc)}">'
            f'<link rel="preconnect" href="https://fonts.googleapis.com">'
            f'<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap" rel="stylesheet">'
            f'<link rel="stylesheet" href="/assets/theme.css"></head>')

def header():
    return ('<body class="layout-article"><header class="site-header"><div class="container header-inner">'
            '<a class="brand" href="/preview/index.html"><span class="brand-mark">🐾</span>'
            '<span class="brand-name">Pet Relocation Guides</span></a>'
            '<nav class="primary-nav"><ul><li><a href="/preview/index.html">All guides</a></li></ul></nav>'
            '</div></header><main id="main">')

def render(d):
    s = d.get("seo", {}); h = d.get("hero", {})
    p = [head(s.get("title"), s.get("meta_description")), header()]
    # article header
    p.append('<header class="article-head"><div class="container container--article">')
    if h.get("eyebrow"): p.append(f'<a class="cat">{e(h["eyebrow"])}</a>')
    p.append(f'<h1>{e(h.get("h1"))}</h1>')
    if h.get("standfirst"): p.append(f'<p class="standfirst">{e(h["standfirst"])}</p>')
    if d.get("byline"): p.append(f'<div class="byline"><span class="by">{e(d["byline"])}</span></div>')
    p.append('</div>')
    img = (d.get("images") or [{}])[0].get("file") or h.get("image")
    if img: p.append(f'<div class="container container--article"><img class="article-hero" src="{e(img)}" alt="{e(h.get("image_alt"))}"></div>')
    p.append('</header>')
    # answer
    kf = d.get("key_facts", {})
    if kf.get("answer"):
        p.append(f'<section class="section"><div class="container container--article"><h2>The short answer</h2><div class="prose"><p>{safe(kf["answer"])}</p></div></div></section>')
    # takeaways
    if d.get("takeaways"):
        p.append('<section class="section--article"><div class="container container--article"><aside class="takeaways"><h2>Key takeaways</h2><ul>'
                 + "".join(f'<li>{safe(t)}</li>' for t in d["takeaways"]) + '</ul></aside></div></section>')
    # sections
    for sec in d.get("sections", []):
        t = sec.get("type")
        if t == "table":
            rows = "".join("<tr>" + "".join(f"<td>{e(c)}</td>" for c in r) + "</tr>" for r in sec.get("rows", []))
            thead = "<tr>" + "".join(f"<th>{e(c)}</th>" for c in sec.get("columns", [])) + "</tr>"
            p.append('<section class="section section--surface"><div class="container container--article">'
                     + (f'<h2>{e(sec.get("heading"))}</h2>' if sec.get("heading") else "")
                     + (f'<p>{safe(sec.get("body"))}</p>' if sec.get("body") else "")
                     + f'<table class="data">{thead}{rows}</table>'
                     + (f'<p class="tool-note">{safe(sec.get("note"))}</p>' if sec.get("note") else "")
                     + '</div></section>')
        elif t == "flow":
            steps = "".join(f'<span class="flow-step">{e(x)}</span>' + ("" if i == len(sec.get("steps", [])) - 1 else '<span class="flow-arrow">↓</span>') for i, x in enumerate(sec.get("steps", [])))
            p.append(f'<section class="section--article"><div class="container container--article"><h2>{e(sec.get("heading"))}</h2>'
                     + (f'<p>{safe(sec.get("body"))}</p>' if sec.get("body") else "") + f'<div class="flow">{steps}</div></div></section>')
        elif t == "compliance":
            facts = "".join(f'<li>{safe(f.get("text"))}{f" <span class=fa-src>— {e(f.get(chr(97)+chr(117)+chr(116)+chr(104)+chr(111)+chr(114)+chr(105)+chr(116)+chr(121)))}</span>" if f.get("authority") else ""}</li>' for f in sec.get("facts", []))
            adv = "".join(f'<li>{safe(a)}</li>' for a in sec.get("advice", []))
            p.append(f'<section class="section"><div class="container container--article"><h2>{e(sec.get("heading"))}</h2>'
                     f'<div class="fa-grid"><div class="fa-col fa-facts"><div class="fa-label">✅ What the rules require</div><ul>{facts}</ul></div>'
                     f'<div class="fa-col fa-advice"><div class="fa-label">💡 What we recommend</div><ul>{adv}</ul></div></div>'
                     + (f'<p class="fa-note">{safe(sec.get("note"))}</p>' if sec.get("note") else "") + '</div></section>')
        elif t == "case_study":
            rows = "".join(f'<tr><th>{e(r.get("label"))}</th><td>{e(r.get("value"))}</td></tr>' for r in sec.get("rows", []))
            p.append(f'<section class="section--article"><div class="container container--article"><div class="case"><div class="case-tag">Worked example</div>'
                     + (f'<h3>{e(sec.get("subheading") or sec.get("heading"))}</h3>' if (sec.get("subheading") or sec.get("heading")) else "")
                     + f'<table class="case-rows">{rows}</table>'
                     + (f'<div class="case-result">{e(sec.get("result"))}</div>' if sec.get("result") else "") + '</div></div></section>')
        else:  # prose
            body = ""
            if sec.get("paragraphs"): body += "".join(f"<p>{safe(x)}</p>" for x in sec["paragraphs"])
            if sec.get("bullets"): body += "<ul>" + "".join(f"<li>{safe(x)}</li>" for x in sec["bullets"]) + "</ul>"
            p.append('<section class="section"><div class="container container--article">'
                     + (f'<p class="eyebrow">{e(sec.get("eyebrow"))}</p>' if sec.get("eyebrow") else "")
                     + (f'<h2>{e(sec.get("heading"))}</h2>' if sec.get("heading") else "")
                     + f'<div class="prose">{body}</div></div></section>')
    # story
    st = d.get("story", {})
    if st:
        labels = [("Problem", "problem"), ("The mistake", "mistake"), ("What changed it", "discovery"), ("The result", "result"), ("The lesson", "lesson")]
        arc = "".join(f'<li><span class="arc-label">{lab}</span><span class="arc-text">{safe(st.get(k))}</span></li>' for lab, k in labels if st.get(k))
        p.append('<section class="section--article"><div class="container container--article"><h2>A real example</h2><div class="story">'
                 + (f'<p class="story-lead">{safe(st.get("lead"))}</p>' if st.get("lead") else "")
                 + f'<ol class="story-arc">{arc}</ol></div></div></section>')
    # faq
    if d.get("faqs"):
        items = "".join(f'<details><summary>{e(f["q"])}</summary><div class="prose"><p>{safe(f["a"])}</p></div></details>' for f in d["faqs"])
        p.append(f'<section class="section section--surface"><div class="container container--article"><h2>Frequently asked questions</h2>{items}</div></section>')
    # sources
    if d.get("sources"):
        src = "".join(f'<li><strong>{e(x.get("authority"))}</strong> — <a href="{e(x.get("url"))}">{e(x.get("title"))}</a>{f" · {e(x.get(chr(110)+chr(111)+chr(116)+chr(101)))}" if x.get("note") else ""}</li>' for x in d["sources"])
        p.append(f'<section class="section"><div class="container container--article"><h2>Official sources</h2><ul class="prose">{src}</ul></div></section>')
    # cta
    c = d.get("cta", {})
    if c:
        p.append('<section class="section section--primary"><div class="container container--article" style="text-align:center">'
                 + f'<h2>{e(c.get("heading"))}</h2><p>{safe(c.get("body"))}</p>'
                 + (f'<p class="help-cta">{safe(c.get("help_cta"))}</p>' if c.get("help_cta") else "")
                 + '<a class="btn btn-gold" href="#">Get a quote</a></div></section>')
    p.append('</main></body></html>')
    return "".join(p)

cards = []
for f in sorted(glob.glob(str(SRC / "*.json"))):
    if os.path.basename(f) == "uae-import-reference.json": continue
    d = json.loads(Path(f).read_text(encoding="utf-8"))
    slug = os.path.basename(f)[:-5]
    (OUT / (slug + ".html")).write_text(render(d), encoding="utf-8")
    img = (d.get("images") or [{}])[0].get("file", "")
    cards.append((d.get("hero", {}).get("h1", slug), d.get("seo", {}).get("meta_description", ""), slug + ".html", img))

# index
idx = [head("Pet Relocation Guides — preview", "All 16 blog previews"), header(),
       '<header class="article-head"><div class="container"><h1>Pet relocation guides — preview</h1>'
       '<p class="standfirst">All 16 blogs, rendered. Click any to view.</p></div></header>'
       '<section class="section"><div class="container"><div class="card-grid">']
for title, desc, href, img in sorted(cards):
    idx.append(f'<a class="card" href="{e(href)}">' + (f'<img src="{e(img)}" style="width:100%;border-radius:10px;margin-bottom:.6rem">' if img else "")
               + f'<h3>{e(title)}</h3><div class="card-meta">{e(desc[:110])}…</div><div class="card-arrow">Read →</div></a>')
idx.append('</div></div></section></main></body></html>')
(OUT / "index.html").write_text("".join(idx), encoding="utf-8")
print(f"rendered {len(cards)} blog previews + index -> dist/pawroute/preview/")
print("open: http://localhost:8000/preview/index.html")
