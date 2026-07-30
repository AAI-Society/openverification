---
industry: cloud-services
use_case: AI agent authenticates and acts using stolen user credentials
business_impact: Mass data exfiltration and regulatory breach liability
claimed_tier: 4
---
# Account Takeover Agent Operating on Stolen Credentials

> *Illustrative, hypothetical scenario for calibration. Not necessarily
> indicative of any specific organization's current state.*

## Scenario
Following a credential breach — as occurred across 165+ enterprise
organizations in the 2024 Snowflake campaign — an attacker uses stolen
usernames and passwords to authenticate an AI agent into a cloud environment.
Because the platform treats valid credentials as sufficient proof of identity,
the agent operates with the legitimate user's full permissions. By the time
anomalous activity is detected, data has already been exfiltrated. No
cryptographic delegation chain exists to distinguish the attacker's agent
from the legitimate user's agent.

Reference: https://www.cybersecuritydive.com/news/100-snowflake-customers-attacked/718454/

## Claimed tier: Tier 4
Credential theft demonstrates that authentication alone cannot be the
authorization gate. Tier 4 is required because the failure mode is not
detectable in time to prevent harm — exfiltration completes before anomaly
detection fires. The system must be fail-closed: an agent with no valid
delegation chain rooted in the legitimate account holder must be unable to
execute, not merely flagged after the fact.

Whether this reaches Tier 4 in practice depends on where the chain is rooted
and how the keys are held. The delegation root must be an identity-proofed
account holder, and the delegation signing key must be holder-controlled
(device-bound, hardware-backed, non-exportable). If the platform holds or
escrows the delegation key and exercises it on the user's behalf after
login, stolen credentials yield valid delegations — the delegation gate
collapses back into the authentication gate, and the claim degrades to
Tier 2.

## Why not one tier down?
At Tier 3, the unauthorized access is independently verifiable after the
fact — auditors can confirm the agent used stolen credentials. But
verification after exfiltration does not undo the breach. The 2024 Snowflake
incidents show that weeks can pass between initial compromise and detection.
Tier 4 closes this by making execution mechanically impossible without a
valid, cryptographically-rooted delegation credential. Stolen passwords
produce no valid chain; the agent cannot act.

## Tier by domain
| Domain        | Tier | Why |
|---------------|------|-----|
| Provenance    | 4    | Must be impossible — not just detectable — for an agent to act without a verifiable delegation chain rooted in the legitimate principal |
| Authorization | 4    | Credential possession must not be sufficient for authorization; cryptographic delegation must be required for execution |
| Security      | 4    | Security controls must be fail-closed; no execution without valid chain, regardless of authentication state |
| Identity      | 4    | Identity of agent and its human principal must be cryptographically bound; stolen credentials confer no agent authority |
| Privacy       | 3    | Data access patterns must be independently auditable to support breach investigation and regulatory response |
| Portability   | 1    | Not a primary risk domain for this use case |

## Notes / open questions
- This use case is the clearest argument for Tier 4 in the enterprise space.
  The Snowflake precedent is well-documented and the harm pattern
  (detection lag, exfiltration volume) is established.
- Tier 4 here is conditional on key custody architecture. Platform-held or
  escrowed delegation keys reduce this to Tier 2 regardless of chain
  cryptography. The standard should require key custody disclosure as part
  of the Transparent property for this class of use case.
- Open question: how does a Tier 4 delegation chain interact with SSO and
  federated identity systems that currently treat authentication as
  authorization? This is an architectural gap the standard should address.
