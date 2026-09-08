#!/usr/bin/env python3
"""Validate this package's narrow metadata format and local distribution links.

This is not a general YAML parser or a behavioral skill evaluator.
"""
import ast
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAMES = {"solo-ask", "solo-plan", "solo-build", "solo-debug", "solo-review", "solo-memory"}
LINK = re.compile(r"\[[^\]\n]*\]\(([^)\s]+)\)")
PRIVATE = re.compile(r"/(?:Users|home)/[^/\s]+/|[A-Z]:\\Users\\|(?:ghp_|github_pat_)[A-Za-z0-9_]{20,}|-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----")
TOP_FILES = {"README.md", "README.en.md", "LICENSE", "NOTICE.md", "VERSION", "VALIDATION.md", "CONTRIBUTING.md", ".gitignore", "MANIFEST.json"}
TOP_DIRS = {"skills", "shared", "scripts", "tests", "docs", "licenses", ".github"}


def files(root):
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        if any(part in {".git", "__pycache__"} for part in rel.parts):
            continue
        if path.is_symlink():
            raise ValueError(f"Symlink in distribution: {rel}")
        if path.is_file():
            yield path


def validate_skill(skill):
    errors = []
    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    parts = text.split("---\n", 2)
    if len(parts) != 3 or parts[0] != "":
        return [f"{skill.name}: missing frontmatter"]
    fields = dict(line.split(": ", 1) for line in parts[1].splitlines() if ": " in line)
    if fields.get("name") != skill.name:
        errors.append(f"{skill.name}: name mismatch")
    try:
        description = json.loads(fields.get("description", "null"))
        if not isinstance(description, str) or not 20 <= len(description) <= 1024:
            errors.append(f"{skill.name}: invalid description")
    except json.JSONDecodeError:
        errors.append(f"{skill.name}: description must be a quoted JSON/YAML string")
    for path in skill.rglob("*.md"):
        for target in LINK.findall(path.read_text(encoding="utf-8")):
            if "://" in target or target.startswith("#"):
                continue
            resolved = (path.parent / target.split("#")[0]).resolve()
            if not resolved.is_relative_to(skill.resolve()) or not resolved.is_file():
                errors.append(f"{skill.name}: non-self-contained link {target}")
    ui = (skill / "agents" / "openai.yaml").read_text(encoding="utf-8")
    match = re.search(r'^  short_description: (".*")$', ui, re.M)
    if not match or not 25 <= len(json.loads(match[1])) <= 64:
        errors.append(f"{skill.name}: short_description must be 25-64 characters")
    return errors


def validate(root=ROOT):
    errors = []
    if {p.name for p in (root / "skills").iterdir()} != NAMES:
        errors.append("Exactly the six declared skills must be distributed")
    for name in sorted(NAMES):
        try:
            errors.extend(validate_skill(root / "skills" / name))
        except (OSError, ValueError) as exc:
            errors.append(f"{name}: {exc}")
    paths = list(files(root))
    for path in paths:
        rel = path.relative_to(root)
        if (len(rel.parts) == 1 and rel.name not in TOP_FILES) or (len(rel.parts) > 1 and rel.parts[0] not in TOP_DIRS):
            errors.append(f"Unexpected publication path: {rel}")
        if path.suffix not in {".md", ".py", ".json", ".yaml", ".yml", ".txt"} and path.name not in TOP_FILES:
            errors.append(f"Unexpected file type: {rel}")
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"Not UTF-8 text: {rel}")
            continue
        if PRIVATE.search(text):
            errors.append(f"Potential private material: {rel}")
        if path.suffix == ".py":
            ast.parse(text, filename=str(rel))
        elif path.suffix == ".json":
            json.loads(text)
        elif path.suffix == ".md":
            for target in LINK.findall(text):
                if "://" in target or target.startswith("#"):
                    continue
                resolved = (path.parent / target.split("#")[0]).resolve()
                if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                    errors.append(f"Broken local link in {rel}: {target}")
    for source in (root / "shared").glob("*.md"):
        for name in NAMES:
            target = root / "skills" / name / "references" / source.name
            if not target.exists() or target.read_bytes() != source.read_bytes():
                errors.append(f"Shared reference drift: {name}/{source.name}")
    manifest = root / "MANIFEST.json"
    if manifest.exists():
        declared = json.loads(manifest.read_text())
        actual = [p.relative_to(root).as_posix() for p in paths]
        if declared != actual:
            errors.append("MANIFEST.json differs from actual publication files")
    else:
        errors.append("Missing publication manifest")
    return errors


if __name__ == "__main__":
    problems = validate()
    print("\n".join(problems) if problems else "PASS: six self-contained skills, metadata, local links, shared references and publication manifest.")
    raise SystemExit(bool(problems))
