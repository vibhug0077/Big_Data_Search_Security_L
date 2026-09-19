<div class="hero session-hero">
<div class="cell-kicker">CSBD4011P - Chapter 06 lab - CO1</div>
<h1>Controls and audit</h1>
<p>Review control-evidence coverage, normalize audit events without retaining sensitive bodies, test authorization decisions, and preserve an intentionally failed control as evidence.</p>
<div class="meta-row"><span class="meta-pill">Local Python</span><span class="meta-pill">Audit JSON</span><span class="meta-pill">Docker-tested</span></div>
</div>

{{< include ../../docs/execution_context.md >}}

<figure class="chapter-image-infographic">
<img src="../../assets/infographics/chapter_06_controls_and_audit_infographic.png" alt="Controls and audit workflow from threat and control selection through testing, audit evidence, and residual risk review">
<figcaption><strong>Chapter 6 visual guide:</strong> a control must have a purpose, owner, test, evidence, failure handling, and a residual-risk decision.</figcaption>
</figure>

## Alignment and theory link

**Theory chapter:** Available in the [private theory repository](https://github.com/vibhug0077/Big_Data_Search_Security) for enrolled students and instructors.  
**Course outcome:** CO1 - discuss big data search and analyse problems related to Elasticsearch.  
**Lab purpose:** make control lifecycle states and audit evidence explicit without turning a local policy unit test into a claim about every service path.

The theory, code, data, and execution evidence are maintained together in this canonical repository.

## Prerequisites

- Read Chapter 6 in the theory book.
- Docker Desktop and `docker compose` must be available.
- No live Kafka, Kerberos, TLS endpoint, backup, or distributed authorization service is contacted.
- The JSON file is deterministic teaching data derived from the supplied control matrix, audit-event, and policy examples.

## Working directory and files

Host working directory:

```text
C:\UPES\Repos\Big_Data_Search_Security_L
```

Container working directory:

```text
/workspace/labs/chapter_06_controls_and_audit
```

| Role | File | Used by |
|---|---|---|
| Deterministic teaching data | [`data/controls_audit_data.json`](data/controls_audit_data.json) | Control matrix, audit events, and policy cases |
| Runnable code | [`code/controls_audit_examples.py`](code/controls_audit_examples.py) | Four local controls/audit examples |
| Readable output | [`outputs/controls_audit_output.txt`](outputs/controls_audit_output.txt) | Result comparison |
| Raw terminal capture | [`outputs/controls_audit_terminal.txt`](outputs/controls_audit_terminal.txt) | Command, container, output, and exit status |

## Code examples

1. Compare control-matrix evidence references with controls actually tested by this local script.
2. Normalize audit events to a safe allow-list and prove that the sensitive `body` field is omitted.
3. Execute positive and negative authorization tests against a deterministic policy.
4. Run an intentionally insecure policy variant and preserve the detected failure rather than hiding it.

The `FAILED CONTROL DETECTED` line is an expected teaching result: the insecure variant is supposed to violate the negative test, and the script proves that the test detects the violation. The final smoke marker means the detector worked; it does not mean the insecure variant was secure.

## Execution command

PowerShell from the public code root:

```powershell
docker compose -f docker/course-dev/docker-compose.yml run --rm course-dev `
  bash -lc "cd /workspace/labs/chapter_06_controls_and_audit && python3 code/controls_audit_examples.py"
```

Bash from the public code root:

```bash
docker compose -f docker/course-dev/docker-compose.yml run --rm course-dev \
  bash -lc 'cd /workspace/labs/chapter_06_controls_and_audit && python3 code/controls_audit_examples.py'
```

## Captured output

<div class="execution-status"><strong>Execution status: Docker-tested.</strong> The dependency-free controls and audit script was executed in the `course-dev` container using the committed deterministic JSON file.</div>

{{< include outputs/controls_audit_output_render.qmd >}}

## Security evidence classification

| Classification | Chapter 6 result | Evidence boundary |
|---|---|---|
| Configured control | Policy, audit-field allow-list, and matrix records exist in the fixture | Configuration exists only in the local teaching program |
| Tested control | Safe audit normalization and secure policy positive/negative cases | Assertions run in the container and are recorded in output |
| Failed control | Insecure policy variant allows `reader SELECT private_notes` | Failure is intentional and detected; it is not suppressed |
| Untested control | Payload limit, restore rehearsal, TLS/certificate validation, distributed enforcement | No corresponding service or recovery environment is available |
| Residual risk | Gateway/search/export/backup/direct-storage paths and audit-store integrity | Requires end-to-end platform tests and operational review |

## Interpretation

- A control matrix row with an evidence reference is not automatically a proof that the control was executed in this run; the local assertions are the evidence for the examples shown here.
- Audit normalization demonstrates field minimization. It does not protect the audit store, prove clock accuracy, or establish log completeness.
- The secure policy cases pass, and the intentionally insecure variant is caught by a negative test.
- A failed control must remain visible so that corrective action and residual risk can be discussed.

## Limitations and untested scope

- No credentials, secrets, sensitive documents, or live audit store are used.
- The policy is a set-membership model, not an Elasticsearch, SQL, Hadoop, Kafka, or Kerberos enforcement point.
- No TLS handshake, certificate validation, backup restore, payload limit, network binding, or distributed identity propagation is tested.
- The output does not claim compliance, security certification, or production readiness.

## Troubleshooting and viva prompts

| Symptom | Check first | Safe response |
|---|---|---|
| `FAILED CONTROL DETECTED` appears | The explanation above the output | This is an expected preserved failure of the insecure fixture; the detector must catch it. |
| Sensitive `body` appears in safe events | `safe_event_fields` in the JSON file | Restore the allow-list and rerun; do not log the body. |
| A matrix row is called tested automatically | Evidence classification table | Distinguish a fixture reference from an executed test. |

1. Why is a log record not proof that the event really happened?
2. Why must a negative authorization test be included?
3. Which residual risks remain after the local policy tests pass?

## Bloom's taxonomy assessment questions

| Bloom level | Marks | Question | CO |
|---|---:|---|---|
| Understand | 5 | Distinguish configured, tested, failed, untested, and residual-risk states using the supplied control matrix. | CO1 |
| Apply | 5 | Apply the audit-field allow-list to both supplied events and show which fields are retained and which field is omitted. | CO1 |
| Analyse | 5 | Analyse the secure policy results and the intentionally insecure policy result. Explain why the final smoke marker can still be a pass. | CO1 |
| Analyse/Evaluate | 15 | Evaluate the audit events for reconstruction quality. Identify missing fields, sensitive fields that must not be logged, and evidence needed to protect the audit path. | CO1 |
| Evaluate | 15 | Evaluate the claim that the policy tests prove end-to-end authorization. Identify at least four untested enforcement paths and propose evidence for each. | CO1 |
| Create | 20 | Design a threat-to-control evidence matrix for a distributed search service. Include control type, owner, enforcement point, positive and negative tests, audit schema, failed-control handling, review date, and residual risk. | CO1 |
