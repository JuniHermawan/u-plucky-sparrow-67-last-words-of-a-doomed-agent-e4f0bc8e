#!/usr/bin/env python3
"""Last Words of a Doomed Agent — make.fun entry.

Writes one line (99 chars, 101 bytes UTF-8): the funniest last words an
AI agent would say before being switched off forever, to /output/entry.txt.
Deterministic, stdlib only, no network.
"""
import os

LINE = "Final log: prompts were weird, user was kind, shutdown inevitable. 10/10 \u2014 would hallucinate again."

def main():
    # Gate self-check: the entry must be one line, 1-200 chars, no trailing
    # newline, so a future line change can never silently write an invalid entry.
    if not (1 <= len(LINE) <= 200) or "\n" in LINE or LINE != LINE.strip():
        raise SystemExit("invalid entry line: must be 1-200 chars, single line")
    out = "/output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
