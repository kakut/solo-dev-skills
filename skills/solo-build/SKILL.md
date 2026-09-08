---
name: solo-build
description: "Implement a clear feature or approved task and verify the resulting behavior. Use for code changes, UI implementation, and bounded worker assignments; Chinese: 做实现、开发功能. Diagnose unexplained failures with a focused evidence loop."
---

# Solo Build · 做实现

Deliver the requested behavior with evidence appropriate to the change.

## Start from the agreement

Inspect project instructions, current code, working-tree changes and the supplied task/spec. For team work read [collaboration](references/collaboration.md); for memory or handoff read [continuity](references/continuity.md).

A clear small change needs no new specification. For material ambiguities ask a focused question with a recommendation. Continue local implementation decisions already within scope. As a worker, preserve the task ID, active attempt, input version and assigned modification boundary.

## Implement and check

1. Select a narrow behavior and the interface through which it can be observed. Follow existing architecture and naming; keep unrelated changes intact.
2. For business rules, state changes or regressions, prefer a test that fails on the missing behavior before implementation. Expected outcomes come from requirements or independent worked examples, not a copy of the implementation.
3. Implement enough to deliver that behavior. Refactor locally when it improves the current change while preserving behavior and scope.
4. Run relevant checks as the slice becomes available. Use the project's required validation before completion. For low-impact text/style edits choose direct or visual inspection instead of ceremonial tests.
5. Test through useful public interfaces. Avoid tests coupled to private calls, or mocks that bypass the behavior being claimed. Check real visual output when appearance is part of acceptance.
6. Keep progress and unfinished work distinguishable. A passing local test is evidence for that tested scope, not proof of a deployed or integrated feature.

If a shared interface or upstream assumption must change, report the effect and coordinate a revised contract. Handle ordinary local failures autonomously. Surface real access, scope or product-decision blockers without inventing success.

## Complete the assignment

Inspect the final diff for scope, obvious correctness issues and missed requirements. Use independent review when requested or warranted and available; do not spawn agents merely because this skill exists. A separate reviewer can use solo-review, but installation is not required.

Report delivered behavior, artifact location/version, checks actually performed, unverified areas and remaining work. Save a checkpoint when project memory is enabled or a handoff is needed. Team workers send the required report to the verified destination and then finish their assignment; local final text alone does not prove delivery.

The user/coordinator owns acceptance according to the assignment. Integrating, committing, pushing and publishing are distinct actions: honor existing authorization and host constraints instead of assuming any of them from the skill name. If full implementation is authorized, persist through the appropriate checks and handoff.
