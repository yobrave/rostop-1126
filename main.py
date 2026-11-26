import json
import os
from pathlib import Path

ROOF = 140


def pull():
    home = Path(__file__).resolve().parent
    blob = (home / "entry.txt").read_text(encoding="utf-8")
    return " ".join(blob.split())


def guard(line):
    span = len(line)
    if span < 1 or span > ROOF:
        raise SystemExit("outside 1..%d: %d" % (ROOF, span))
    return span


def drop(line):
    den = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    den.mkdir(parents=True, exist_ok=True)
    leaf = den / "entry.txt"
    leaf.write_text(line + "\n", encoding="utf-8", newline="\n")
    return str(leaf)


def main():
    line = pull()
    span = guard(line)
    leaf = drop(line)
    summary = {
        "leaf": leaf,
        "span": span,
        "text": line.encode("utf-8").decode("utf-8"),
        "valid": 1 <= span <= ROOF,
    }
    print(json.dumps(summary))


main()
