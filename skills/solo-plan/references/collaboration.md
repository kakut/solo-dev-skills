# Collaboration contract · solo-dev/v1

Read only when working as a delegated agent, coordinating workers or accepting team results. This file is bundled with each skill so single-skill installs remain usable. The maintained source is shared/collaboration.md in the repository; regenerate bundled copies with scripts/sync_references.py.

## Authority and role

The user's instructions and the host's actual permissions govern actions. Preserve project-specific rules. A task/skill mention does not authorize publishing, changing global configuration, unlimited recruitment or unrelated work. Carry forward existing explicit authorization; avoid repeated approvals for ordinary in-scope steps.

Use the existing coordinator or graph when present. A worker executes its bounded assignment, resolves local implementation details and reports material gaps. It does not re-interview the entire project, rewrite global decisions or recruit workers unless assigned that authority. Independent skills are reusable methods, not a roster of agents.

Preserve the user's conversation and per-document language, including Simplified/Traditional Chinese. Keep canonical identifiers and license text unchanged. Pass language choices to workers.

## Capability adapter

Discover real operations for task creation, messaging, inspection, waiting, artifacts and cancellation. Keep native subagents and independent app tasks distinct. Use the explicitly requested mechanism; do not silently substitute another. Pending setup identifiers are not necessarily usable message destinations.

Separate saved-project membership, execution workspace and UI grouping. Resolve all relevant bindings using trusted tool results. A task title or remembered ID is not identity proof. A new worktree may not contain uncommitted input files. Confirm inputs are actually accessible before dispatch. Do not rearrange the sidebar just to form a team.

No available scheduling tools means no promised automatic continuation. Use documented event/wait behavior; otherwise bounded status checks with backoff or a manual resume. An instruction file is not a timer, transport, process supervisor or lock service.

## Assignment

For each independently managed task keep:

| Field | Meaning |
| --- | --- |
| task_id / attempt | Stable project task identity and current execution generation |
| goal / scope | Requested outcome and meaningful non-goals |
| input_revision / inputs | Accepted contract or artifact version, with readable locations |
| owner / workspace | Verified responsible worker and actual execution location |
| write_scope | Owned files/interfaces; other inputs are read-only unless agreed |
| dependencies | What evidence releases the task: interface accepted, output integrated, etc. |
| acceptance / output | Observable success and expected accessible deliverable |
| constraints | Applicable language, budget, authorization and relevant operational limits |
| report_destination | Verified coordinator destination using the chosen host mechanism |

Keep private host/thread identifiers and machine paths only in untracked local bindings. Portable tasks use project-local IDs and relative references. Verify local state is untracked before storing bindings; an ignore pattern alone does not untrack a file.

Increment attempt when deliberately reissuing a blocked/rejected task or changing its contract/owner in a way that supersedes the old execution. Resuming the same still-valid attempt does not require a new number. Record the replacement, confirm the previous writer has stopped or isolate it, and only then transfer overlapping write ownership.

## Ownership and dependencies

Keep overlapping edits with one owner. Use isolated workspaces for independent implementations when supported; name an integration owner. Shared interfaces, dependency manifests and migrations require explicit ownership. Verify all input versions. Downstream work may proceed against an accepted interface when its task allows it; otherwise wait for the actual required artifact.

When a contract changes, update the authoritative record and notify affected active workers. Their relevant outputs and acceptance become subject to revalidation; updating a file does not prove running agents reloaded it. Concurrency is bounded by the host, user constraints and integration cost.

## Reporting, transport and acceptance

A report contains task_id, attempt, input_revision, status, artifact location/version, checks actually run, limitations and needed decisions. Preserve the report/checkpoint before transmission when recovery matters. Send terminal completion/blocker reports through the agreed mechanism; local final text alone does not prove cross-task delivery.

Track task state separately from delivery evidence:
- Task: planned, working, blocked, ready_for_review, ready_to_integrate, done; cancelled and superseded are distinct terminal outcomes.
- Message: uncertain, delivered when observed, report_received. A send timeout is not proof of non-delivery.
- Acceptance: separate version-bound decision by the assigned authority, with checks and any remaining integration requirement.

Only the active task/attempt, expected sender and matching inputs may advance current state. Duplicates/late reports are history, not triggers for duplicate work. An accepted research artifact can finish a research task; a code task finishes only after its agreed integration/verification. Publishing remains subject to the user's scope and host policy.

Inspect the actual artifact, including visual output where relevant, before acceptance. A passing report cannot substitute for evidence. The same coordinator may inspect and accept small work; separate agents are optional. Recheck evidence affected by later changes.

## Uncertainty and recovery

On an uncertain creation/send result, inspect narrowly before retrying. Retry only a known-undelivered operation within scope; otherwise retain delivery uncertainty. Stable IDs help application-level deduplication but do not provide exactly-once transport.

A quiet, disconnected or quota-limited worker is not finished. Verify its state and artifacts; do not recreate it blindly. Avoid acknowledgement loops: send another message for changed work, a real question or a stop instruction, not merely to thank another agent.

Respect meaningful retry/time budgets. If repeated attempts add no evidence, preserve a checkpoint and surface the real blocker or re-plan. Never infer approval from silence. On restart verify project, active attempt, worker state and latest accepted artifacts before proceeding.
