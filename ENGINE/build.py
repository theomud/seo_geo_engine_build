#!/usr/bin/env python3
"""
SEO + GEO Content Engine — static site generator.

Business-agnostic. Point it at a site folder and it renders a complete
static website from a single brand config (site.yml) plus block-composed
page files (pages/*.yml). Pages are ordered lists of typed "blocks"
(hero, pricing_tiers, checklist, steps, faq, cta, ...) which the engine
renders via Jinja partials in engine/templates/blocks/.

Usage:
    py engine/build.py sites/pawroute
    py engine/build.py sites/pawroute --out dist
    py engine/build.py sites/pawroute --serve   # build + local preview server

Swap the site folder to generate a site for any business. Nothing in the
engine knows about pets, routes, or UAE — that all lives in the site data.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import html
import json
import re
import shutil
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required:  py -m pip install pyyaml")

try:
    from jinja2 import Environment, FileSystemLoader, select_autoescape
except ImportError:  # pragma: no cover
    sys.exit("Jinja2 is required:  py -m pip install jinja2")


ENGINE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = ENGINE_DIR / "templates"


# --------------------------------------------------------------------------- #
# Data loading
# --------------------------------------------------------------------------- #
def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or {}
    if not isinstance(data, dict):
        raise ValueError(f"{path} must be a mapping, got {type(data).__name__}")
    return data


def load_pages(site_dir: Path) -> list[dict]:
    """Load every pages/**/*.yml file into a list of page dicts."""
    pages_dir = site_dir / "pages"
    if not pages_dir.is_dir():
        raise SystemExit(f"No pages/ folder in {site_dir}")
    pages = []
    for path in sorted(pages_dir.rglob("*.yml")):
        page = load_yaml(path)
        page.setdefault("blocks", [])
        if "url" not in page:
            # Derive a clean URL from the file path relative to pages/
            rel = path.relative_to(pages_dir).with_suffix("")
            slug = "" if rel.name == "home" else str(rel).replace("\\", "/")
            page["url"] = "/" if slug == "" else f"/{slug}/"
        page["_src"] = str(path)
        pages.append(page)
    return pages


# --------------------------------------------------------------------------- #
# URL / output helpers
# --------------------------------------------------------------------------- #
def clean_dir(out_dir: Path) -> None:
    """Empty out_dir without removing the root (OneDrive/Windows can lock the
    folder handle, which makes rmtree of the root fail). Clears contents,
    retrying past read-only flags."""
    import os
    import stat

    def _onerror(func, path, _exc):
        try:
            os.chmod(path, stat.S_IWRITE)
            func(path)
        except OSError:
            pass

    out_dir.mkdir(parents=True, exist_ok=True)
    for child in out_dir.iterdir():
        if child.is_dir():
            shutil.rmtree(child, onexc=_onerror)
        else:
            try:
                child.unlink()
            except OSError:
                _onerror(os.unlink, child, None)


def url_to_output(url: str) -> Path:
    """'/' -> index.html ; '/services/uae-to-uk/' -> services/uae-to-uk/index.html"""
    clean = url.strip("/")
    if clean == "":
        return Path("index.html")
    return Path(clean) / "index.html"


# --------------------------------------------------------------------------- #
# Structured data (GEO / SEO) — JSON-LD
# --------------------------------------------------------------------------- #
def build_jsonld(page: dict, site: dict) -> list[dict]:
    """Assemble JSON-LD graph: Organization + WebPage + any FAQ blocks + Service."""
    biz = site.get("business", {})
    org_id = site.get("url", "") + "#org"
    blocks: list[dict] = []

    org = {
        "@type": biz.get("schema_type", "Organization"),
        "@id": org_id,
        "name": biz.get("name"),
        "url": site.get("url"),
    }
    if biz.get("description"):
        org["description"] = biz["description"]
    if biz.get("logo"):
        org["logo"] = biz["logo"]
    contact = site.get("contact", {})
    if contact.get("phone"):
        org["telephone"] = contact["phone"]
    if contact.get("email"):
        org["email"] = contact["email"]
    if biz.get("address"):
        org["address"] = {"@type": "PostalAddress", **biz["address"]}
    if biz.get("area_served"):
        org["areaServed"] = biz["area_served"]
    if biz.get("price_range"):
        org["priceRange"] = biz["price_range"]
    if biz.get("knows_about"):
        org["knowsAbout"] = biz["knows_about"]
    if biz.get("same_as"):
        org["sameAs"] = biz["same_as"]
    # Only emit aggregateRating / reviews when REAL ones exist (never fabricate — truth policy)
    rev = biz.get("reviews", {})
    if rev.get("aggregate_rating"):
        ar = rev["aggregate_rating"]
        org["aggregateRating"] = {"@type": "AggregateRating",
                                  "ratingValue": ar.get("rating"), "reviewCount": ar.get("count")}
    blocks.append(org)

    # Author / E-E-A-T — a named Person if site.author.person is filled, else the team (Organization)
    author = site.get("author", {})
    person = author.get("person") or {}
    if person.get("name"):
        author_node = {"@type": "Person", "@id": site.get("url", "") + "#author",
                       "name": person["name"], "worksFor": {"@id": org_id}}
        if person.get("job_title"): author_node["jobTitle"] = person["job_title"]
        if person.get("credentials"): author_node["description"] = person["credentials"]
        if person.get("same_as"): author_node["sameAs"] = person["same_as"]
        blocks.append(author_node)
        author_ref = {"@id": site.get("url", "") + "#author"}
    else:
        author_ref = {"@id": org_id}   # honest default: authored/reviewed by the team

    # Service schema for service-type pages
    if page.get("schema") == "service" and page.get("service"):
        svc = {
            "@type": "Service",
            "name": page["service"].get("name", page.get("title")),
            "provider": {"@id": org_id},
        }
        if page["service"].get("area_served"):
            svc["areaServed"] = page["service"]["area_served"]
        if page.get("meta_description"):
            svc["description"] = page["meta_description"]
        blocks.append(svc)

    # FAQPage schema from any faq block on the page
    faqs = []
    for block in page.get("blocks", []):
        if block.get("type") == "faq":
            for item in block.get("items", []):
                faqs.append(
                    {
                        "@type": "Question",
                        "name": item.get("q", ""),
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": item.get("a", ""),
                        },
                    }
                )
    if faqs:
        blocks.append({"@type": "FAQPage", "mainEntity": faqs})

    # WebPage node with freshness dates (datePublished/dateModified) — SEO + GEO freshness signal
    base = site.get("url", "").rstrip("/")
    page_url = base + page.get("url", "/")
    today = _dt.date.today().isoformat()
    webpage = {
        "@type": "WebPage",
        "@id": page_url + "#webpage",
        "url": page_url,
        "name": page.get("title"),
        "isPartOf": {"@id": org_id},
        "datePublished": page.get("published", today),
        "dateModified": page.get("updated", today),
    }
    if page.get("meta_description"):
        webpage["description"] = page["meta_description"]
    webpage["author"] = author_ref
    webpage["publisher"] = {"@id": org_id}
    blocks.append(webpage)

    # BreadcrumbList (SEO navigation signal)
    crumbs = build_breadcrumbs(page, site)
    if len(crumbs) > 1:
        blocks.append({
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": c["label"],
                 "item": base + c["url"]}
                for i, c in enumerate(crumbs)
            ],
        })

    return [{"@context": "https://schema.org", "@graph": blocks}]


# --------------------------------------------------------------------------- #
# Jinja environment
# --------------------------------------------------------------------------- #
_SLUG_RE = re.compile(r"[^a-z0-9]+")


def slugify(value: str) -> str:
    return _SLUG_RE.sub("-", str(value).lower()).strip("-")


_ACRONYMS = {"uae", "uk", "usa", "eu", "faq", "noc", "cdc", "iata", "apha", "moccae",
             "aqcs", "daff", "cfia", "dalrrd", "avs", "geo", "seo"}

def _crumb_label(seg: str) -> str:
    words = []
    for w in seg.replace("-", " ").split():
        if w.lower() in _ACRONYMS:
            words.append(w.upper())
        elif w.lower() == "to":
            words.append("to")
        else:
            words.append(w.capitalize())
    return " ".join(words)

def build_breadcrumbs(page: dict, site: dict) -> list[dict]:
    """Home → … → current, from the page URL. Empty for the homepage."""
    url = page.get("url", "/")
    if url == "/":
        return []
    segs = [s for s in url.strip("/").split("/") if s]
    crumbs = [{"label": "Home", "url": "/"}]
    path = ""
    for i, s in enumerate(segs):
        path += "/" + s
        last = i == len(segs) - 1
        label = page.get("breadcrumb") if (last and page.get("breadcrumb")) else _crumb_label(s)
        crumbs.append({"label": label, "url": path + "/"})
    return crumbs


def make_env() -> Environment:
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html", "xml", "j2"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    from markupsafe import Markup

    def tojson_ld(value):
        # Safe to emit raw inside <script type="application/ld+json">.
        # Guard against premature </script> termination.
        text = json.dumps(value, ensure_ascii=False, indent=2).replace("</", "<\\/")
        return Markup(text)

    env.filters["slugify"] = slugify
    env.filters["tojson_ld"] = tojson_ld
    return env


# --------------------------------------------------------------------------- #
# Build
# --------------------------------------------------------------------------- #
def build(site_dir: Path, out_root: Path) -> Path:
    site = load_yaml(site_dir / "site.yml")
    pages = load_pages(site_dir)

    site_name = site.get("name") or site_dir.name
    out_dir = out_root / slugify(site_name)
    clean_dir(out_dir)

    env = make_env()
    base_tpl = env.get_template("base.html.j2")

    # Navigation: explicit nav in site.yml, else derive from pages with nav_order
    nav = site.get("nav")
    if not nav:
        nav = [
            {"label": p.get("nav_label", p.get("title")), "url": p["url"], "order": p.get("nav_order", 999)}
            for p in pages
            if p.get("in_nav")
        ]
        nav.sort(key=lambda n: n.get("order", 999))

    year = _dt.date.today().year

    rendered_urls = []
    for page in pages:
        ctx = {
            "site": site,
            "page": page,
            "nav": nav,
            "year": year,
            "jsonld": build_jsonld(page, site),
            "current_url": page["url"],
            "breadcrumbs": build_breadcrumbs(page, site),
        }
        html_out = base_tpl.render(**ctx)
        target = out_dir / url_to_output(page["url"])
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html_out, encoding="utf-8")
        rendered_urls.append((page["url"], page.get("updated") or _dt.date.today().isoformat(), page))

    # Generated theme CSS from design tokens
    theme_tpl = env.get_template("theme.css.j2")
    css = theme_tpl.render(site=site, theme=site.get("theme", {}))
    assets_dir = out_dir / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)
    (assets_dir / "theme.css").write_text(css, encoding="utf-8")

    # Copy any static assets shipped with the site (images, favicons, etc.)
    site_assets = site_dir / "assets"
    if site_assets.is_dir():
        shutil.copytree(site_assets, assets_dir, dirs_exist_ok=True)

    # Optional site-wide JS
    js_tpl_path = TEMPLATES_DIR / "main.js"
    if js_tpl_path.exists():
        shutil.copy(js_tpl_path, assets_dir / "main.js")

    # sitemap.xml + robots.txt + llms.txt
    base_url = site.get("url", "").rstrip("/")
    write_sitemap(out_dir, base_url, rendered_urls)
    (out_dir / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {base_url}/sitemap.xml\n", encoding="utf-8"
    )
    write_llmstxt(out_dir, base_url, site, rendered_urls)

    return out_dir


def write_llmstxt(out_dir: Path, base_url: str, site: dict, entries) -> None:
    """llms.txt — a curated map of the site for AI crawlers (the GEO equivalent of robots/sitemap)."""
    biz = site.get("business", {})
    groups = {"Guides": [], "Destinations": [], "Tools": [], "Key pages": []}
    for entry in entries:
        url = entry[0] if isinstance(entry, (list, tuple)) else entry
        page = entry[2] if isinstance(entry, (list, tuple)) and len(entry) > 2 else {}
        title = page.get("title", url).split(" | ")[0].split(" — ")[0].strip()
        desc = page.get("meta_description", "")
        line = f"- [{title}]({base_url}{url})" + (f": {desc}" if desc else "")
        if url == "/":
            continue
        if "/blog" in url:
            groups["Guides"].append(line)
        elif "/destinations" in url:
            groups["Destinations"].append(line)
        elif "/tools" in url:
            groups["Tools"].append(line)
        else:
            groups["Key pages"].append(line)
    out = [f"# {biz.get('name', site.get('name', ''))}"]
    if biz.get("tagline"):
        out.append(f"> {biz['tagline']}")
    if biz.get("description"):
        out.append("\n" + " ".join(biz["description"].split()))
    for section, lines in groups.items():
        if lines:
            out.append(f"\n## {section}")
            out.extend(sorted(lines))
    (out_dir / "llms.txt").write_text("\n".join(out) + "\n", encoding="utf-8")


def _sitemap_priority(url: str) -> str:
    """Light priority hint by page role (Google mostly ignores it, but it's harmless + honest)."""
    if url == "/":
        return "1.0"
    if re.search(r"/destinations/[a-z]+-to-[a-z]|/pricing/?$", url):
        return "0.9"   # money pages
    if re.search(r"/destinations/?$|/tools/?$|/blog/?$|/destinations/[a-z-]+/?$", url):
        return "0.8"   # hubs / tools
    return "0.6"

def write_sitemap(out_dir: Path, base_url: str, entries) -> None:
    """entries: list of (url, lastmod, page) tuples (page optional/ignored)."""
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    today = _dt.date.today().isoformat()
    for entry in entries:
        url = entry[0] if isinstance(entry, (list, tuple)) else entry
        lastmod = entry[1] if isinstance(entry, (list, tuple)) and len(entry) > 1 else today
        loc = html.escape(f"{base_url}{url}")
        lines.append(f"  <url><loc>{loc}</loc><lastmod>{html.escape(str(lastmod))}</lastmod>"
                     f"<priority>{_sitemap_priority(url)}</priority></url>")
    lines.append("</urlset>")
    (out_dir / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="SEO+GEO static site engine")
    parser.add_argument("site", help="Path to a site folder (containing site.yml)")
    parser.add_argument("--out", default="dist", help="Output root (default: dist)")
    parser.add_argument("--serve", action="store_true", help="Serve the result after building")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args(argv)

    site_dir = Path(args.site).resolve()
    if not (site_dir / "site.yml").exists():
        return _fail(f"No site.yml found in {site_dir}")

    out_root = Path(args.out).resolve()
    out_dir = build(site_dir, out_root)

    pages = list(out_dir.rglob("index.html"))
    print(f"OK  built {len(pages)} pages -> {out_dir}")
    for p in sorted(pages):
        print(f"    /{p.parent.relative_to(out_dir).as_posix()}".rstrip("/") or "    /")

    if args.serve:
        serve(out_dir, args.port)
    return 0


def serve(out_dir: Path, port: int) -> None:
    import functools
    import http.server
    import socketserver

    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(out_dir))
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Serving {out_dir} at http://localhost:{port}  (Ctrl+C to stop)")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nstopped")


def _fail(msg: str) -> int:
    print(f"ERROR: {msg}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
