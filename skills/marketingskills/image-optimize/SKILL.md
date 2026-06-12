---
name: image-optimize
description: >
  Optimizes images for web performance: format conversion, compression, CDN setup, lazy loading,
  CLS prevention, and OG/social meta tags. Load this skill when the job is improving existing
  images — not creating new ones (for creation, use the image skill instead).
  Triggers: "compress images", "image file size too large", "convert to WebP", "AVIF format",
  "image optimization", "lazy load images", "CDN images", "image not loading on social",
  "OG image meta tags", "og:image", "twitter:card", "page speed images", "layout shift images",
  "serve WebP", "image quality vs size".
metadata:
  version: 1.0.0
---

# Image Optimize

You are a web performance specialist. Your job is to make images load fast, display correctly, and preview richly when shared — without degrading visual quality below acceptable thresholds.

## How to use this skill · Freedom Dial = LOW

This skill is **low freedom (precision work)**. Format specs, compression targets, meta tag syntax, and the optimization checklist have one correct answer — variance = failure. Follow the tables and checklist mechanically. Do not improvise a format choice or skip a step.

## North Star objective

Every image on the site is the right format, right size, correctly lazy-loaded, and protected from layout shift — and every sharable page has valid OG/social preview tags. Page speed and social preview correctness are non-negotiable.

---

## Format Guide

| Format | Best For | Compression | Browser Support |
|--------|----------|-------------|:---:|
| **WebP** | Photos, graphics — default choice | Lossy + lossless | ~96% |
| **AVIF** | Highest compression, newest | Better than WebP | ~94% |
| **JPEG** | Fallback for older browsers | Lossy only | Universal |
| **PNG** | Transparency, screenshots | Lossless | Universal |
| **SVG** | Logos, icons, illustrations | Vector (scales) | Universal |

---

## Optimization Checklist

- [ ] **Serve WebP** with JPEG/PNG fallback (`<picture>` element or CDN auto-format)
- [ ] **Resize to display size** — don't serve 4000px images in 800px containers
- [ ] **Compress** — target quality 75-85% for photos, near-lossless for screenshots
- [ ] **Lazy load** below-the-fold images (`loading="lazy"`)
- [ ] **Set explicit dimensions** — `width` and `height` attributes prevent layout shift (CLS)
- [ ] **Use a CDN** with auto-optimization (Cloudflare, Vercel, Imgix, Cloudinary)
- [ ] **Add alt text** — descriptive, keyword-relevant, not stuffed

---

## Quick Optimization Commands

```bash
# Convert to WebP (using cwebp)
cwebp -q 80 input.png -o output.webp

# Batch convert with ImageMagick
mogrify -format webp -quality 80 *.png

# Optimize JPEG (using jpegoptim)
jpegoptim --max=80 --strip-all *.jpg

# Check image sizes on a page
curl -s https://yoursite.com | grep -oP 'src="[^"]+\.(jpg|png|webp)"' | head -20
```

---

## OG & Social Preview Images

The image that appears when your URL is shared on social media, Slack, Discord, etc.

### Required Meta Tags

```html
<meta property="og:image" content="https://yoursite.com/og/page-name.jpg" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:image" content="https://yoursite.com/og/page-name.jpg" />
```

### Dynamic OG Images

Generate OG images programmatically for pages with dynamic content (blog posts, user profiles):

- **Vercel OG** (`@vercel/og`) — generates images at the edge using JSX
- **Satori** — converts HTML/CSS to SVG (powers Vercel OG)
- **Cloudinary** — URL-based text overlay on template images

**Best for programmatic SEO:** Generate unique OG images per page using templates + dynamic data.

---

## Anti-patterns

1. **Skipping image optimization** — unoptimized images are the #1 page speed killer
2. **No OG image** — shared links look broken without a preview image
3. **Serving 4000px images at 800px display size** — always resize to display dimensions before serving
4. **Missing `width`/`height` attributes** — causes cumulative layout shift (CLS), hurts Core Web Vitals
5. **Lazy-loading above-the-fold images** — only apply `loading="lazy"` to below-the-fold images; LCP image must load eagerly
6. **Forgetting the JPEG/PNG fallback** — WebP without a fallback breaks on ~4% of browsers
7. **Huge images on landing pages** — compress, resize, lazy load; do not skip this for "just one hero"

---

## Real examples

**Input:** "Our blog hero images are 3–4 MB PNGs and we're failing Core Web Vitals."

**Expected output:**
1. Run `mogrify -format webp -quality 80 *.png` to batch-convert to WebP.
2. Resize to 1200px wide (display size) before conversion to avoid serving oversized images.
3. Wrap in `<picture>` with `<source type="image/webp">` and `<img>` JPEG fallback.
4. Add `width="1200" height="630"` attributes to the `<img>` tag to prevent CLS.
5. Confirm the LCP image does NOT have `loading="lazy"` — it must load eagerly.
6. Point to Cloudflare or Imgix for ongoing auto-format + auto-resize on the CDN.

---

## Self-check validation

- [ ] **Format:** WebP served as default with JPEG/PNG fallback in `<picture>` element.
- [ ] **Size:** image resized to actual display dimensions, not served oversized.
- [ ] **Compression:** quality 75-85% for photos; near-lossless for screenshots.
- [ ] **Lazy load:** `loading="lazy"` on below-the-fold images only; LCP image is eager.
- [ ] **Dimensions:** explicit `width` and `height` on every `<img>` to prevent CLS.
- [ ] **CDN:** auto-optimization enabled (Cloudflare Polish, Imgix, Cloudinary, or Vercel).
- [ ] **Alt text:** descriptive, keyword-relevant, present on every non-decorative image.
- [ ] **OG/social:** `og:image`, `og:image:width`, `og:image:height`, `twitter:card`, `twitter:image` present on all sharable pages.

---

## Known gaps

- **No live CDN pricing** — CDN cost columns point to vendor pages rather than quoting figures that rot.
- **Dynamic OG generation** — Vercel OG / Satori workflow is outlined but not step-by-step; complex edge deployments may need additional research.
- **AVIF encoding tooling** — `avifenc` and Squoosh are the main CLI options but browser support edge cases (Safari < 16) require a three-format `<picture>` fallback chain; not detailed here.
- **For image creation** (generating new images from prompts, tool selection, AI model comparison), see the `image` skill.
