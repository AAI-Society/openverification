# Verifiability Use-Case Stories

Illustrative, hypothetical scenarios that map real-world AI use cases onto the
**Verifiability Matrix**. Each story claims a **Verifiability Tier** for a use
case and shows the per-domain reasoning behind it. Together they act as a
calibration corpus for the standard.

## The Verifiability Matrix

- **Six verification domains** (columns): Provenance, Authorization, Security,
  Identity, Privacy, Portability.
- **Four Verifiability Tiers** (rows): how strongly a claim is verified.

### Verifiability Tiers

- **Tier 1 (self-reported).** Asserted by the provider, e.g. model cards and
  self-reported benchmarks.
- **Tier 2 (independently evaluated).** Checked by a third party, e.g. external
  evaluations and red-teaming.
- **Tier 3 (open and reproducible).** Anyone can independently reproduce the
  check, e.g. open weights and reproducible eval harnesses. Detection after the
  fact.
- **Tier 4 (self-enforcing).** Verification is enforced at serving time and
  **fails closed**: an unverified action can't be served, not merely flagged
  afterward, e.g. an attested serving gate.

Per-domain definitions of each tier are being refined by the working groups;
treat the above as the general ladder.

## How the overall tier is set

A story's overall tier is the **highest bar the domains that carry the most
risk** for that use case demand, not an average across all six. Low tiers on
domains that don't carry risk are expected and fine.

## Tiers are ordinal, tied to their justification

A tier is a claim about verification strength, and it only means something
alongside its reasoning. Don't average tiers or compare bare numbers across
stories.

Two similar use cases can end up with different tier numbers, because submitters
apply their own judgment and bring their own context. Read the "why," not the
number. Different takes are expected, and open collaboration is encouraged, so
bring them to the discussion.

## Contributing

1. Copy `_TEMPLATE.md` and rename it to a short slug (e.g. `clinical-triage.md`).
2. Fill in the frontmatter (`industry`, `use_case`, `claimed_tier`) and each
   section, including **"Why not one tier down?"**
3. One story per file. Keep the disclaimer line at the top.
4. From the repository root, run:

   ```sh
   python3 scripts/validate_use_cases.py
   ```

5. Open a PR.

Stories are **hypothetical illustrations for calibration, not representations of
any specific organization's current state.**

The command catches structural problems before review. It does not judge
whether a tier assignment is correct, establish that a claim is true, or
determine conformance with the standard.
