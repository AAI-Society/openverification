---
industry: financial-services
use_case: Pig butchering scam — scammer-controlled agent operates on victim-provided credentials to drain accounts
business_impact: Irreversible account losses and platform liability for unauthorized agent execution
claimed_tier: 4
---
# Pig Butchering: Socially Engineered Credential Handoff Enabling Rogue Agent

> *Illustrative, hypothetical scenario for calibration. Not necessarily
> indicative of any specific organization's current state.*

## Scenario
A victim is socially engineered over weeks into trusting a fraudulent
"investment advisor" — the pattern known as pig butchering. The FBI's
Operation Level Up (2024) identified over 8,100 victims of such schemes,
with estimated losses exceeding $285M in the first year of the operation
alone. The victim voluntarily hands over account credentials. The scammer
deploys an agent that drains the account using those credentials. The
platform cannot distinguish this agent from the legitimate account holder's
own agent because credentials were provided willingly — there is no breach
signal to detect.

Reference: https://www.fbi.gov/how-we-can-help-you/victim-services/national-crimes-and-victim-resources/operation-level-up

## Claimed tier: Tier 4
The distinctive challenge here is that the credential transfer was voluntary.
Standard fraud signals (unusual login location, brute force patterns) are
absent. Only a cryptographic delegation chain rooted in the legitimate account
holder's verified identity can distinguish an authorized agent from a
scammer's agent operating on gifted credentials. This must be enforced at
execution — a scammer's agent presents no valid chain and cannot act.

Whether this use case actually reaches Tier 4 depends on two architectural
conditions, not just the presence of a delegation chain:

1. **Where the chain is rooted.** The root must be a verified identity bound
   to the legitimate account holder (e.g., identity-proofed at enrollment),
   not merely to whoever holds the account credentials. A chain rooted in
   credential possession inherits the same weakness as the credentials — a
   scammer who obtains credentials could mint a valid-looking chain.

2. **How the signing keys are held.** If the account holder's delegation
   signing key is held client-side (device-bound, hardware-backed, or
   biometrically gated on the holder's own device), a scammer with
   credentials cannot issue delegations. If the key is held or escrowed by
   the platform and exercised on the user's behalf after login, the
   delegation gate collapses back into the authentication gate — and the
   use case degrades to Tier 2, since trust returns to the operator.

Tier 4 holds only when both conditions are met: identity-proofed root,
non-exportable holder-controlled keys, and fail-closed execution.

## Why not one tier down?
At Tier 3, independent verification confirms after the fact that the agent
lacked a valid delegation chain from the legitimate account holder. But the
account is already drained. Pig butchering victims often do not discover the
fraud until withdrawal is blocked or the scammer disappears — by then the
harm is irreversible. Tier 4's fail-closed enforcement prevents execution
entirely: no valid chain, no action.

## Tier by domain
| Domain        | Tier | Why |
|---------------|------|-----|
| Provenance    | 4    | Agent must be provably traceable to a delegation chain rooted in the legitimate account holder, not just the credential holder |
| Authorization | 4    | Voluntary credential sharing must not confer agent authorization; delegation must be cryptographically separate from authentication |
| Security      | 4    | Execution must be gated; detection after voluntary credential transfer is insufficient |
| Identity      | 4    | The legitimate account holder's identity must be cryptographically bound to any agent authorized to act on their behalf |
| Privacy       | 2    | Standard financial privacy controls apply; the risk domain here is authorization, not data exposure |
| Portability   | 1    | Not a primary risk domain for this use case |

## Notes / open questions
- This use case exposes a foundational gap: most financial platforms treat
  authentication (proving you have the credentials) as equivalent to
  authorization (proving you are the legitimate account holder authorizing
  an agent). Proof of Control separates these.
- The voluntary nature of the credential transfer makes behavioral anomaly
  detection largely ineffective, which is why this is a strong Tier 4 case.
- Tier 4 here is conditional on key custody architecture. Platform-held or
  escrowed delegation keys reduce this to Tier 2 regardless of chain
  cryptography. The standard should require key custody disclosure as part
  of the Transparent property for this class of use case.
- This is fundamentally a social attack, which makes it one of the hardest
  cases in the set. The humans are part of the system, and legitimate intent
  is genuinely present: the victim *wants* to give the scammer access at the
  moment they do it. No verification tier can prevent a persuaded account
  holder from being persuaded. What Tier 4 changes is the mechanics of what
  persuasion can yield. Handing over credentials no longer hands over agent
  authority — the scammer must instead get the victim to actively issue a
  delegation from their own verified identity and holder-controlled keys.
  That is a higher-friction, more explicit act ("authorize this agent to
  move funds") that creates a natural intervention point for warnings,
  cooling-off periods, and scoped/capped grants. PoC narrows the blast
  radius of successful manipulation; it does not eliminate manipulation.
- Boundary for the working group: if the scammer socially engineers the
  victim through the delegation ceremony itself, the resulting chain is
  cryptographically valid. The standard verifies control, not the quality
  of the human judgment behind a grant — worth stating explicitly so PoC
  conformance is not misread as anti-fraud certification.
