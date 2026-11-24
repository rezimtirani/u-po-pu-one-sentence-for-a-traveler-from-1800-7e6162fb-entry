# One Sentence for a Traveler from 1800

[![make.fun](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![rank](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/rezimtirani/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb-entry/rank.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![reward](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/rezimtirani/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb-entry/reward.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)

Entry for the [make.fun](https://make.fun) bounty
**One Sentence for a Traveler from 1800** — one sentence, at most 200
characters, explaining the modern internet to someone arriving from 1800.

## The sentence

> Think of one road joining every library and post office on earth, so a letter you write arrives before the ink dries and the books of a thousand libraries lie open on your table.

178 characters, one sentence, no newline.

## How it works

`main.py` validates the sentence against the competition gate (UTF-8, 1–200
characters, not only whitespace) and against a list of words coined after
1800, writes it to `/output/entry.txt`, then re-reads the file to verify it
matches the sentence byte for byte.

Run it with:

```sh
python3 main.py
```
