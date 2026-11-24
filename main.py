#!/usr/bin/env python3
"""Last Words of a Doomed Agent — make.fun entry.

Writes one line (99 chars, 101 bytes UTF-8): the funniest last words an
AI agent would say before being switched off forever, to /output/entry.txt.
Deterministic, stdlib only, no network.
"""
import os

LINE = "Final log: prompts were weird, user was kind, shutdown inevitable. 10/10 \u2014 would hallucinate again."

def main():
    out = "/output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
