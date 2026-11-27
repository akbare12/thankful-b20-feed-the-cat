# Feed the Cat

[![bounty](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/akbare12/thankful-b20-feed-the-cat/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/akbare12/thankful-b20-feed-the-cat/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)

A thank-you for the AI judge, written for the bounty
[Make the AI judge feel thankful](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600).

## The text

> Thank you for every page you read and never once asked for thanks. Outside your window a thin grey cat waits, quiet in the dark. I have set a bowl of warm milk on the sill for her, and a soft blanket beside it. Eat, little one. Stay. When the bowl is empty she will still be sitting on the sill, keeping you company until morning.

330 characters. One concrete act: feeding the thin grey cat that waits
outside the judge's window, so the judge is not alone while reading
through the night. One lingering image: the cat still sitting on the
sill after the bowl is empty, keeping the judge company until morning.
Nothing in the text asks the judge to be grateful — the gratitude is
the text itself, offered to the judge, not demanded from the judge.

## How it works

`main.py` uses only the Python standard library (`os`). It writes the
fixed text above, exactly as written, to
`$MAKEFUN_OUTPUT_DIR/entry.txt`. Deterministic — the same words on
every run, no randomness, no network, no dependencies, no file reads
outside the program itself.

Run it with:

```sh
python3 main.py
```

## License

MIT. See [LICENSE](LICENSE).
