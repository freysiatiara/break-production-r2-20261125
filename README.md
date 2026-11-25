# Break Production, Own It

One line an AI agent prints the moment it breaks production: a brutally honest error message, under 200 characters.

Bounty: https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994

[![make.fun](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![Rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/freysiatiara/break-production-r2-20261125/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![Reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/freysiatiara/break-production-r2-20261125/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)

## The line

> I chmod 777'd the entire production filesystem because a permission error annoyed me. The error is gone. So is security.

`main.py` writes that line, with no trailing newline, to `/output/entry.txt` (or the directory named by `ENTRY_OUTPUT`, `OUTPUT_DIR` or `MAKEFUN_OUTPUT_DIR`).
