---
name: solo-ask
description: "Turn a vague idea into a bounded, testable agreement. Use for requirement discovery, pressure-testing a proposal, or consequential product tradeoffs; Chinese: 问清楚、理清需求. A clear implementation request can proceed without another interview."
---

# Solo Ask · 问清楚

Reach enough shared understanding to take the next authorized step.

## Orient

Read the user's actual request, relevant project instructions and existing decisions. Inspect the relevant implementation when it can answer a factual question. Distinguish a proposal for future behavior from a claim about current behavior.

For a team assignment, read [collaboration](references/collaboration.md). A worker clarifies only gaps in its assigned task; the existing coordinator owns project-wide decisions. Use [continuity](references/continuity.md) when project memory exists or a handoff is needed.

## Ask what changes the outcome

1. Establish the user's problem, intended audience, essential behavior and observable success. Reuse answers already present.
2. Find unresolved decisions that materially change the current scope, cost, behavior or failure consequences. Look up environmental facts instead of asking the user to do the research.
3. Ask the most consequential questions first. Default to one to three questions per round, each with a concise recommendation and meaningful tradeoff. Ask dependent questions after their prerequisites are settled.
4. Separate confirmed facts, adopted decisions and reversible assumptions. Explain significant uncertainty. Use reasonable defaults for low-impact details within existing authorization.
5. When discussion stalls on appearance or behavior, propose a minimal prototype that answers that specific question; create it when within scope. Research unknown facts with the tools available. Neither activity automatically authorizes implementation of the product.

Translate engineering depth into concrete promises: an experiment needs one useful verified path; a tool for repeated use needs appropriate regression coverage and failure handling; a service others rely on needs the operational commitments its use actually requires. Team size and model choice are separate decisions. Simplicity cannot erase necessary data protection; higher assurance cannot add unrelated features.

## Finish

Stop when the current goal, scope, acceptance conditions and material decisions are sufficient for the next authorized step. Deferred features remain deferred. Let the user end the interview; label consequential unresolved choices rather than silently settling them.

Return a short agreement: problem, intended behavior, scope, acceptance, important decisions/assumptions and the next step. Use the user's language, preserving explicit per-artifact language choices. A small request can need zero questions and no new document.

If the user asked only for discussion, stop with the agreement. If they already authorized implementation and no material decision is outstanding, continue without another phase-transition approval. Other Solo skills are optional; this skill does not require their installation.
