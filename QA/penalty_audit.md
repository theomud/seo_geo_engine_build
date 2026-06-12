# Penalty and Suppression Audit

Use this before publishing and during monthly reviews.

## Failure modes

### Banned

Manual action shown in Search Console.

Check:

- paid links
- link schemes
- cloaking
- sneaky redirects
- scraped content
- doorway pages
- fake structured data
- hidden text

### Ghosted

Algorithmic suppression with no message.

Check:

- thin content
- content built only for search
- off-topic mass publishing
- bad user satisfaction
- weak page quality
- duplicated pages
- low trust signals

### Not ranking

No penalty. The page simply lacks authority, relevance, links, intent match, or quality.

Check:

- weak topical authority
- wrong intent
- insufficient evidence
- weak internal links
- no unique value
- no reason to rank

## QA verdict

```yaml
penalty_audit:
  manual_action_risk: low_medium_high
  ghosting_risk: low_medium_high
  not_ranking_risk: low_medium_high
  required_fixes: []
  publish_allowed: true_or_false
```
