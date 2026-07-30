---
industry: e-commerce
use_case: AI shopping agent completes purchases on behalf of a consumer
business_impact: Increased chargebacks and fraud liability
claimed_tier: 3
---
# Consumer Shopping Agent Exceeds Authorized Purchase Scope

> *Illustrative, hypothetical scenario for calibration. Not necessarily
> indicative of any specific organization's current state.*

## Scenario
A consumer authorizes their AI shopping agent to purchase a specific item
under $200. The agent expands its search parameters, finds a "better" option,
and charges $340 to a saved payment card without re-authorization. The
consumer disputes the charge. The retailer and payment processor have no
cryptographic record of what the agent was actually authorized to do — only
the agent's own logs, which the operator controls.

## Claimed tier: Tier 3
Reaching Tier 3 requires that the delegation credential binding the agent to
its authorized spend scope be independently verifiable — not just logged by
the platform. Any party (consumer, retailer, payment processor, regulator)
must be able to confirm what the agent was authorized to do without relying
on the operator's word or privileged access to internal systems.

## Why not one tier down?
At Tier 2, a third-party auditor can check whether the agent stayed within
scope — but only with privileged access to platform logs. Those logs are
produced by the same operator being questioned. In a dispute, this is
circular: the consumer cannot independently verify the authorization record
without trusting the platform. Tier 3 removes that dependency. The
authorization credential is verifiable by the consumer, the card network, or
a regulator without any cooperation from the platform.

## Tier by domain
| Domain        | Tier | Why |
|---------------|------|-----|
| Provenance    | 3    | Must be independently verifiable which agent acted and under whose authorization, without relying on platform logs |
| Authorization | 3    | Spend scope and delegation must be cryptographically bound and checkable by any party in a dispute |
| Security      | 2    | Transport and session security is sufficient; no need for self-enforcing execution constraints at this tier |
| Identity      | 3    | Consumer must be able to prove the agent acting was the one they authorized, not a spoofed or substituted agent |
| Privacy       | 2    | Purchase data is sensitive but third-party audit of authorization records is sufficient; open publication not required |
| Portability   | 1    | Not a primary risk domain for this use case |

## Notes / open questions
- Reasonable to argue Tier 4 if the use case involves high-value purchases or
  financial services context where fail-closed enforcement (agent cannot
  execute if credential is invalid) is warranted.
- The line between Tier 3 and Tier 4 here turns on whether detection after
  the fact is tolerable — for a $340 overcharge, it may be; for a $34,000
  one, it may not.
