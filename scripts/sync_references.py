#!/usr/bin/env python3
"""Bundle shared instructions for independently installable skills."""
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def sync(root=ROOT, check=False):
    changed = []
    for skill in sorted((root / "skills").iterdir()):
        if not skill.is_dir() or skill.is_symlink():
            raise ValueError(f"Unexpected skill entry: {skill.name}")
        for source in sorted((root / "shared").glob("*.md")):
            target = skill / "references" / source.name
            if source.is_symlink() or target.is_symlink() or target.parent.is_symlink():
                raise ValueError("Reference paths must be regular files/directories")
            content = source.read_bytes()
            if not target.exists() or target.read_bytes() != content:
                changed.append(target.relative_to(root).as_posix())
                if not check:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(content)
    return changed


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    changes = sync(check=args.check)
    print("\n".join(changes) if changes else "Shared references are synchronized.")
    raise SystemExit(1 if args.check and changes else 0)
