# Use-case template

Copy this file, rename it to a descriptive slug, and delete the guidance
comments as you fill it in. One scenario or one incident per file.

There are two submission types.

**Scenario.** A hypothetical deployment, written for calibration. This is the
default. Keep the disclaimer line, and do not describe any real organization's
actual current state.

**Incident.** A documented event, with primary sources. Use this only where
the facts are published by the parties involved or by an investigator with
access, and cite those sources. An incident submission argues about the tier
the deployment was operating at and the tier its risky domains demanded, so it
uses `observed_tier` and `required_tier` in place of `claimed_tier`.

---

```
---
industry: <sector, e.g. consumer-lending>
use_case: <one line: what the AI system does>
submission_type: <scenario | incident>
claimed_tier: <1-4>            # scenario submissions only
observed_tier: <1-4>           # incident submissions only
required_tier: <1-4>           # incident submissions only
threats:                       # slugs from THREATS.md
  - <slug>
  - <slug>
sources:                       # incident submissions only; primary sources first
  - <title> — <url>
---

# <Short title>

> *Illustrative, hypothetical scenario for calibration. Not necessarily
> indicative of any specific organization's current state.*
>
> Incident submissions replace this line with: *Documented incident. Facts are
> drawn from the sources listed in the frontmatter.*

<!--
HOW TO FILL THIS OUT

A Tier is a verifiability claim: how strongly a property is shown to hold,
rather than how good the system is.

  Tier 1  Assertion        the operator's word
  Tier 2  Attestation      a third party vouches
  Tier 3  Trust-minimized  anyone can verify, with no party to trust
  Tier 4  Self-enforcing   the action cannot run without producing evidence

Tiers 1 and 2 both ask you to trust a party. Tiers 3 and 4 do not. A claim
turns on which side of that boundary it sits.

Give each of the six domains its own tier in the table below, with a reason.
The overall tier is the highest bar the risky domains for this use case
demand, rather than an average across all six. Low tiers on domains that carry
no risk here are expected and correct.

The "Why not one tier down?" section is the point of the exercise. Fill it.

Tag every threat the deployment exercises, using THREATS.md. The out-of-scope
column of that file is where the "What Proof-of-Control does not verify here"
section comes from.
-->

## Scenario
Who the user is, what the AI system does, and what is at stake if verification
is weak. Keep it concrete: one user, one decision, real consequences.

## Claimed tier: Tier <N>
Why this use case belongs at this tier. What does reaching this tier require,
and why does this use case specifically need it?

<!-- Incident submissions use these two headings instead:
## Tier observed: Tier <N>
## Tier the risky domains demanded: Tier <N>
-->

## Why not one tier down?
The residual-weakness argument. Name the exact failure mode at Tier <N-1> that
this use case cannot tolerate. That gap is what the next tier up closes.

Two tests help here.

**Reversibility.** Can the harm be undone once you detect it? Money that has
settled, data that has been disclosed, an answer key that has been taken and a
border that has been crossed are all final. Where detection after the fact is
not a remedy, the argument for Tier 4 is that enforcement has to refuse the
action rather than report it.

**Completeness.** At Tier 3 you can verify that the records you hold were not
altered, and you are not guaranteed the record is whole; an agent can act
off-record, and the absence of a record tells you nothing. At Tier 4 the
action cannot execute without producing evidence, so absence of evidence means
the action did not happen. If your use case turns on knowing that you have
seen everything, say so here.

## Tier by domain
How each of the six domains lands here, and why. The overall tier above is set
by the domains that carry the most risk for this use case; the others can sit
lower. Where a domain is not claimed, write "not claimed" rather than leaving
it blank, so a reader takes the claim as silent on it rather than reassuring.

| Domain        | Tier | Why |
|---------------|------|-----|
| Provenance    |      |     |
| Privacy       |      |     |
| Portability   |      |     |
| Authorization |      |     |
| Identity      |      |     |
| Security      |      |     |

## Threats exercised
The threats this deployment is exposed to, from THREATS.md, and what each one
looks like here. Tagging a threat says the deployment is exposed to it, rather
than that the deployment defends against it.

| Threat | What it looks like here |
|--------|-------------------------|
| `<slug>` |  |
| `<slug>` |  |

## What Proof-of-Control does not verify here
Start from the out-of-scope entries for the threats you tagged, then add
anything specific to this deployment. This section is what keeps the claim
readable. A submission with nothing in it is over-claiming.

Verification is not validation. Proof-of-Control shows what an agent did and
whether each action stayed within its controls. It does not judge whether a
control was adequate, whether a decision was sound, or whether an effect
settled in the outside world.

## Residual trust assumptions to disclose
What a reader still has to trust after every claim above holds. Name the roots
of credential issuance, the attestation chain with its version, freshness and
revocation policy, the monitor set for any transparency log and what happens
if monitors lapse, and any point where two attestations are assumed to describe
the same machine.

## Notes / open questions
Anything unresolved, or where reasonable people might place this differently.
If this use case turns on a control that was asserted but never wired into the
execution path, note it here: no tier closes that gap.
```
