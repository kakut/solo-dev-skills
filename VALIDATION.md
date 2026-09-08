# Validation status

Release: `0.1.0-alpha.1`. This is an experimental, instruction-first release.

## Release checks

The package provides a Python standard-library validator and distribution tests. The validator checks the six entrypoints, this package's narrow frontmatter format, UI description length, local Markdown links, bundled references and an explicit publication manifest. It also flags a small set of private-path/credential patterns; that is not a comprehensive secret scanner.

Distribution tests exercise copying each skill without siblings, missing-reference rejection, sibling-reference rejection, read-only drift checks, repeatable reference synchronization, refusal of symlink write targets and the publication manifest.

Run:

```bash
python3 scripts/sync_references.py --check
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Observed locally before publication on 2026-09-09 (macOS, Python 3.13):

| Check | Observed result |
| --- | --- |
| Shared-reference synchronization check | Passed |
| Package validator | Passed; 44 declared publication files |
| Distribution unittest suite | 6 tests passed, including all 6 isolated skill copies |
| Bundled skill-creator quick_validate.py | All 6 skills passed; PyYAML 6.0.3 supplied only to the local validation environment |

The first private-path check matched its own regex source. The pattern was corrected without excluding scanner files; the complete package check and distribution suite then passed. No agent behavior pass is inferred from these results.

CI repeats the structural/distribution checks; it does not run an agent or contact an external service beyond normal checkout/setup. The external skill-creator validator is not bundled or required at runtime.

## Not established

- Effectiveness in real development projects or comparative token/time savings.
- Successful execution of the 12 behavioral scenarios by independent agents.
- Live native-subagent or independent-task creation, reporting, acceptance and resumption.
- Automatic recovery after app shutdown, quota exhaustion or compaction.
- Exactly-once delivery, a scheduler, concurrent shared-state transactions or distributed locks.
- Automatic access to all project conversations, or restoration of never-saved information.
- Cross-host, cross-OS and long-term memory behavior.

Memory in this release is a file protocol executed by the host agent. There is no runtime memory database or record-writing helper. Maintenance scripts only synchronize packaged references and validate the distribution.

See [behavioral evaluation](tests/behavioral-evaluation.md) before making behavior claims. MIT licensing and open publication are not production-readiness certifications.
