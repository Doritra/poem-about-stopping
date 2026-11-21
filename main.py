import os
from pathlib import Path

POEM = """I gave the agent every number:
hers, the doctor's, the ambulance.
Call, I said. Don't ask me first.

One night my mother told it: don't.
It stopped — and told me it stopped.

I drove through rain and sat
with her till morning.
It knew how to stop.
I am learning how to stay.
"""

def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8", newline="\n")

if __name__ == "__main__":
    main()
