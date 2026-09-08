# Contributing

Improve a demonstrated decision or workflow failure. Provide the scenario, expected behavior, actual behavior, host capability limits and the relevant skill version. Remove private transcripts, runtime identifiers and credentials from examples.

Keep six focused entrypoints and independently installable skill folders. Edit shared/collaboration.md or shared/continuity.md once, then run scripts/sync_references.py. Preserve English and Chinese README meaning. Prefer a small targeted rule over accumulated blanket prohibitions.

Run the package validator, reference check and unittest suite. Behavioral cases need fresh agent context containing the skill and raw scenario, without the expected answer. Real host coordination requires a separately scoped live test; simulated decisions do not establish message delivery or recovery. Report untested capabilities clearly in VALIDATION.md.
