# Open Verification

**The Proof-of-Control Standard for AI Agents** — Working Draft v0.1.4, open for public comment until **October 30, 2026**.

## What is Open Verification?

In open verification, the root of trust is a mechanism anyone can verify, not a party anyone must believe. Open verification carries the ethos of open source software into the agentic era, extending it from inspecting source code to verifying the actions agents take in the agentic stack. It is a category of approaches that is purpose-built for the agentic age, where deployment of non-deterministic agents requires mechanisms that remove the need to trust a single gatekeeper.

**Proof-of-Control** is the open-verification approach this standard defines for AI agents. It produces a continuously verifiable chain of custody: tamper-evident evidence of what an agent did — the data it touched and the actions it took — guaranteeing the *integrity* of what happened, not the correctness of what the agent produced.

## Why it matters

AI is moving from systems that answer to agents that act. Every boundary an agent crosses — a database, another company's system, a payment rail, a medical record — is a place where evidence of what it did goes missing. Today, the only account of what happened is usually the system's own, and that account can be mistaken, manipulated, or rewritten after the fact. This is the **Verifiability Gap**: the widening distance between what AI agents do and anyone's ability to openly verify that they stayed within the controls they were given.

Enterprises cannot demonstrate to their boards what their agents did. Regulators cannot verify that a high-risk system operated within authorized parameters. Insurers cannot underwrite what they cannot audit. Proof-of-Control closes that gap with evidence anyone can verify.

## The core of the standard

- **Six domains of verification** — what evidence is produced about: **Provenance, Privacy, Portability, Authorization, Identity, Security**.
- **Four Verifiability Tiers** — how openly the evidence can be verified, i.e., who you must trust:
  1. **Assertion** — the operator's word
  2. **Attestation** — a third party vouches
  3. **Trust-minimized** — anyone can verify with published tools; the parties its soundness rests on are disclosed rather than removed
  4. **Self-enforcing** — verification is built into operation; the system cannot run if integrity breaks
- **The binary threshold** — a system has Proof-of-Control or it does not. The line falls between Tiers 2 and 3: below it, authenticated documentation; above it, openly verifiable evidence.
- **Four evidence properties** — evidence must be **binary, contemporaneous, tamper-evident, and transparent**.

The standard is technology-neutral (it defines what the evidence must be, not which mechanism produces it), vendor-neutral, and designed to complement — not replace — existing frameworks like NIST AI RMF, ISO/IEC 42001, SOC 2, MAESTRO, and OWASP.

## Status

This is a **working draft, not a final standard**. It is currently in public comment (until October 30, 2026). When public comment closes, the normative core of the specification graduates to this repository as the canonical, versioned source of truth. The standard is developed in the open, stewarded by the Advanced AI Society, and published under CC BY 4.0.

## This repository: use-case stories

Right now this repo hosts **[Verifiability Use-Case Stories](Proof-of-Control/use_cases/)** — illustrative scenarios that map real-world AI use cases onto the six domains and four tiers. They act as a calibration corpus for the standard.

### Submit a use case

1. Copy [`Proof-of-Control/use_cases/_TEMPLATE.md`](Proof-of-Control/use_cases/_TEMPLATE.md) and rename it to a short slug (e.g. `clinical-triage.md`).
2. Fill in the frontmatter (`industry`, `use_case`, `claimed_tier`) and each section, including **"Why not one tier down?"**
3. One story per file; keep the disclaimer line at the top.
4. Open a pull request.

See the [use-cases README](Proof-of-Control/use_cases/README.md) for full guidance.

## Get involved

- **Comment on the draft** during the public-comment period — open working-group questions are marked `⚠️ [WG-INPUT NEEDED]` throughout the draft.
- **Join a working group** — one for each of the six domains, plus an insurance working group.
- **Contribute a use case** — via pull request, as described above.

## License

The specification is freely available under **CC BY 4.0**. See [LICENSE](LICENSE) for this repository's license.
