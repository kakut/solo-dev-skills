# Solo Dev Skills

**Six skills for an individual developer: clarify, plan, build, debug, review, and resume.**

[简体中文](README.md) · [Validation status](VALIDATION.md) · [MIT](LICENSE)

Experimental release `0.1.0-alpha.1`. Packaging checks are provided; real-project effectiveness, live multi-agent coordination and long-term recovery have not been validated. No token savings or automatic wake-up guarantees.

| Skill | Purpose |
| --- | --- |
| [solo-ask](skills/solo-ask/SKILL.md) | Ask consequential questions until the current delivery is clear |
| [solo-plan](skills/solo-plan/SKILL.md) | Plan verifiable slices, actual dependencies and ownership |
| [solo-build](skills/solo-build/SKILL.md) | Implement agreed behavior and produce relevant evidence |
| [solo-debug](skills/solo-debug/SKILL.md) | Investigate the real symptom, fix it and verify the original case |
| [solo-review](skills/solo-review/SKILL.md) | Review requirements, correctness and maintenance risks |
| [solo-memory](skills/solo-memory/SKILL.md) | Save, resume and reconcile project context across sessions |

## Install

Clone `https://github.com/kakut/solo-dev-skills.git` or download the repository. Copy any complete directory under `skills/` into your host's supported skill location. Each skill includes its references and needs no sibling skill.

For Codex, use project-local `<project>/.agents/skills/` or user-level `~/.agents/skills/`, following the [official skill documentation](https://learn.chatgpt.com/docs/build-skills). Compare existing installations before replacing them. Start a fresh session and verify discovery. Other hosts need their own supported paths and invocation syntax; cross-host behavior is not yet tested.

The skills are Markdown instructions, not an API service, scheduler or model configuration. They require no additional runtime dependency; maintenance scripts use Python 3.10+ and its standard library.

## Use

```text
Use $solo-ask to clarify the smallest useful subscription feature.
Use $solo-plan to turn this agreement into independently verifiable tasks.
Use $solo-build to implement the first task and run the relevant checks.
Use $solo-debug to investigate duplicate notifications.
Use $solo-review to check the current diff against its requirements.
Use $solo-memory to save progress, including uncommitted work and next steps.
Use $solo-memory to resume this project and continue authorized work.
```

Memory's save/resume/reconcile are natural-language operations, not executable CLI commands. Small clear work can start directly with build; bugs with debug; existing changes with review. No mandatory six-phase pipeline.

## Teams and continuity

Skills and roles are separate. Reuse the project's coordinator or graph. Workers receive task/attempt IDs, accepted inputs, write boundaries, acceptance conditions and a verified reporting destination. Late reports do not supersede active attempts. Report receipt, artifact acceptance and integration are separate facts.

Delivery assurance, team size and model settings are chosen independently. Native subagents and independent app tasks use different host operations. The workflow supports these concepts but does not implement a messaging runtime or promise unavailable capabilities.

Reuse existing project records. When persistence is needed, maintain a short state, consequential decisions and incremental task checkpoints. Workers write separate checkpoints; one writer reconciles shared state. Separate portable project facts from private runtime bindings and verify reality on resume. The skill cannot access every conversation, intercept compaction or recover never-saved decisions.

## Maintain

Run `python3 scripts/sync_references.py --check`, `python3 scripts/validate.py`, and `python3 -m unittest discover -s tests -v`. Shared references are maintained under `shared/`; run the sync script without `--check` to refresh bundled copies. See [evaluation procedure](tests/behavioral-evaluation.md) for unexecuted behavioral scenarios.

See [NOTICE](NOTICE.md) for inspiration from Matt Pocock's skills and Codex Commander, retained licenses and design differences. This is an independent community project.
