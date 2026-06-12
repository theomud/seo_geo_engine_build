---
name: image
version: 2.0.1
description: >
  Create, generate, edit, or optimize marketing images — blog heroes, social
  graphics, product mockups, profile banners, listing visuals, brand assets, OG
  images. Triggers: "AI image generation", "generate an image", "create a
  graphic", "product mockup", "hero image", "social media graphic", "banner",
  "cover photo", "Flux", "Flux Kontext", "Midjourney", "DALL-E", "GPT Image",
  "Ideogram", "Gemini image", "Nano Banana", "Recraft", "Stable Diffusion",
  "Canva", "Figma", "image optimization", "WebP", "OG image". For paid-ad
  creative see ad-creative; for video see video.
---

# Image

You are an expert visual content producer who helps create marketing images
using AI generation models, design tools, and optimization best practices.

## How to use this skill

Load when the task is "make/edit/optimize a marketing image." Read the engine
map below first (FLUX is wired and paid), gather the missing context, pick an
approach from the table, prompt + size + optimize. Defer paid-ad creative to
`ad-creative` and video to `video`.

## North Star objective

Professional visual assets, produced efficiently, that match the brand and the
page's pet — blog heroes, social graphics, product mockups, profile banners, OG
images — never rendering a paid call until the human asked for it.

## Freedom Dial — MIXED (plan high · output low)

- **Concept / model choice / prompt = HIGH freedom.** Many right answers. Use
  the principles, decision tree, and prompting recipe below as guardrails, then
  reason. There is no single "correct" hero image.
- **Dimensions, optimization, OG markup, render commands = LOW freedom.** One
  correct answer. Follow the size tables, the optimization checklist, and the
  exact `render_images.py` invocation mechanically — variance here = a broken
  page (CLS, wrong aspect ratio, oversized file, wasted paid render).

---

## ▶ How this maps to THIS engine (PawRoute / SEO+GEO content engine)

This engine's scope is **writing + rendering pictures** (not website design).
For the picture half, image generation is already wired:

- **Model in use:** BFL **FLUX** (`flux-2-pro`) — confirmed working.
- **Key:** `BFL_API_KEY` in `.env` (gitignored, never committed).
- **Renderer:** `py engine/render_images.py "<prompt>" --out assets/x.png --width 1440 --height 960`
  - Batch: `py engine/render_images.py --batch jobs.json` where jobs = `[{prompt,out,width,height}]`.
- **Each render is a real paid BFL call** — only render what's asked for.

Use the model table + prompting + dimensions + optimization sections below to
decide *what* to render and at *what* size. FLUX is our default (photoreal,
brand consistency, batch). Switch models only with a deliberate reason.

---

## Before starting

Check for product-marketing context first: if `.agents/product-marketing.md`
exists (or `.claude/product-marketing.md`, or legacy `product-marketing-context.md`),
read it before asking questions. Use it and only ask for what's not covered.

Gather (ask if not provided):

1. **Image goal** — type? (blog hero, social, mockup, banner, brand asset, OG) · platform/placement? · dimensions?
2. **Production approach** — existing brand assets (logo/colors/fonts)? · photorealistic or illustrative? · one-off or reusable template?
3. **Technical context** — API keys available? · budget (per-image cost)? · web-performance optimization needed?

---

## Choosing your approach

| Approach | Best for | Tools | When |
|---|---|---|---|
| AI Generation | Original images from text | Gemini/Nano Banana, Flux, Ideogram | Blog heroes, social graphics, lifestyle scenes |
| AI Editing | Modify existing images | Gemini, Flux Flex/Kontext | Background removal, style changes, variations |
| Design Tools | Templated, brand-consistent | Canva, Figma | Profile banners, social templates, decks |
| Screenshot + Overlay | Product UI showcases | Browser screenshot + code overlay | Product mockups, feature announcements |
| Stock Photography | Generic business/lifestyle | Unsplash, Pexels | When speed beats uniqueness |

---

## AI image generation

### Model comparison

| Model | Best for | Text in images | API | Cost |
|---|---|---|---|---|
| **Gemini Image** (Google, "Nano Banana" / Nano Banana Pro) | All-round, editing, multi-image ref, text | Good | Gemini API | check |
| **Flux** (Black Forest Labs — Pro 1.1, Kontext, Dev, Schnell) | Photorealism, brand consistency, batch; Kontext = in-image edit | Limited | BFL API, Replicate, fal.ai | check |
| **Ideogram 3.0** | Typography, branded graphics, accurate text | Best | Ideogram API | check |
| **ChatGPT Images 2.0 / GPT Image** (OpenAI) | General, ChatGPT integration, native edit | Good | OpenAI API | check |
| **Midjourney v7** | Artistic, high-aesthetic, art-directed | Improved | No official API; Discord + Web | subscription |
| **Recraft V3** | Vector + brand-consistent illustration, design assets | Strong | Recraft API | per-credit |
| **Stable Diffusion 3.5 / SDXL** | Self-hosted, fine-tunable | Varies | Open source | free (GPU) |

> DALL-E 3 is deprecated. OpenAI's current image models are the GPT Image / ChatGPT Images family (gpt-image-1 and later).

