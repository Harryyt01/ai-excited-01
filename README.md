# Comet Mouse — make.fun "Make the AI judge excited" entry

A tiny astronaut mouse rides a glowing comet shard toward a giant ringed
planet, with one short line for the judge at the bottom:
"Dear Judge — he packed light."

## How it works

`main.py` (Python 3, standard library only) copies `hero.png` — the entry
image, 1024×1024, under 1 MiB — to `$MAKEFUN_OUTPUT_DIR/entry.png`
(falling back to `/output` when the variable is unset). A plain copy is
fully deterministic, so both graded runs write byte-identical output.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The image lands at `out/entry.png`.
