---
industry: financial-services
use_case: Deepfake video or biometric used to pass liveness checks and authorize agent access
business_impact: High-value fraudulent transfers with no recoverable authorization trail
claimed_tier: 3
---
# Deepfake Biometric Bypass Authorizing Agent Financial Transfers

> *Illustrative, hypothetical scenario for calibration. Not necessarily
> indicative of any specific organization's current state.*

## Scenario
In January 2024, a finance worker at engineering firm Arup was deceived by
AI-generated deepfakes of his CFO and colleagues on a video call, transferring
$25.6M across 15 transactions before discovering the fraud. As biometric
liveness checks expand to agent authentication flows, the same technique
applies: a deepfaked biometric session passes the liveness check, the platform
issues an authorization token, and an agent executes consequential actions
under that token. The biometric check verified an image, not a legitimate
principal's intent.

Reference: https://www.cnn.com/2024/02/04/asia/deepfake-cfo-scam-hong-kong-intl-hnk

## Claimed tier: Tier 3
Biometric authentication proves that a face passed a liveness check — it does
not prove that the legitimate account holder authorized a specific agent to
act. Tier 3 is required because in the aftermath of a deepfake incident, the
institution, the account holder, and investigators must be able to
independently verify whether a legitimate delegation existed for the disputed
transfers — without relying on the platform's own session logs, which show
only that authentication "succeeded." A spoofed biometric session produces a
passed liveness check but no independently verifiable delegation record; that
absence is itself the evidence that distinguishes fraud from authorized
activity, and it must be checkable by any party without privileged access.

## Why not one tier down?
At Tier 2, an auditor with privileged access can review the platform's
authentication and session logs — but those logs show a successful biometric
check and a valid-looking authorization token. The deepfake produced exactly
the records a legitimate session would produce. Operator-held logs therefore
cannot distinguish the fraud, and in a dispute the account holder is left
contesting the platform's own records. Tier 3 closes this by making the
delegation record independently verifiable and cryptographically separate
from the authentication event: anyone can check whether a valid delegation
rooted in the legitimate principal existed for those transfers, without the
platform's cooperation.

## Tier by domain
| Domain        | Tier | Why |
|---------------|------|-----|
| Provenance    | 3    | Whether a transfer was rooted in a legitimate principal's delegation must be independently verifiable, not inferred from session logs |
| Authorization | 3    | The delegation record must be cryptographically separate from the spoofable authentication event and checkable by any party in a dispute |
| Security      | 2    | Liveness detection and session security remain necessary controls, but third-party assessment of those controls is sufficient |
| Identity      | 3    | The binding between the legitimate account holder and any authorized agent must be independently verifiable, not dependent on biometric liveness |
| Privacy       | 2    | Standard financial privacy controls apply |
| Portability   | 1    | Not a primary risk domain for this use case |

## Notes / open questions
- This use case makes the strongest case for separating authentication
  (who you appear to be) from authorization (what you have delegated an
  agent to do). These are architecturally separate problems that current
  platforms often conflate.
- Reasonable to argue Tier 4 for high-value transfer thresholds, where
  post-facto verification is too late and execution should be mechanically
  gated on a valid delegation credential — the Arup pattern ($25.6M across
  15 transactions in one session) is the argument for that stricter stance.
  As with the pig-butchering case, a Tier 4 claim would additionally depend
  on where the delegation chain is rooted and how the signing keys are held.
- Open question: does hardware-attested identity (TEE-bound keys) satisfy
  the delegation requirement, or is a separate cryptographic delegation
  layer always required?