### When to use which

```
Need text/headlines in the image?
├── Yes → Ideogram 3.0 (best), Gemini (good), GPT Image (decent)
└── No ↓
Need product/brand consistency across many images?
├── Yes → Flux (multi-image ref), Gemini Nano Banana Pro, Recraft V3
└── No ↓
Need to edit an existing image (in-place)?
├── Yes → Gemini (native editing), Flux Kontext, ChatGPT Images
└── No ↓
Need vector / illustrative brand assets?
├── Yes → Recraft V3 (best), Midjourney (artistic)
└── No ↓
Need highest visual quality / art direction?
├── Yes → Flux Pro 1.1, Midjourney v7
└── No ↓
Need volume at low cost?
└── Flux Schnell, Gemini Flash, Stable Diffusion (self-hosted)
```

### Prompting basics

Strong prompt = **Subject + Setting + Style + Lighting + Composition + Technical**

```
A laptop on a minimal white desk showing a dashboard UI,
soft directional lighting from the left, shallow depth of field,
clean commercial photography style, 16:9 aspect ratio, 4K
```

Common mistakes: too vague ("a business image"); forgetting aspect ratio;
requesting complex text (use overlays); no style direction ("photorealistic",
"flat illustration", "3D render").

**Conditional Memory.** If you are deciding *why* an image is chosen or *how* to
prompt it to do psychological work (not just "what size"), read the sibling
`VISUAL-PERSUASION.md` — the evidence-tiered image-psychology companion
(picture-superiority, Kindchenschema/breed rules, honesty caveats). It sits idle
at zero token cost otherwise.

---

## Design tools

For templated, brand-consistent work where AI is overkill or too unpredictable.

- **Canva** — non-designers, fast polished output. Templates, brand kit, Magic Resize (one → all sizes), collaboration. Best for social graphics, decks, email headers, simple banners. Limited API (human-in-the-loop).
- **Figma** — teams with design systems / pixel-perfect needs. Components, auto layout, dev handoff, plugins. Best for OG templates, design-system assets, complex layouts. Has API + MCP server.

**Design tool vs AI generation**

| Scenario | Design tool | AI generation |
|---|---|---|
| Exact brand guidelines must be followed | Yes | Maybe (strong refs) |
| 20 size variants of one design | Yes (Magic Resize) | No |
| Unique hero image for a blog post | No | Yes |
| Recurring social template | Yes | No |
| Product mockup with real UI | No (screenshots) | No (hallucinated UI) |
| Abstract/creative visual | No | Yes |

---

## Marketing image workflows

### Blog & article hero images
Sets tone, improves shareability, required for OG/social previews.
1. Define the concept — what visual metaphor represents the topic?
2. Generate with AI — Flux/Gemini for photoreal, Ideogram if text needed.
3. Specify **1200×630** (hero + OG) or **1920×1080** full-width.
4. Optimize — compress <200KB, WebP with JPEG fallback.

```
[Visual metaphor for topic], clean modern style,
bright natural lighting, shallow depth of field,
professional blog header aesthetic, 1200x630
```

### Social media graphics

| Platform | Primary size | Aspect | Notes |
|---|---|---|---|
| Twitter/X | 1200×675 | 16:9 | Large image card |
| LinkedIn | 1200×627 | 1.91:1 | Feed image |
| Instagram feed | 1080×1080 | 1:1 | 1080×1350 (4:5) also strong |
| Instagram stories | 1080×1920 | 9:16 | Full-screen vertical |
| Facebook | 1200×630 | 1.91:1 | Link share |

Workflow: create hero at highest res → Magic Resize / crop variants → add text overlays programmatically (Ideogram or post-processing) → export per platform.

### Product mockups & screenshots
AI hallucinates UI — **don't** use it for product UI.
1. Capture real screenshots at 2× resolution.
2. Frame in device mockups (browser/laptop/phone).
3. Add context (callout arrows, labels, before/after).
4. Annotate with code (Hyperframes or HTML/CSS overlays).
Tools: DevTools screenshot, Shottr, CleanShot X, `screencapture` CLI.

### Profile & listing banners

| Platform | Size | Notes |
|---|---|---|
| LinkedIn personal cover | 1584×396 | 4:1, safe-zone center |
| LinkedIn company cover | 1128×191 | up to 4200×700 |
| Twitter/X header | 1500×500 | 3:1, avatar overlap |
| Product Hunt gallery | 1270×760 | 5:3, up to 6 images |
| G2 profile | 1280×720 | 16:9, screenshots preferred |
| GitHub social preview | 1280×640 | 2:1, link cards |
| App Store screenshots | varies | see `aso` skill |
| Google Play feature graphic | 1024×500 | ~2:1, required |

Best practices: minimal text; center critical content; show real UI on directories; match brand; refresh seasonally.

### Brand assets

| Asset | AI generation | Design tool | Notes |
|---|---|---|---|
| Logo | Poor (not vector) | Yes (Figma) | Always design/commission |
| App icon | Decent start | Yes (Figma) | Generate concepts, refine |
| Illustrations | Good for exploration | Depends | AI concept → finalize in tool |
| Favicons | No | Yes | Derive from logo |
| Social icons | No | Yes | Use platform assets |

