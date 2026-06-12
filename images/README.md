# images/ — rendered pictures

All AI-rendered pictures live here, **separate** from content and any site
output. This is the picture half of the engine's job (the other half is the
writing).

## Structure

```
images/
├── _samples/        # test renders / experiments
├── pawroute/        # images for the PawRoute site (one subfolder per business)
│   └── <page>/      # group by page when it helps
└── northside/       # images for the Northside test site
```

One folder per business/site; group by page inside when a page has several.

## How images get here

Rendered with **BFL FLUX** (`flux-2-pro`) via the engine's renderer:

```bash
# single image
py engine/render_images.py "warm photo of a golden retriever beside an IATA pet crate at an airport gate, soft morning light, photorealistic, no text" \
   --out images/pawroute/uae-to-uk/hero.png --width 1440 --height 960

# a whole set
py engine/render_images.py --batch jobs.json
# jobs.json = [{ "prompt": "...", "out": "images/pawroute/...png", "width": 1440, "height": 960 }, ...]
```

- Key: `BFL_API_KEY` in `.env` (gitignored).
- Each render is a **real, paid** BFL call — only render what's needed.
- Naming: `images/<site>/<page>/<role>.png` (e.g. `hero.png`, `step-2.png`).

See `skills/image/SKILL.md` for model choice, prompting, dimensions per
platform, and optimization (WebP, OG sizes, alt text).
