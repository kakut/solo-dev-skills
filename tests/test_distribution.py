"""Exercise single-skill distribution and failures that can break publication."""
import importlib.util
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


validator = load("validate")
syncer = load("sync_references")


class DistributionTests(unittest.TestCase):
    def test_every_skill_installs_without_siblings(self):
        with tempfile.TemporaryDirectory() as directory:
            for name in sorted(validator.NAMES):
                with self.subTest(skill=name):
                    target = Path(directory) / name
                    shutil.copytree(ROOT / "skills" / name, target)
                    self.assertEqual(validator.validate_skill(target), [])

    def test_missing_reference_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "solo-memory"
            shutil.copytree(ROOT / "skills" / target.name, target)
            (target / "references" / "continuity.md").unlink()
            self.assertTrue(any("non-self-contained" in e for e in validator.validate_skill(target)))

    def test_external_sibling_dependency_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "solo-build"
            shutil.copytree(ROOT / "skills" / target.name, target)
            (root / "other.md").write_text("uninstalled sibling")
            with (target / "SKILL.md").open("a") as handle:
                handle.write("\n[Dependency](../other.md)\n")
            self.assertTrue(any("non-self-contained" in e for e in validator.validate_skill(target)))

    def test_reference_sync_is_repeatable_and_check_is_read_only(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "shared", root / "shared")
            shutil.copytree(ROOT / "skills", root / "skills")
            source = root / "shared" / "continuity.md"
            source.write_text(source.read_text() + "\nFixture revision.\n")
            target = root / "skills" / "solo-memory" / "references" / source.name
            before = target.read_bytes()
            self.assertEqual(len(syncer.sync(root, check=True)), 6)
            self.assertEqual(target.read_bytes(), before)
            self.assertEqual(len(syncer.sync(root)), 6)
            self.assertEqual(syncer.sync(root), [])
            self.assertEqual(target.read_bytes(), source.read_bytes())

    def test_symlink_write_target_is_refused(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "shared", root / "shared")
            shutil.copytree(ROOT / "skills", root / "skills")
            outside = root / "untouched.md"
            outside.write_text("keep")
            target = root / "skills" / "solo-memory" / "references" / "continuity.md"
            target.unlink()
            target.symlink_to(outside)
            with self.assertRaises(ValueError):
                syncer.sync(root)
            self.assertEqual(outside.read_text(), "keep")

    def test_publication_manifest_matches(self):
        self.assertEqual(validator.validate(ROOT), [])


if __name__ == "__main__":
    unittest.main()
