---
industry: technology
use_case: Threat actor uses deepfake identity to pass hiring process and gain insider system access
business_impact: Persistent agent-level insider access that survives human threat actor detection
claimed_tier: 4
---
# Nation-State Actor Uses Deepfake to Gain Insider Agent Access

> *Illustrative, hypothetical scenario for calibration. Not necessarily
> indicative of any specific organization's current state.*

## Scenario
In July 2024, KnowBe4 unknowingly hired a North Korean operative who used
an AI-generated identity to pass four video interviews and background checks.
Upon receiving a company laptop, the operative immediately attempted to install
malware. In an agentic environment, the same vector produces a worse outcome:
once hired, the operative is a legitimate employee record in the HR system
and identity provider, and the platform does not gate what a credentialed
employee is permitted to do — provisioning agents is within the normal
authority their role confers. The threat actor provisions and delegates to
internal AI agents whose authority derives from that employee record,
embedding persistent access into automated workflows that survive the
operative's own detection and termination. The registration authority the
agents chain back to — the employer's own HR and identity systems — is
exactly the system the fraudulent identity has already defeated.

Reference: https://blog.knowbe4.com/how-a-north-korean-fake-it-worker-tried-to-infiltrate-us

## Claimed tier: Tier 4
Employment onboarding must not automatically confer agent authorization.
The structural problem is where the root of trust sits: if the delegation
chain is rooted in the employee record, then the employer — whose hiring
and identity-proofing process has already been defeated — is vouching for
itself. That is a Tier 2 root of trust at best, and in this scenario it is
a compromised one. Tier 4 requires that the trust anchor sit outside the
employment record entirely: agent provisioning must chain to an
independently verified organizational identity (identity-proofed
enrollment, holder-controlled keys, an anchor external to the HR/IdP
stack), and enforcement must be fail-closed — an agent whose chain roots
only in employment status cannot execute. A threat actor who defeats the
hiring process gains an employee record, but no valid root, and therefore
no agents.

## Why not one tier down?
At Tier 3, an investigation can independently verify that an agent was
provisioned by a threat actor using a fraudulent identity — after malware
is deployed or data is exfiltrated. The KnowBe4 incident was discovered
within 25 minutes of the laptop being powered on; in an agentic workflow,
agents provisioned before detection continue operating after the human
threat actor is locked out. And because the employee record is the very
artifact the fraud produced, independent verification that chains back to
that record verifies nothing — it confirms a fraudulent registration as
valid. Tier 4 closes both gaps: the root of trust is anchored outside the
defeated registration system, and agents cannot be provisioned or operated
without a chain to that external anchor.

## Tier by domain
| Domain        | Tier | Why |
|---------------|------|-----|
| Provenance    | 4    | Agent provisioning must be cryptographically traceable to a trust anchor outside the employer's HR/IdP stack, not to employment records the fraud produced |
| Authorization | 4    | Employment must not confer agent authorization; delegation must chain to independently verified identity and be enforced at execution |
| Security      | 4    | Agent provisioning must be fail-closed; a fraudulently onboarded employee must be unable to provision persistent agents |
| Identity      | 4    | The identity of anyone provisioning agents must be verified against a root of trust external to the registration system the deepfake defeated |
| Privacy       | 2    | Standard data access controls apply; the risk domain here is agent provisioning, not data exposure |
| Portability   | 1    | Not a primary risk domain for this use case |

## Notes / open questions
- The root-of-trust placement is the crux: a delegation chain rooted in the
  employee record inherits the integrity of the hiring process, which is the
  attack surface in this scenario. The standard should require that Tier 4
  claims for provisioning authority disclose where the trust anchor sits and
  demonstrate it is independent of the registration system being protected.
- Related: agent provisioning rights should themselves be treated as a
  delegatable permission requiring Tier 4 verification, not an implicit
  consequence of role assignment.
- The KnowBe4 case is the best-documented public incident for this pattern;
  the agentic extension is currently hypothetical but architecturally
  straightforward.
