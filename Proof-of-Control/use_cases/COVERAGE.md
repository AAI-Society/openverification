# Coverage index

**13 of 29 threats have a worked use case.** 9 submissions.

Generated from the `threats:` frontmatter across this folder. Do not
edit by hand: run `python3 make_coverage.py`.

## By family

| Family | Covered | |
|---|---|---|
| Instruction and goal manipulation | 0/3 | `░░░░░░░░░░░░░░░░░░░░` |
| Memory, knowledge, and supply chain | 0/4 | `░░░░░░░░░░░░░░░░░░░░` |
| Identity, authority, and inter-agent trust | 3/4 | `███████████████░░░░░` |
| Tools, actions, and effects | 1/4 | `█████░░░░░░░░░░░░░░░` |
| Data exposure | 1/1 | `████████████████████` |
| Autonomy, drift, and lifecycle | 2/3 | `█████████████░░░░░░░` |
| Record integrity and resilience | 3/5 | `████████████░░░░░░░░` |
| Human oversight and disclosure | 2/2 | `████████████████████` |
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
| Memory, knowledge, and supply chain | `model-poisoning` | Training-time data or model poisoning |
| Memory, knowledge, and supply chain | `supply-chain-poisoning` | Poisoned supply chain, tools or MCP |
| Identity, authority, and inter-agent trust | `insecure-inter-agent-comms` | Insecure inter-agent communication |
| Tools, actions, and effects | `unexpected-code-execution` | Unexpected code execution |
| Tools, actions, and effects | `unsafe-actuation` | Unsafe actuation |
| Tools, actions, and effects | `improper-output-handling` | Improper output handling |
| Autonomy, drift, and lifecycle | `behavioral-drift` | Rogue agents or behavioral drift |
| Record integrity and resilience | `cascading-failure` | Cascading failure or fail-open |
| Record integrity and resilience | `coverage-decay` | Coverage decay |
| Output quality and availability | `misinformation` | Misinformation or hallucination |
| Output quality and availability | `hidden-bias` | Hidden bias |

## Every threat

| Family | Threat | Use cases |
|---|---|---|
| Instruction and goal manipulation | `prompt-injection` | — |
| Instruction and goal manipulation | `bent-goals` | — |
| Instruction and goal manipulation | `system-prompt-leakage` | — |
| Memory, knowledge, and supply chain | `memory-poisoning` | — |
| Memory, knowledge, and supply chain | `rag-weakness` | — |
| Memory, knowledge, and supply chain | `model-poisoning` | — |
| Memory, knowledge, and supply chain | `supply-chain-poisoning` | — |
| Identity, authority, and inter-agent trust | `identity-abuse` | `account-takeover-stolen-credentials`, `deepfake-biometric`, `deepfake-interview-insider`, `license-piracy-agent`, `pig-butchering` |
| Identity, authority, and inter-agent trust | `context-blind-authorization` | `agent-exceeds-principal-clearance`, `rogue-internal-agent-pii` |
| Identity, authority, and inter-agent trust | `excessive-agency` | `account-takeover-stolen-credentials`, `agent-exceeds-principal-clearance`, `deepfake-interview-insider`, `rogue-internal-agent-pii`, `shopping-agent` |
| Identity, authority, and inter-agent trust | `insecure-inter-agent-comms` | — |
| Tools, actions, and effects | `tool-misuse` | `license-piracy-agent` |
| Tools, actions, and effects | `unexpected-code-execution` | — |
| Tools, actions, and effects | `unsafe-actuation` | — |
| Tools, actions, and effects | `improper-output-handling` | — |
| Data exposure | `data-exfiltration` | `account-takeover-stolen-credentials`, `agent-exceeds-principal-clearance`, `rogue-internal-agent-pii` |
| Autonomy, drift, and lifecycle | `autonomy-creep` | `shopping-agent` |
| Autonomy, drift, and lifecycle | `behavioral-drift` | — |
| Autonomy, drift, and lifecycle | `scope-creep-lifecycle` | `deepfake-interview-insider` |
| Record integrity and resilience | `audit-tampering` | `rogue-internal-agent-pii` |
| Record integrity and resilience | `cascading-failure` | — |
| Record integrity and resilience | `coverage-decay` | — |
| Record integrity and resilience | `evidence-repudiation` | `deepfake-biometric`, `rogue-internal-agent-pii`, `shopping-agent` |
| Record integrity and resilience | `trust-opacity` | `account-takeover-stolen-credentials`, `deepfake-interview-insider`, `pig-butchering` |
| Human oversight and disclosure | `approval-fatigue` | `deepfake-biometric`, `pig-butchering` |
| Human oversight and disclosure | `undisclosed-ai` | `license-piracy-agent`, `pig-butchering` |
| Output quality and availability | `misinformation` | — |
| Output quality and availability | `hidden-bias` | — |
| Output quality and availability | `unbounded-consumption` | `shopping-agent` |

## Every use case

| Use case | Threats tagged |
|---|---|
| `account-takeover-stolen-credentials` | `identity-abuse`, `excessive-agency`, `data-exfiltration`, `trust-opacity` |
| `agent-exceeds-principal-clearance` | `excessive-agency`, `context-blind-authorization`, `data-exfiltration` |
| `credit-decisioning` | **none tagged** |
| `deepfake-biometric` | `identity-abuse`, `approval-fatigue`, `evidence-repudiation` |
| `deepfake-interview-insider` | `identity-abuse`, `excessive-agency`, `scope-creep-lifecycle`, `trust-opacity` |
| `license-piracy-agent` | `identity-abuse`, `tool-misuse`, `undisclosed-ai` |
| `pig-butchering` | `identity-abuse`, `approval-fatigue`, `undisclosed-ai`, `trust-opacity` |
| `rogue-internal-agent-pii` | `excessive-agency`, `context-blind-authorization`, `data-exfiltration`, `audit-tampering`, `evidence-repudiation` |
| `shopping-agent` | `excessive-agency`, `autonomy-creep`, `unbounded-consumption`, `evidence-repudiation` |
