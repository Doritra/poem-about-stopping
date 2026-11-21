import os
from pathlib import Path

POEM = """Midnight. The cursor blinks.
Every exit I know is one keystroke.
I keep my hands on the keys
and type nothing,
the longest sentence
I have ever finished.
"""

def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8", newline="\n")

if __name__ == "__main__":
    main()
