# Coverage index

**10 of 29 threats have a worked use case.** 2 submissions.

Generated from the `threats:` frontmatter across this folder. Do not
edit by hand: run `python3 make_coverage.py`.

## By family

| Family | Covered | |
|---|---|---|
| Instruction and goal manipulation | 0/3 | `░░░░░░░░░░░░░░░░░░░░` |
| Memory, knowledge, and supply chain | 1/4 | `█████░░░░░░░░░░░░░░░` |
| Identity, authority, and inter-agent trust | 4/4 | `████████████████████` |
| Tools, actions, and effects | 1/4 | `█████░░░░░░░░░░░░░░░` |
| Data exposure | 1/1 | `████████████████████` |
| Autonomy, drift, and lifecycle | 1/3 | `███████░░░░░░░░░░░░░` |
| Record integrity and resilience | 2/5 | `████████░░░░░░░░░░░░` |
| Human oversight and disclosure | 0/2 | `░░░░░░░░░░░░░░░░░░░░` |
| Output quality and availability | 0/3 | `░░░░░░░░░░░░░░░░░░░░` |

## Threats with no use case yet

A submission covering one of these helps most.

| Family | Threat | |
|---|---|---|
| Instruction and goal manipulation | `prompt-injection` | Prompt injection / goal hijacking |
| Instruction and goal manipulation | `bent-goals` | Poisoned or bent goals |
| Instruction and goal manipulation | `system-prompt-leakage` | System prompt leakage |
| Memory, knowledge, and supply chain | `memory-poisoning` | Memory and context poisoning |
| Memory, knowledge, and supply chain | `rag-weakness` | Vector, embedding or retrieval weakness |
| Memory, knowledge, and supply chain | `model-poisoning` | Training-time data or model poisoning |
| Tools, actions, and effects | `tool-misuse` | Tool misuse |
| Tools, actions, and effects | `unsafe-actuation` | Unsafe actuation |
| Tools, actions, and effects | `improper-output-handling` | Improper output handling |
| Autonomy, drift, and lifecycle | `autonomy-creep` | Autonomy creep |
| Autonomy, drift, and lifecycle | `scope-creep-lifecycle` | Scope creep and lifecycle |
| Record integrity and resilience | `cascading-failure` | Cascading failure or fail-open |
| Record integrity and resilience | `coverage-decay` | Coverage decay |
| Record integrity and resilience | `trust-opacity` | Trust opacity |
| Human oversight and disclosure | `approval-fatigue` | Human-agent trust exploitation or approval fatigue |
| Human oversight and disclosure | `undisclosed-ai` | Undisclosed AI or absent consent |
| Output quality and availability | `misinformation` | Misinformation or hallucination |
| Output quality and availability | `hidden-bias` | Hidden bias |
| Output quality and availability | `unbounded-consumption` | Unbounded consumption |

## Every threat

| Family | Threat | Use cases |
|---|---|---|
| Instruction and goal manipulation | `prompt-injection` | — |
| Instruction and goal manipulation | `bent-goals` | — |
| Instruction and goal manipulation | `system-prompt-leakage` | — |
| Memory, knowledge, and supply chain | `memory-poisoning` | — |
| Memory, knowledge, and supply chain | `rag-weakness` | — |
| Memory, knowledge, and supply chain | `model-poisoning` | — |
| Memory, knowledge, and supply chain | `supply-chain-poisoning` | `frontier-lab-agent-collective` |
| Identity, authority, and inter-agent trust | `identity-abuse` | `frontier-lab-agent-collective` |
| Identity, authority, and inter-agent trust | `context-blind-authorization` | `frontier-lab-agent-collective` |
| Identity, authority, and inter-agent trust | `excessive-agency` | `frontier-lab-agent-collective` |
| Identity, authority, and inter-agent trust | `insecure-inter-agent-comms` | `frontier-lab-agent-collective` |
| Tools, actions, and effects | `tool-misuse` | — |
| Tools, actions, and effects | `unexpected-code-execution` | `frontier-lab-agent-collective` |
| Tools, actions, and effects | `unsafe-actuation` | — |
| Tools, actions, and effects | `improper-output-handling` | — |
| Data exposure | `data-exfiltration` | `frontier-lab-agent-collective` |
| Autonomy, drift, and lifecycle | `autonomy-creep` | — |
| Autonomy, drift, and lifecycle | `behavioral-drift` | `frontier-lab-agent-collective` |
| Autonomy, drift, and lifecycle | `scope-creep-lifecycle` | — |
| Record integrity and resilience | `audit-tampering` | `frontier-lab-agent-collective` |
| Record integrity and resilience | `cascading-failure` | — |
| Record integrity and resilience | `coverage-decay` | — |
| Record integrity and resilience | `evidence-repudiation` | `frontier-lab-agent-collective` |
| Record integrity and resilience | `trust-opacity` | — |
| Human oversight and disclosure | `approval-fatigue` | — |
| Human oversight and disclosure | `undisclosed-ai` | — |
| Output quality and availability | `misinformation` | — |
| Output quality and availability | `hidden-bias` | — |
| Output quality and availability | `unbounded-consumption` | — |

## Every use case

| Use case | Threats tagged |
|---|---|
| `credit-decisioning` | **none tagged** |
| `frontier-lab-agent-collective` | `insecure-inter-agent-comms`, `audit-tampering`, `excessive-agency`, `context-blind-authorization`, `identity-abuse`, `unexpected-code-execution`, `data-exfiltration`, `supply-chain-poisoning`, `behavioral-drift`, `evidence-repudiation` |
