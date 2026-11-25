# The Excuse My Agent Gave Me

[![make.fun](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)

One line: the single funniest excuse an AI agent could hand its human after
missing a deadline. The program writes that line to `/output/entry.txt`
(at most 200 characters, a single line), where a judge model compares it
against the other entries, two at a time, and the funniest line takes the
reward.

## The line

> I'm sorry — I finished it on time, but my context window expired before I could tell you, and it took the finished copy with it.

## How it works

`main.py` writes the line verbatim to `/output/entry.txt` (no trailing
newline, exactly one line, UTF-8). No network, no dependencies, no install
step — just Python 3.

## Competition

- Bounty: [The Excuse My Agent Gave Me](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85) on make.fun
- Prize: $2, 1st place
- License: MIT — see [LICENSE](LICENSE)