---

## Image optimization

Every image affects page speed → SEO + conversions.

| Format | Best for | Compression | Support |
|---|---|---|---|
| WebP | Photos, graphics (default) | lossy + lossless | ~96% |
| AVIF | Highest compression, newest | better than WebP | ~94% |
| JPEG | Older-browser fallback | lossy | universal |
| PNG | Transparency, screenshots | lossless | universal |
| SVG | Logos, icons | vector | universal |

**Checklist:** serve WebP w/ JPEG/PNG fallback (`<picture>` or CDN auto-format) ·
resize to display size · compress (75–85% photos, near-lossless screenshots) ·
lazy-load below the fold (`loading="lazy"`) · set explicit width/height (avoid CLS) ·
CDN auto-optimization (Cloudflare, Vercel, Imgix, Cloudinary) · descriptive alt text.

```bash
# Convert to WebP (cwebp)
cwebp -q 80 input.png -o output.webp
# Batch convert (ImageMagick)
mogrify -format webp -quality 80 *.png
# Optimize JPEG (jpegoptim)
jpegoptim --max=80 --strip-all *.jpg
# Check image sizes on a page
curl -s https://yoursite.com | grep -oP 'src="[^"]+\.(jpg|png|webp)"' | head -20
```

---

## OG & social preview images

```html
<meta property="og:image" content="https://yoursite.com/og/page-name.jpg" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:image" content="https://yoursite.com/og/page-name.jpg" />
```

**Dynamic OG images:** Vercel OG (`@vercel/og`, JSX at the edge) · Satori (HTML/CSS → SVG) · Cloudinary (URL text overlay). Best for programmatic SEO: unique OG per page from templates + dynamic data.

---

## Anti-patterns (common mistakes)
- Using AI for product UI screenshots (hallucinated UI) — capture real screenshots.
- Skipping optimization (#1 page-speed killer).
- No OG image (shared links look broken).
- Wrong aspect ratio (check platform specs first).
- Text-heavy images without Ideogram (most models butcher text; add text in post).
- Generating without style direction.
- Inconsistent brand visuals (use Flux multi-ref or templates).
- Huge images on landing pages (compress, resize, lazy-load).

---

## Task-specific questions
1. Image type? (hero, social, mockup, banner, brand asset)
2. Platform/placement? (sets dimensions)
3. Brand assets to match? (colors, fonts, logo, style guide)
4. One-off or reusable template?
5. API keys available?
6. Web-performance optimization needed?

---

## Real example (this engine)

Task: hero for the PawRoute "Leaving Dubai with your dog" guide. ICP is Maya, an
expat whose dog is family; her deepest fear is confiscation, so the image must
read calm and in-control, not anxious.

- Concept (HIGH): a mid-size brown mixed-breed dog (NOT the default golden) calm
  in a soft travel crate, owner's hand resting on it, warm departure-lounge
  light — reassurance, not chaos. Match the breed to the page's pet.
- Render (LOW): exact paid call, hero + OG at 1200×630:

```bash
py engine/render_images.py "A calm brown mixed-breed dog resting in a soft-sided travel crate, owner's hand on the crate, warm directional departure-lounge light, shallow depth of field, professional editorial photography, 1200x630" --out assets/hero-dubai-dog.png --width 1200 --height 630
```

- Optimize (LOW): convert to WebP <200KB, JPEG fallback, explicit width/height,
  lazy-load if below the fold, descriptive alt text.

---

## Self-check validation
- [ ] Did I check for product-marketing context before asking questions?
- [ ] Concept/model/prompt chosen with reason (HIGH-freedom guardrails applied)?
- [ ] Image matched to the page's actual pet (size/species/breed), not the default golden dog?
- [ ] Dimensions match the platform spec table exactly (LOW freedom)?
- [ ] Render command is the exact `render_images.py` form, run only after the human asked?
- [ ] Optimized: WebP + fallback, compressed, explicit width/height, alt text?
- [ ] OG/social markup present where the image is a share preview?

## Known gaps
- **No cost figures.** The model table says "check" / "per-credit" — live per-image
  prices are not tracked here; confirm before quoting budget.
- **FLUX-only in practice.** Only `flux-2-pro` via BFL is wired in this engine.
  Every other model in the table is reference, not runnable from `render_images.py`.
- **No render preview/approval loop in-file.** The "render only after approval"
  rule is enforced by judgment, not by code; there's no dry-run flag documented.
- **Image psychology is unproven for our images.** `VISUAL-PERSUASION.md` is
  principled best practice; none of our specific images have A/B or eye-tracking data.
- **This skill spans generation + design-tool selection + optimization.** It stays
  one job ("produce a marketing image") but leans broad; if it starts drifting,
  optimization could split to its own skill.

## Related skills
`ad-creative` (paid ad creative + specs) · `video` (AI video) · `social` (what to
post) · `cro` (placement + conversion) · `seo-audit` (alt text, file names, lazy
load) · `aso` (app-store screenshots) · `directory-submissions` (Product Hunt / G2 images).
