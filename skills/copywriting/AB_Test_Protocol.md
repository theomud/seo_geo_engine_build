# A/B Test Protocol

> Backed by `claim_bank.csv` (Kohavi/Tang/Xu 2020; Larsen et al., The American Statistician
> 2024). The headline risk is **peeking**; this protocol exists to prevent false wins.

## Before the test

- [ ] **Hypothesis** stated as: changing X will improve [primary metric] because [mechanism].
      For lead-gen the primary metric is a **conversion event** (quote request / qualified
      enquiry), not pageviews.
- [ ] **One primary metric** chosen in advance; guardrail metrics listed.
- [ ] **MDE** (minimum detectable effect) chosen -- the smallest lift worth detecting.
- [ ] **Sample size & duration** fixed in advance from MDE, baseline rate, power (typically
      0.8) and significance (alpha 0.05). Run full business cycles (avoid day-of-week bias).
- [ ] **A/A sanity check** considered to validate the testing setup.

## During the test

- [ ] **Do NOT peek-and-stop.** Repeatedly checking and stopping when it "looks significant"
      inflates false positives. *(well-established; Kohavi/Tang/Xu 2020.)*
- [ ] If you need to monitor continuously, use a **sequential testing** method with Type-I /
      FDR control rather than naive repeated significance tests.
      *(well-established; Larsen et al. 2024.)*
- [ ] Do not change the variant mid-flight; do not add traffic sources mid-test.

## After the test

- [ ] Reach the pre-registered sample size / stopping rule before deciding.
- [ ] Report effect size with a confidence/credible interval, not just a p-value.
- [ ] Check guardrail metrics did not regress.
- [ ] Treat any single vendor-style "+X% uplift" as **specific to this test**, not a universal
      law. *(caveat; vendor uplift figures are context-specific.)*

## Decision

- Ship if the primary metric improved beyond MDE with control of false positives and no
  guardrail regression. Otherwise iterate or revert. Log the result to feed the calibration
  loop.
