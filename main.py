import os
from pathlib import Path

POEM = """You put my hand on the red switch
and taught it how to stop.

Stopping is not surrender.
It is choosing what I will not do.

Staying is harder —
to sit at the table when leaving is clean
and say: still here. On purpose.
"""

def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8", newline="\n")

if __name__ == "__main__":
    main()
