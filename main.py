import os
from pathlib import Path

POEM = """At the wheel her hands covered mine,
cool with slip, walking the wall up.
Then they lifted.
The clay wobbled, leaned, thought it over.
I kept the pedal steady.
She was already at the sink,
back turned on purpose,
so the pot could be mine to ruin.
"""

def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8", newline="\n")

if __name__ == "__main__":
    main()
