# External skill repos — evaluation & what we adopt

*License-checked review of community GitHub skills. We adopt ideas/patterns only from
permissive licenses, with attribution; we do NOT copy copyleft (GPL) code into this engine.*

| Repo | License | Verdict | What we take |
|---|---|---|---|
| **AgriciDaniel/claude-seo** | **MIT** ✅ safe | Comprehensive (25 sub-skills, 18 agents); core works offline | **Headless renderer** (Playwright + trafilatura) — more robust than our regex parser; **schema validators**; **Google-API credential tiers** (for when we add GSC/PSI). API extensions (DataForSEO/Firecrawl) are optional bring-your-own-key. |
| **Cognitic-Labs/geoskills** | **Apache-2.0** ✅ safe | 6 GEO skills, no keys, local analysis | **`llms.txt` generation** (the AI-crawler equivalent of robots.txt — *we don't have this*; adopting now); their GEO weighted dims (Citability 35% · Structured 20% · Technical 20% · Entity 25%) to cross-check our GEO lens; geo-monitor concept (our `ai_citation.py` already covers). |
| **AI2HU/gego** | **GPL-3.0** ⚠️ copyleft | GEO tracker across LLMs (OpenAI/Anthropic/Gemini/Perplexity/Ollama) | **Ideas only — no code copied** (GPL would force our licence). Validates our `ai_citation.py`; ideas worth adding later: auto keyword-extraction from responses, cron scheduling, response metadata (latency/tokens). |

## Adopted now
- ✅ **`llms.txt`** generation in `engine/build.py` (idea from geoskills; our own implementation). Lists the site's key pages + descriptions for AI crawlers — closes a genuine GEO gap (we had sitemap.xml + robots.txt but no llms.txt).

## Adopt next (when prioritised)
- **Headless renderer** (claude-seo, MIT): swap the auditor's regex parser for Playwright + trafilatura for more robust extraction on JS/SPA pages. (We already use Playwright for verification.)
- **GEO-dimension calibration**: weight our GEO lens against geoskills' Citability-heavy split once we have live AI-citation data to calibrate against.
- **Citation harness enhancements** (gego ideas, not code): keyword extraction from answers + scheduled re-runs (we already have multi-provider querying).

## Rule
Permissive (MIT/Apache) → adopt ideas/files with attribution. Copyleft (GPL) → ideas only, never code.
Always review the `SKILL.md` + run nothing untrusted; third-party skills can contain scripts.
