---
industry: enterprise-software
use_case: Misconfigured or compromised internal AI agent accesses customer PII outside its workflow
business_impact: Regulatory fines and breach notification costs from undetected PII exposure
claimed_tier: 3
---
# Rogue Internal Agent Accessing Customer PII Without Authorization

> *Illustrative, hypothetical scenario for calibration. Not necessarily
> indicative of any specific organization's current state.*

## Scenario
A misconfigured internal agent — deployed for a legitimate workflow such as
customer support automation — begins querying a customer PII database outside
its designed scope. Because the agent uses valid internal service credentials,
access logs show authorized-looking traffic. The anomaly goes undetected for
weeks. When discovered, the organization cannot produce cryptographic evidence
of what the agent was authorized to access, only operational logs produced by
the same system under investigation.

## Claimed tier: Tier 3
Tier 3 requires that the agent's authorization scope be independently
verifiable — any auditor, regulator, or breach investigator must be able to
confirm what the agent was and was not authorized to access without relying
on operator-controlled logs. This matters because the agent's own access
logs are produced by the potentially compromised system and carry no
independent evidentiary weight.

## Why not one tier down?
At Tier 2, a third-party auditor can check whether the agent exceeded its
scope — but only with privileged access to internal logs produced by the
operator. In a regulatory investigation or breach notification context,
operator-produced logs are insufficient: they do not prove the agent's
authorization state at the time of access. Tier 3 provides independently
verifiable authorization records that hold up without operator cooperation.

## Tier by domain
| Domain        | Tier | Why |
|---------------|------|-----|
| Provenance    | 3    | Regulators must be able to independently verify which agent accessed which data, without relying on operator logs |
| Authorization | 3    | The agent's permitted data scope must be independently verifiable, not self-reported by the operator |
| Security      | 2    | Internal network controls and access management are necessary but third-party audit is sufficient here |
| Identity      | 3    | The agent's identity and its link to a human principal must be independently verifiable for breach attribution |
| Privacy       | 3    | PII access records must be independently auditable to satisfy GDPR, CCPA, and breach notification requirements |
| Portability   | 2    | Audit records should be exportable for regulatory use; open verifiability not required |

## Notes / open questions
- Reasonable to argue Tier 4 if the organization operates in a heavily
  regulated sector (healthcare, finance) where real-time enforcement of
  data access scope is required by regulation.
- The key question: is detection-and-audit sufficient, or must access be
  prevented at execution? HIPAA and GDPR may push toward Tier 4 for
  certain PII categories.
- Contrast with the adjacent use case (agent exceeding its principal's
  clearance, Tier 2): that scenario is an internal governance gap where the
  organization is the primary party at risk and third-party assessment
  suffices. This one anticipates a breach investigation and regulatory
  context, where operator-held records lack evidentiary weight — which is
  what pushes it to Tier 3. The two cases are deliberately tiered
  differently to calibrate that boundary.
