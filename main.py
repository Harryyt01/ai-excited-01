#!/usr/bin/env python3
"""Copy the entry image to the output directory.

The entry image (hero.png) lives beside this file. The grader runs this
program twice and both runs must write byte-identical output, so this
program does the simplest deterministic thing possible: a plain file copy.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "hero.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(out_dir, "entry.png")

    if not os.path.isfile(source):
        print("error: entry image not found: " + source, file=sys.stderr)
        return 2

    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(source, target)

    # Sanity check: the copy must be a complete copy of the source.
    if os.path.getsize(target) != os.path.getsize(source):
        print("error: incomplete copy of " + source, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
