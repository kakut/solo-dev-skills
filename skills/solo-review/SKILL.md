---
name: solo-review
description: "Review a change or deliverable against requirements, correctness risks, and maintainability, with version-specific evidence. Use for PRs, branches, working changes, or accepting an agent result; Chinese: 验成果、审查改动. Review is read-only unless fixes are requested."
---

# Solo Review · 验成果

Determine whether the actual deliverable meets its agreement and identify consequential defects.

## Establish scope and evidence

Read the requested comparison, originating requirements and relevant project rules. For team acceptance read [collaboration](references/collaboration.md); for recorded decisions read [continuity](references/continuity.md).

Resolve the exact target and baseline. Include staged/unstaged work when the user asked to review it; a HEAD-only diff misses uncommitted changes. Record the commit or an equivalent artifact snapshot. If comparison is ambiguous, clarify before reporting broad conclusions. An empty diff has no reviewed changes.

Locate the spec from the supplied reference or project context. If unavailable, review correctness and conventions while explicitly limiting requirements coverage; do not manufacture a spec from the implementation.

## Review three dimensions

1. **Requirements:** missing/partial behavior, incorrect interpretation, unrequested scope. Compare concrete acceptance criteria to actual code or output.
2. **Correctness and risk:** triggering conditions, error paths, state consistency, regressions and data effects. Investigate enough surrounding code to substantiate a finding. Run useful checks when feasible; otherwise label the gap.
3. **Maintainability:** complexity introduced for the current need, interface clarity and project conventions. Treat style preferences and code smells as judgments, not proven defects. Leave tool-enforced formatting to tools.

Inspect the delivered interface or visual artifact when appearance is part of acceptance. Worker descriptions and passing unit tests cannot prove visual quality or integration behavior.

When independent reviewers are authorized and useful, give each the raw requirements and exact artifact, not an expected verdict. Keep dimensions identifiable when consolidating, but remove duplicates and unsupported claims. No mandatory team or fixed role roster.

## Report and accept

For each actionable finding state impact, trigger, location and evidence; suggest the smallest relevant correction. Lead with material risks. Distinguish verified defects from hypotheses and subjective recommendations. If no actionable findings exist, say so with the scope and unperformed checks; do not invent findings to fill a template.

A review result is separate from an acceptance decision. Only mark a task accepted if authorized and its declared criteria are met, recording task/attempt, input version, reviewed artifact and evidence. Integration may still remain. Changed artifacts or upstream contracts require re-evaluating affected acceptance.

Review stays read-only unless the user requested fixes. If fixes are authorized, implement and recheck affected behavior without changing the original acceptance criteria to make the result pass. Save a concise review checkpoint when project memory is enabled.
