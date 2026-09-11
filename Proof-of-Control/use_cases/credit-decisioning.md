---
industry: consumer-lending
use_case: AI assisting credit decisions on loan applications
claimed_tier: 4
---

# AI-assisted consumer credit decisioning

> *Illustrative, hypothetical scenario for calibration. Not necessarily
> indicative of any specific organization's current state.*

## Scenario
A lender uses an AI model to score loan applications and issue approve/deny
decisions. Applicants have a legal right to the reasons behind an adverse
decision, and an unapproved or drifted model must never be the one that decides
a live application. If verification is weak, a model other than the approved one
can issue a real decision to a real applicant, and the lender only finds out,
if ever, after the fact.

## Claimed tier: Tier 4
Credit decisions are legally consequential and acted on immediately, so
detection after the fact is not enough: a wrong decision has already reached the
applicant. Tier 4 makes serving **fail-closed**. Before any decision is issued,
a live check verifies that the exact approved model, in its approved
configuration, is what will serve. If that check fails, no decision is issued,
so an unapproved model never reaches an applicant in the first place.

## Why not one tier down?
Tier 3 gives open weights, reproducible evals, and an audit log, so you can
prove *after the fact* which model ran on a given application. But that is
detection, not prevention: an unapproved or drifted model can still issue a live
decision before any audit catches it, and by then the applicant has been
approved or denied. For a legally consequential decision the applicant has
already relied on, that lag is exactly the failure that matters. Tier 4 closes
it by refusing to serve unless the live attestation of model and config passes,
so the wrong model is blocked at issuance, not flagged later.

## Tier by domain
The overall Tier 4 is driven by provenance and authorization, the two domains
where a fail-closed gate is required. Portability barely matters here, which is
expected; the claimed tier reflects the highest bar the risky domains impose,
not an average across all six.

| Domain        | Tier | Why |
|---------------|------|-----|
| Provenance    | 4 | A live gate verifies which model and config is about to serve and blocks issuance if it is not the approved one. This is the driver. |
| Authorization | 4 | Only the approved model in the approved configuration is permitted to serve; anything else means the decision cannot be issued. |
| Security      | 3 | Adversarial setting (applicants game scores); pipeline integrity is openly verifiable but not fully fail-closed on every vector. |
| Identity      | 3 | Each issued decision binds to an accountable model and operator identity. |
| Privacy       | 2 | Sensitive financial PII, regulated; handled by data controls and third-party assessment rather than an enforcement gate. |
| Portability   | 1 | Whether the decision is portable across systems is not what makes it verifiable; self-reported. |

## Notes / open questions
- Tier 4 here means the serving gate is **fail-closed and attested**, not that
  the model computation is proven with zero-knowledge methods. Proving the
  inference itself (zkML) was raised as not currently feasible; this example
  deliberately relies on attested, fail-closed serving plus an audit log, not on
  proof of the computation.
- Tier 4 proves the *approved* model served. It does **not** prove the approved
  model is fair, well-aligned, or trained on good data; those are established at
  earlier tiers (evaluation, red-teaming) and remain necessary. Tier 4 assumes
  them rather than replacing them.
