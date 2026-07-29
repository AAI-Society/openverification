---
industry: software-and-cloud-services
use_case: AI coding agent requesting promotion of an approved security patch
claimed_tier: 4
---

# AI coding agent requesting production promotion under delegated authority

> *Illustrative, hypothetical scenario for calibration. Not necessarily
> indicative of any specific organization's current state.*

## Scenario

A platform engineer delegates a bounded task to an AI coding agent: remediate
a dependency vulnerability in one service. Unlike a fixed deployment script,
the agent chooses edits and calls tools across source control, CI, an artifact
registry, and the deployment API without a human approving each intermediate
step. It may inspect the repository, edit a branch, and request CI runs. It
does not hold a reusable production credential.

The protected action is a compare-and-swap update of the authoritative
deployment reference for one production service, from its expected current
digest to one approved artifact digest. Runtime rollout happens afterward and
is outside the Tier 4 claim. Before the production target accepts the reference
update, it evaluates authorization evidence bound to:

- the artifact digest, target service, operation, and expected current
  production state;
- the principal's delegation, including its scope and validity window;
- the committed policy version and the required review and CI records; and
- a nonce or equivalent replay guard.

The policy can check that the required records exist and match the request. It
cannot establish that a reviewer exercised good judgment or that the tests
were adequate. Source, build, and registry statements also retain their
disclosed roots of trust; a signature does not make the asserted lineage true.

## Claimed tier: Tier 4

The Tier 4 requirement is narrow: Authorization for the production mutation.
The production target's update protocol verifies the action-bound evidence
before changing the authoritative reference. It then performs the state check
and reference update atomically, so the verified precondition cannot change
between authorization and mutation. Missing, invalid, stale, replayed, or
mismatched evidence leaves the reference unchanged.

Every mutation of that reference, including an emergency change, uses a
separately scoped delegation but the same verifier and atomic, fail-closed
update protocol. No out-of-band credential or API exists inside the claim
boundary.

The scenario does not prescribe a proof system or require proof of a
frontier-model inference. Anyone can run the published authorization-verification
procedure without discretionary cooperation from the agent or operator. The
evidence still carries the trust roots and assumptions disclosed in the
lower-tier domain claims.

## Why not one tier down?

At Tier 3, anyone could independently check the cryptographic bindings and
recorded policy result under the disclosed trust roots. The evidence could even
be generated at deployment time. The authoritative reference could still
change without first requiring a successful check.

For a privileged software change, detection is not the required control. A
substituted artifact can expose data, alter access, or disrupt service before
rollback begins, and rollback cannot undo those effects. Tier 4 closes that gap
by making successful verification a precondition of the production state
change.

## Tier by domain

Authorization drives the overall Tier 4. The other rows state the evidence
strength this scenario actually describes; the numbers are not averaged.

| Domain        | Tier | Why |
|---------------|------|-----|
| Provenance    | 2 | Source, build, CI, and registry records are signed by identified systems and assessed under disclosed trust roots. The Tier 4 Authorization gate binds the already-approved artifact digest; it does not elevate the full lineage claim. |
| Authorization | 4 | The production target updates the authoritative reference only after independently verifying that the artifact, target, operation, policy, delegation, freshness data, and current state fit the authorized envelope. No path inside the claim boundary can skip that check. |
| Security      | 2 | Attestations and assessments can show that named controller and CI configurations matched approved references, but they still depend on attestors or hardware and software roots. The story makes no broader security claim. |
| Identity      | 2 | Principal, agent, and workload credentials are authenticated, but their binding still depends on credential issuers and key-management processes. Identity is an input to Authorization, not evidence that the actor is trustworthy. |
| Privacy       | 1 | The scenario makes no independently assessed or verifiable privacy claim about source, test, or incident data. |
| Portability   | 2 | An open evidence package carries the same action and artifact identifiers across source control, CI, the registry, and deployment. Its records remain rooted in the systems that issue them, so continuity can be appraised but is not yet independently verifiable without those parties. |

No conformance stage is claimed. This hypothetical assigns target evidence
strength to a control design; it does not represent a Self-Declared,
Third-Party Assessed, or Continuously Monitored deployment.

## Claim boundary

The Tier 4 claim supports one conclusion: the production target applied the
committed authorization predicate to the action-bound evidence and refused the
state transition unless it passed. It assumes that the policy reflects its
authors' intent, the cryptographic mechanism and verifier are sound, freshness
and replay controls work, and the stated claim boundary is complete. Failure of
one of those assumptions invalidates or lowers the claim.

The evidence does not show that the patch is correct or secure, that a human
review was careful, that CI covered every relevant failure, or that authenticated
lineage statements were truthful beyond their disclosed roots. A bad patch
that satisfies the committed policy can still pass the gate. Code review,
testing, incident response, and human accountability remain necessary.

The pre-action authorization record is also separate from the deployment
outcome. After actuation, the controller may emit a completion record describing
the resulting state it observed. That record does not prove that every runtime
instance is healthy or that the rollout achieved its intended effect.

## Notes / open questions

- Evidence crosses four administrative surfaces: source control, CI, artifact
  registry, and deployment. Does independently verifiable continuity belong
  under Portability, or should continuity across boundaries become an evidence
  property of its own?
- Should the standard require separate, linked records for pre-action
  authorization and post-action completion, so an authorization record cannot
  be mistaken for evidence of the deployment outcome?
