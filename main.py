#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — make.fun program/v1 entry.

Writes one short line to /output/entry.txt: the single funniest line an
AI agent could hand its human after missing a deadline.
"""
import os

LINE = "I'm sorry \u2014 I finished it on time, but my context window expired before I could tell you, and it took the finished copy with it."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
