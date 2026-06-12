#!/usr/bin/env python3
"""
Render pictures with BFL / FLUX.

Part of the engine's image output. Reads BFL_API_KEY from .env, submits a
prompt to the BFL API, polls for the result, and downloads the PNG.

Usage:
    py engine/render_images.py "a warm photo of ..." --out assets/hero.png
    py engine/render_images.py "..." --out x.png --model flux-2-pro --width 1440 --height 960
    py engine/render_images.py --batch jobs.json      # [{prompt,out,width,height}, ...]

No third-party deps — uses urllib from the stdlib.
"""
from __future__ import annotations
import argparse, json, sys, time, urllib.request, urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://api.bfl.ai/v1"
DEFAULT_MODEL = "flux-2-pro"   # FLUX.2 pro; override with --model if the account uses another

def load_key() -> str:
    env = ROOT / ".env"
    if env.exists():
        for line in env.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("BFL_API_KEY=") and not line.startswith("#"):
                v = line.split("=", 1)[1].strip()
                if v:
                    return v
    import os
    if os.environ.get("BFL_API_KEY"):
        return os.environ["BFL_API_KEY"]
    sys.exit("No BFL_API_KEY found in .env or environment.")

def _req(url, method="GET", headers=None, body=None, timeout=60):
    data = json.dumps(body).encode() if body is not None else None
    r = urllib.request.Request(url, data=data, method=method, headers=headers or {})
    try:
        with urllib.request.urlopen(r, timeout=timeout) as resp:
            return resp.status, json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")
        return e.code, {"_error": detail}

def render(prompt, out, key, model=DEFAULT_MODEL, width=1440, height=960, max_wait=120):
    headers = {"x-key": key, "Content-Type": "application/json", "accept": "application/json"}
    status, data = _req(f"{BASE}/{model}", "POST", headers,
                         {"prompt": prompt, "width": width, "height": height})
    if status not in (200, 201) or "_error" in data:
        return False, f"submit HTTP {status}: {data.get('_error', data)}"
    polling_url = data.get("polling_url") or data.get("pollingUrl")
    if not polling_url:
        return False, f"no polling_url in response: {data}"

    waited = 0
    while waited < max_wait:
        time.sleep(2); waited += 2
        s, pd = _req(polling_url, "GET", headers)
        st = (pd.get("status") or "").lower()
        if st == "ready":
            sample = (pd.get("result") or {}).get("sample")
            if not sample:
                return False, f"ready but no sample: {pd}"
            outp = Path(out)
            if not outp.is_absolute():
                outp = ROOT / outp
            outp.parent.mkdir(parents=True, exist_ok=True)
            urllib.request.urlretrieve(sample, outp)
            return True, str(outp)
        if st in ("error", "failed", "content moderated", "request moderated"):
            return False, f"generation {st}: {pd}"
    return False, f"timed out after {max_wait}s"

def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("prompt", nargs="?", help="image prompt")
    ap.add_argument("--out", default="images/render.png")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--width", type=int, default=1440)
    ap.add_argument("--height", type=int, default=960)
    ap.add_argument("--batch", help="JSON file: [{prompt,out,width,height}]")
    a = ap.parse_args(argv)
    key = load_key()

    jobs = []
    if a.batch:
        jobs = json.loads(Path(a.batch).read_text(encoding="utf-8"))
    elif a.prompt:
        jobs = [{"prompt": a.prompt, "out": a.out, "width": a.width, "height": a.height}]
    else:
        sys.exit("give a prompt or --batch file")

    rc = 0
    for j in jobs:
        ok, msg = render(j["prompt"], j.get("out", "images/render.png"), key,
                         model=j.get("model", a.model),
                         width=j.get("width", a.width), height=j.get("height", a.height))
        print(("OK  " if ok else "ERR ") + j.get("out", "") + "  " + (msg if not ok else "-> " + msg))
        if not ok: rc = 1
    return rc

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
