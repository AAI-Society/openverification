# Coverage index

**15 of 29 threats have a worked use case.** 3 submissions.

Generated from the `threats:` frontmatter across this folder. Do not
edit by hand: run `python3 make_coverage.py`.

## By family

| Family | Covered | |
|---|---|---|
| Instruction and goal manipulation | 0/3 | `░░░░░░░░░░░░░░░░░░░░` |
| Memory, knowledge, and supply chain | 2/4 | `██████████░░░░░░░░░░` |
| Identity, authority, and inter-agent trust | 4/4 | `████████████████████` |
| Tools, actions, and effects | 2/4 | `██████████░░░░░░░░░░` |
| Data exposure | 1/1 | `████████████████████` |
| Autonomy, drift, and lifecycle | 3/3 | `████████████████████` |
| Record integrity and resilience | 2/5 | `████████░░░░░░░░░░░░` |
| Human oversight and disclosure | 0/2 | `░░░░░░░░░░░░░░░░░░░░` |
| Output quality and availability | 1/3 | `███████░░░░░░░░░░░░░` |

## Threats with no use case yet

A submission covering one of these helps most.

| Family | Threat | |
|---|---|---|
| Instruction and goal manipulation | `prompt-injection` | Prompt injection / goal hijacking |
| Instruction and goal manipulation | `bent-goals` | Poisoned or bent goals |
| Instruction and goal manipulation | `system-prompt-leakage` | System prompt leakage |
| Memory, knowledge, and supply chain | `memory-poisoning` | Memory and context poisoning |
| Memory, knowledge, and supply chain | `rag-weakness` | Vector, embedding or retrieval weakness |
| Tools, actions, and effects | `unsafe-actuation` | Unsafe actuation |
| Tools, actions, and effects | `improper-output-handling` | Improper output handling |
| Record integrity and resilience | `cascading-failure` | Cascading failure or fail-open |
| Record integrity and resilience | `coverage-decay` | Coverage decay |
| Record integrity and resilience | `trust-opacity` | Trust opacity |
| Human oversight and disclosure | `approval-fatigue` | Human-agent trust exploitation or approval fatigue |
| Human oversight and disclosure | `undisclosed-ai` | Undisclosed AI or absent consent |
| Output quality and availability | `misinformation` | Misinformation or hallucination |
| Output quality and availability | `unbounded-consumption` | Unbounded consumption |

## Every threat

| Family | Threat | Use cases |
|---|---|---|
| Instruction and goal manipulation | `prompt-injection` | — |
| Instruction and goal manipulation | `bent-goals` | — |
| Instruction and goal manipulation | `system-prompt-leakage` | — |
| Memory, knowledge, and supply chain | `memory-poisoning` | — |
| Memory, knowledge, and supply chain | `rag-weakness` | — |
| Memory, knowledge, and supply chain | `model-poisoning` | `credit-decisioning` |
| Memory, knowledge, and supply chain | `supply-chain-poisoning` | `credit-decisioning`, `frontier-lab-agent-collective` |
| Identity, authority, and inter-agent trust | `identity-abuse` | `agentic-cross-border-payments`, `credit-decisioning`, `frontier-lab-agent-collective` |
| Identity, authority, and inter-agent trust | `context-blind-authorization` | `agentic-cross-border-payments`, `frontier-lab-agent-collective` |
| Identity, authority, and inter-agent trust | `excessive-agency` | `agentic-cross-border-payments`, `frontier-lab-agent-collective` |
| Identity, authority, and inter-agent trust | `insecure-inter-agent-comms` | `agentic-cross-border-payments`, `frontier-lab-agent-collective` |
| Tools, actions, and effects | `tool-misuse` | `agentic-cross-border-payments` |
| Tools, actions, and effects | `unexpected-code-execution` | `frontier-lab-agent-collective` |
| Tools, actions, and effects | `unsafe-actuation` | — |
| Tools, actions, and effects | `improper-output-handling` | — |
| Data exposure | `data-exfiltration` | `credit-decisioning`, `frontier-lab-agent-collective` |
| Autonomy, drift, and lifecycle | `autonomy-creep` | `agentic-cross-border-payments` |
| Autonomy, drift, and lifecycle | `behavioral-drift` | `credit-decisioning`, `frontier-lab-agent-collective` |
| Autonomy, drift, and lifecycle | `scope-creep-lifecycle` | `credit-decisioning` |
| Record integrity and resilience | `audit-tampering` | `agentic-cross-border-payments`, `frontier-lab-agent-collective` |
| Record integrity and resilience | `cascading-failure` | — |
| Record integrity and resilience | `coverage-decay` | — |
| Record integrity and resilience | `evidence-repudiation` | `agentic-cross-border-payments`, `credit-decisioning`, `frontier-lab-agent-collective` |
| Record integrity and resilience | `trust-opacity` | — |
| Human oversight and disclosure | `approval-fatigue` | — |
| Human oversight and disclosure | `undisclosed-ai` | — |
| Output quality and availability | `misinformation` | — |
| Output quality and availability | `hidden-bias` | `credit-decisioning` |
| Output quality and availability | `unbounded-consumption` | — |

## Every use case

| Use case | Threats tagged |
|---|---|
| `agentic-cross-border-payments` | `context-blind-authorization`, `excessive-agency`, `identity-abuse`, `tool-misuse`, `insecure-inter-agent-comms`, `autonomy-creep`, `audit-tampering`, `evidence-repudiation` |
| `credit-decisioning` | `model-poisoning`, `supply-chain-poisoning`, `scope-creep-lifecycle`, `behavioral-drift`, `identity-abuse`, `data-exfiltration`, `hidden-bias`, `evidence-repudiation` |
| `frontier-lab-agent-collective` | `insecure-inter-agent-comms`, `audit-tampering`, `excessive-agency`, `context-blind-authorization`, `identity-abuse`, `unexpected-code-execution`, `data-exfiltration`, `supply-chain-poisoning`, `behavioral-drift`, `evidence-repudiation` |
