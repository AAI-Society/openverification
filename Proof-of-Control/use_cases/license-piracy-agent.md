---
industry: software-publishing
use_case: Previously flagged threat actor deploys AI agents to bulk-purchase and pirate software licenses at scale
business_impact: Revenue loss and inability to enforce prior bad actor history across synthetic agent identities
claimed_tier: 3
---
# Known Threat Actor Using Agents to Scale License Fraud Under New Identities

> *Illustrative, hypothetical scenario for calibration. Not necessarily
> indicative of any specific organization's current state.*

## Scenario
A threat actor previously identified for using bots to bulk-purchase software
licenses and resell pirated copies now deploys AI agents to do the same at
scale, cycling through synthetic identities to evade prior flagging. Each
agent presents a new, unconnected identity. The software publisher has no
mechanism to link the new agent identities to the known bad actor's
accountability chain — the prior violation history is invisible because the
actor's Responsible Party identity is not cryptographically bound to the
agents being deployed.

## Claimed tier: Tier 3
Tier 3 requires that the Responsible Party behind any agent be independently
verifiable by the software publisher, without relying on the actor's
self-reported identity. This allows prior violation history to attach to the
accountability chain regardless of how many synthetic identities are cycled
through. Any party — publisher, platform, enforcement body — can verify the
chain without privileged access to the publisher's internal fraud database.

## Why not one tier down?
At Tier 2, a third-party fraud auditor can check whether a given agent is
linked to a known bad actor — but only with privileged access to the
publisher's internal records and with the auditor's cooperation. This is
too slow and too dependent on platform cooperation to be operationally
useful for real-time purchase enforcement. Tier 3 makes the Responsible
Party chain independently verifiable at the point of transaction.

## Tier by domain
| Domain        | Tier | Why |
|---------------|------|-----|
| Provenance    | 3    | The Responsible Party behind any purchasing agent must be independently verifiable, regardless of synthetic identity cycling |
| Authorization | 2    | Purchase authorization is legitimate in isolation; the risk is identity laundering, not authorization scope |
| Security      | 2    | Standard platform security controls apply; the risk here is identity, not access control |
| Identity      | 3    | Agent identity must be cryptographically bound to a Responsible Party whose history is independently verifiable |
| Privacy       | 2    | Purchaser identity verification is standard; open publication of identity records is not required |
| Portability   | 2    | Fraud records should be portable across platforms; full open verifiability not required for this use case |

## Notes / open questions
- This use case does not yet have a canonical public incident in the AI agent
  context. The bot-based version of this attack is well-documented; the agent
  version is an emerging threat pattern.
- Open question: what is the minimum Responsible Party verification required
  to satisfy Tier 3 here? did:web anchored to a real organization, or
  something stronger?
- Reasonable to argue Tier 2 if the publisher is willing to accept
  third-party fraud scoring as sufficient; Tier 3 is appropriate if the
  publisher needs to act without auditor cooperation.
