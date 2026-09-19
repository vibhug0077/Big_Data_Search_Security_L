<div class="hero session-hero">
<div class="cell-kicker">CSBD4011P - Chapter 05 lab - CO1</div>
<h1>Threat and risk</h1>
<p>Build an asset and trust-boundary inventory, calculate transparent ordinal risk priorities, and detect a repeated-denial review signal using deterministic teaching data.</p>
<div class="meta-row"><span class="meta-pill">Local Python</span><span class="meta-pill">Deterministic JSON</span><span class="meta-pill">Docker-tested</span></div>
</div>

{{< include ../../docs/execution_context.md >}}

<figure class="chapter-image-infographic">
<img src="../../assets/infographics/chapter_05_threat_and_risk_infographic.png" alt="Threat and risk workflow from assets and boundaries through threat scenarios, likelihood, impact, and treatment">
<figcaption><strong>Chapter 5 visual guide:</strong> identify assets and boundaries, state the threat scenario, record likelihood and impact assumptions, then request evidence before changing residual risk.</figcaption>
</figure>

## Alignment and theory link

**Theory chapter:** Available in the [private theory repository](https://github.com/vibhug0077/Big_Data_Search_Security) for enrolled students and instructors.  
**Course outcome:** CO1 - discuss big data search and analyse problems related to Elasticsearch.  
**Lab purpose:** turn the theory demonstrations into reviewable outputs without pretending that a risk score is a measured probability or that a model is a deployed control.

The theory, code, data, and execution evidence are maintained together in this canonical repository.

## Prerequisites

- Read Chapter 5 in the theory book.
- Docker Desktop and `docker compose` must be available.
- No external scanner, network target, Kafka service, or Kerberos realm is contacted.
- The JSON file is deterministic teaching data created from the chapter's supplied examples so that every learner receives the same result.

## Working directory and files

Host working directory:

```text
C:\UPES\Repos\Big_Data_Search_Security_L
```

Container working directory:

```text
/workspace/labs/chapter_05_threat_and_risk
```

| Role | File | Used by |
|---|---|---|
| Deterministic teaching data | [`data/threat_risk_data.json`](data/threat_risk_data.json) | Inventory, risk register, and denial events |
| Runnable code | [`code/threat_risk_examples.py`](code/threat_risk_examples.py) | Three local security/risk examples |
| Readable output | [`outputs/threat_risk_output.txt`](outputs/threat_risk_output.txt) | Result comparison |
| Raw terminal capture | [`outputs/threat_risk_terminal.txt`](outputs/threat_risk_terminal.txt) | Command, container, output, and exit status |

## Code examples

1. Inventory assets, owners, and trust boundaries.
2. Calculate likelihood multiplied by impact as an ordinal priority while retaining the rating note.
3. Count deterministic denial events and return correlation IDs for review.

The script also prints the evidence classification required for publication. A risk priority is not a security control. The denial pattern is a review signal, not a conclusion that Alice is malicious.

## Execution command

PowerShell from the public code root:

```powershell
docker compose -f docker/course-dev/docker-compose.yml run --rm course-dev `
  bash -lc "cd /workspace/labs/chapter_05_threat_and_risk && python3 code/threat_risk_examples.py"
```

Bash from the public code root:

```bash
docker compose -f docker/course-dev/docker-compose.yml run --rm course-dev \
  bash -lc 'cd /workspace/labs/chapter_05_threat_and_risk && python3 code/threat_risk_examples.py'
```

## Captured output

<div class="execution-status"><strong>Execution status: Docker-tested.</strong> The dependency-free script was executed in the `course-dev` container using the committed deterministic JSON file.</div>

{{< include outputs/threat_risk_output_render.qmd >}}

## Security evidence classification

| Classification | Chapter 5 result | Evidence boundary |
|---|---|---|
| Configured control | Risk-treatment suggestions are recorded in the model | This is a data record, not deployed configuration |
| Tested control | Repeated-denial review signal | Fixed events, threshold, and correlation IDs are asserted by the script |
| Failed control | No control-effectiveness failure is exercised here | The risk-only script must not be read as a passed or failed production control |
| Untested control | Resource-specific role, payload limit, restore rehearsal | No service, storage, or recovery system is contacted |
| Residual risk | Live enforcement, alert timing, audit-store integrity, and recovery | Requires platform-specific tests and operational evidence |

## Interpretation

- The inventory makes owners and boundaries visible; it does not prove that the owners enforce anything.
- The priorities are ordinal comparisons. A score of 20 is not a probability and is not twice a score of 10.
- The repeated-denial output identifies `alice` and evidence IDs `c1`, `c2`, and `c3` for review. It does not establish intent or compromise.
- No residual-risk rating is reduced merely because a Python calculation ran.

## Limitations and untested scope

- No vulnerability scanner, external host, Kafka broker, Kerberos KDC, Elasticsearch authorization layer, or backup is tested.
- The data is fictional and deterministic; it is not student data or an incident record.
- The risk matrix does not model dependency, frequency, monetary loss, or calibrated probability.
- The local denial detector has no time window, baseline, identity assurance, alert delivery, or case-management integration.

## Troubleshooting and viva prompts

| Symptom | Check first | Safe response |
|---|---|---|
| Data file not found | `/workspace/labs/chapter_05_threat_and_risk` | Run the exact container command from the public root. |
| Priority order differs | JSON file and integer likelihood/impact fields | Restore the supplied deterministic file; do not change the expected order. |
| Review signal is treated as an accusation | Interpretation and evidence IDs | Explain why a detector output requires investigation and context. |

1. Why is a trust boundary more informative than saying that a cluster is secure?
2. Why is likelihood multiplied by impact an ordinal prioritization tool?
3. What additional evidence would be required before lowering residual risk for R1?

## Bloom's taxonomy assessment questions

| Bloom level | Marks | Question | CO |
|---|---:|---|---|
| Understand | 5 | Define asset, threat, vulnerability, likelihood, impact, control, and residual risk using one row from the supplied JSON. | CO1 |
| Apply | 5 | Calculate the priority for R1, R2, and R3 and reproduce the sorted order. State the assumptions used. | CO1 |
| Analyse | 5 | Analyse the four denial events and explain why the output is a review signal rather than proof of malicious activity. | CO1 |
| Analyse/Evaluate | 15 | Evaluate the inventory for missing boundaries. Add two components or paths and justify the owner, affected asset, and evidence needed for each. | CO1 |
| Evaluate | 15 | Evaluate whether the risk score for the restricted index should be reduced after the repeated-denial detector passes. Distinguish evidence about detection from evidence about prevention. | CO1 |
| Create | 20 | Design a testable risk-assessment workflow for a distributed search platform. Specify assets, trust boundaries, scenario statements, rating assumptions, control owners, evidence, review dates, residual risk, and failure handling. | CO1 |
