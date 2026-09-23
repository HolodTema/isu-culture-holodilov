import ast
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQUIREMENTS = ROOT / "requirements.txt"
SRC = ROOT / "src"


def imports_in(path):
    names = set()
    tree = ast.parse(path.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                names.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
                names.add(node.module.split(".")[0])
    return names


def declared_in_requirements():
    names = set()
    for line in REQUIREMENTS.read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip()
        if not line:
            continue
        name = line
        for sep in "[]<>=!~; ":
            name = name.split(sep, 1)[0]
        names.add(name.lower().replace("_", "-"))
    return names


def main():
    found = set()
    for path in SRC.rglob("*.py"):
        found |= imports_in(path)

    stdlib = set(sys.stdlib_module_names)
    third_party = found - stdlib

    declared = declared_in_requirements()
    missing = sorted(name for name in third_party if name.lower() not in declared)

    if missing:
        print("Missing in requirements.txt: " + ", ".join(missing))
        return 1

    print("check-requirements: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

