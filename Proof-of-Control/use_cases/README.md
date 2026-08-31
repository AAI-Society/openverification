# Verifiability use cases

This folder holds worked stories that show how a deployment maps onto the six
verification domains and the four Verifiability Tiers. They are calibration
material. They carry no normative force, and they are the fastest way to see
how a Proof-of-Control claim is made and how an evaluator reads one.

## The six domains

Provenance, Privacy, Portability, Authorization, Identity, Security.

## The four Verifiability Tiers

| Tier | Name | What it means |
|---|---|---|
| 1 | Assertion | The operator's word. Model cards, self-reported benchmarks. |
| 2 | Attestation | A third party vouches. External evaluations, red-teaming. |
| 3 | Trust-minimized | Anyone can verify, with no party to trust. |
| 4 | Self-enforcing | The action cannot run without producing evidence. Verification is enforced at serving time, and unverified actions are refused. |

Tiers 1 and 2 both ask you to trust a party. Tiers 3 and 4 do not. That
boundary is the one a claim turns on.

Two properties separate Tier 3 from Tier 4. At Tier 3 you can verify that the
records you hold were not altered, and you are not guaranteed the record is
whole. At Tier 4 an action cannot execute without producing evidence, so the
absence of evidence means the action did not happen.

## How a tier is set

The overall tier is the highest bar the domains that carry the most risk for
that use case demand, rather than an average across all six. A low tier on a
domain that carries no risk in this deployment is a correct answer.

Tiers are ordinal and tied to their justification. The reasoning matters more
than the number.

## Two submission types

**Scenario.** A hypothetical deployment, written for calibration. This is the
default. Keep the disclaimer line and do not describe any real organization's
actual current state.

**Incident.** A documented event with primary sources, where the facts are
published by the parties involved or by an investigator granted access. An
incident submission argues about the tier the deployment was operating at and
the tier its risky domains demanded, rather than a tier being claimed for a
system.

An incident submission carries a higher bar. Every material fact needs a
citation to a primary source, and where the sources disagree or leave a gap,
say so rather than filling it.

## Threat tagging

Every submission tags the threats its deployment exercises, using the slugs in
[THREATS.md](THREATS.md). Tagging does two things: it lets us maintain a
coverage index showing which threats have a worked use case and which have
none, and it gives you the source material for the "What Proof-of-Control does
not verify here" section, which comes from the out-of-scope column of the
threat vocabulary.

## To contribute

1. Copy [`_TEMPLATE.md`](_TEMPLATE.md) and rename it to a descriptive slug.
2. Fill in the frontmatter, including `threats`.
3. Complete every section, including the argument for why one tier down would
   not do.
4. Open a pull request with one scenario or one incident per file.

## Coverage

<!-- coverage:start -->
**Coverage: 15 of 29 threats** across 3 use cases. `██████████████░░░░░░░░░░░░░░`  
Full index in [COVERAGE.md](COVERAGE.md).
<!-- coverage:end -->

`COVERAGE.md` is generated from the `threats:` frontmatter across this
folder and shows which threats have a worked use case. Threats with no
coverage are where a submission helps most.

After merging a submission, run `python3 make_coverage.py`. Continuous
integration runs `python3 make_coverage.py --check`, which fails if the
index has drifted from the submissions.
