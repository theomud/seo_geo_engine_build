#!/usr/bin/env python3
"""
Export a built site as a PORTABLE copy that opens by double-clicking index.html
(no web server needed) and is safe to zip & send.

The normal build uses root-absolute URLs (/assets/..., /destinations/...), which
only resolve behind a server. This rewrites every root-relative href/src to a
path relative to each page's depth, and points directory links at index.html so
they work over file://.

Usage:
    py engine/export_portable.py dist/pawroute "C:/Users/Theo/Downloads/PawRoute-website"
"""
from __future__ import annotations
import re, shutil, sys, zipfile
from pathlib import Path

ATTR_RE = re.compile(r'(href|src)="(/[^"]*)"')

def rewrite(html: str, depth: int) -> str:
    prefix = "../" * depth
    def repl(m):
        attr, url = m.group(1), m.group(2)
        path = url.lstrip("/")
        # directory-style link (ends with / or has no file extension) -> index.html
        last = path.rsplit("/", 1)[-1]
        if path == "" or url.endswith("/"):
            path = (path + "index.html") if path else "index.html"
        elif "." not in last:
            path = path.rstrip("/") + "/index.html"
        return f'{attr}="{prefix}{path}"'
    return ATTR_RE.sub(repl, html)

def main(argv):
    if len(argv) < 2:
        sys.exit("usage: py engine/export_portable.py <built-site-dir> <out-dir>")
    src = Path(argv[0]).resolve()
    out = Path(argv[1]).resolve()
    if not (src / "index.html").exists():
        sys.exit(f"no index.html in {src} — run the build first")

    if out.exists():
        shutil.rmtree(out, ignore_errors=True)
    shutil.copytree(src, out)

    # drop server-only files
    for f in ("sitemap.xml", "robots.txt"):
        p = out / f
        if p.exists():
            p.unlink()

    count = 0
    for page in out.rglob("index.html"):
        depth = len(page.parent.relative_to(out).parts)  # 0 at root
        page.write_text(rewrite(page.read_text(encoding="utf-8"), depth), encoding="utf-8")
        count += 1

    # zip alongside the folder for easy sending
    zip_path = out.with_suffix(".zip")
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for f in out.rglob("*"):
            if f.is_file():
                z.write(f, f.relative_to(out.parent))

    print(f"OK  portable site -> {out}")
    print(f"    rewrote {count} pages for offline / file:// use")
    print(f"    zipped  -> {zip_path}")

if __name__ == "__main__":
    main(sys.argv[1:])
