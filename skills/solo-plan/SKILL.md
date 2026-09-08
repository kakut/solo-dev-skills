---
name: solo-plan
description: "Convert an understood goal into a practical implementation plan with verifiable slices, dependencies, and ownership. Use for feature planning or organizing work across agents; Chinese: 拆计划、拆任务. Do not restart requirement interviews already resolved."
---

# Solo Plan · 拆计划

Make the next piece executable while keeping later decisions adaptable.

## Establish the baseline

Read the goal, acceptance, relevant code and existing plan. Reuse project conventions and the authoritative tracker. If essential product decisions are missing, resolve only those gaps; a full new interview is unnecessary.

Read [collaboration](references/collaboration.md) for delegated or parallel work and [continuity](references/continuity.md) for an existing memory or cross-session plan. A worker plans its assigned scope; an existing graph or coordinator remains authoritative.

## Shape the work

1. Identify existing behavior and reusable interfaces. Investigate unknowns that could invalidate the approach before committing dependent work.
2. For significant alternatives, explain the current requirement each serves and its maintenance cost. Prefer a simpler design that meets the actual need; avoid speculative extension points.
3. Create narrow end-to-end slices. Each delivers an independently demonstrable or verifiable behavior across the necessary layers. Obtain an early complete path before expanding coverage.
4. For every slice state its goal, acceptance, input version, output, dependencies and owner when assigned. A task must fit a fresh agent's context with bounded references, not a full transcript.
5. Distinguish a dependency on an accepted interface from a dependency on an integrated implementation. Parallel work can start against an agreed contract; guesses about an unresolved interface do not satisfy it.
6. For broad mechanical migrations, use compatible expansion, bounded migration batches and final removal. If intermediate changes cannot pass independently, state the integration boundary and verification point explicitly.

## Choose organization separately

Use one owner for tightly coupled changes. Reuse a suitable worker before starting another. Parallelize only when the independent result or isolated review is worth briefing and integration costs. Existing role definitions do not imply every role must be running.

Specify owned files or interfaces and an integration owner. Worktrees isolate edits but still need accessible inputs, conflict resolution and integrated verification. Follow actual host capabilities and existing authorization; a plan is not permission to create independent tasks.

Preserve configured models. Do not equate production requirements with more agents or stronger reasoning settings. Respect supplied time, cost and concurrency limits.

## Deliver

Use a short in-chat plan for small work; persist a plan/task graph when dependencies or handoff justify it. Do not mirror an existing tracker into a competing status system. Leave downstream uncertainty visible instead of inventing detailed future tasks.

The plan is ready when the first task can start, its inputs are available, success is observable and dependencies are honest. Return the next action and only material decisions needing the user. Continue already-authorized implementation when appropriate; otherwise finish the planning request. Skills are optional helpers, not mandatory phases.
