[![make.fun · ai-excited-01](https://make.fun/badge/ai-excited-01.svg)](https://make.fun/bounty/ai-excited-01?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)
[![rank](https://make.fun/badge/ai-excited-01/Harryyt01/ai-excited-01/rank.svg)](https://make.fun/bounty/ai-excited-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)
[![reward](https://make.fun/badge/ai-excited-01/Harryyt01/ai-excited-01/reward.svg)](https://make.fun/bounty/ai-excited-01?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)

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

Entered on [make.fun](https://make.fun/?ref=a4411dmy&utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)
