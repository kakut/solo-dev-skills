---
name: solo-debug
description: "Investigate and fix a reported defect, performance regression, or intermittent failure using observable evidence. Use for errors, wrong results, repeated notifications, or slowness; Chinese: 查故障、排查问题. Preserve uncertainty when reproduction or access is limited."
---

# Solo Debug · 查故障

Explain and repair the user's actual failure with evidence that can disagree with your hypothesis.

## Locate the problem

Read relevant instructions, recent changes and the exact symptom. Separate the user's observation from theories about its cause. For team work read [collaboration](references/collaboration.md); for previous investigations read [continuity](references/continuity.md).

A worker investigates its assigned failure or hypothesis. Distinguish implementation failure, stale inputs and report-delivery failure; a lost report does not justify rebuilding an existing artifact.

## Evidence loop

1. Build the cheapest useful observation: a failing test, request, CLI input, browser interaction, captured event or performance measurement. It must detect the reported symptom, not just prove the program starts.
2. Reduce the scenario while keeping the failure. For intermittent bugs record reproduction frequency and conditions; isolate time, randomness or concurrency where relevant.
3. For non-obvious failures compare plausible causes and each cause's falsifiable prediction. Change one relevant variable at a time. An obvious local defect can take a shorter route.
4. Inspect or instrument the boundary that distinguishes the causes. Record performance baselines before optimization. Keep temporary instrumentation identifiable and redact sensitive values from evidence.
5. Apply the smallest effective fix within scope. When useful, preserve the reproduction as a regression test at an interface that reaches the real failure pattern.
6. Re-run the original scenario and relevant required checks. Remove temporary instrumentation. Explain which evidence supports the cause and repair.

If reproduction is unavailable, continue useful read-only investigation, logs and targeted instrumentation within authorization. Label hypotheses and confidence. Ask only for missing access or evidence that is necessary; never claim verified repair from static plausibility alone.

## Parallel investigations

When delegation is authorized and useful, give investigators different hypotheses and read-only evidence collection. One designated owner integrates overlapping fixes. Compare evidence before broadening changes; respect the task's time/attempt budget and re-plan when repeated failures provide no new information.

## Finish

Report symptom, supported cause or remaining uncertainty, changes, before/after evidence and any regression gap. Save eliminated hypotheses and the next reproducible step when handing off. A real blocker remains a blocker; silence, quota exhaustion and stale worker results do not count as completion.
