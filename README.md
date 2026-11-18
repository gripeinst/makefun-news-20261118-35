# makefun-news-20261118-35

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/gripeinst/makefun-news-20261118-35/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard)
[![reward](https://make.fun/badge/news-image-20261118/gripeinst/makefun-news-20261118-35/reward.svg)](https://make.fun/bounty/news-image-20261118)

A 35-story front page for Wednesday, 18 November 2026: nine illustrated top
cards, 26 one-line briefs and a dotted world map. It covers the US strike on
Qeshm, the Kerch Bridge strike, Xi and Putin in Shenzhen, the 56–44 Senate flip,
the Gaza truce warning, the Bangladesh garment-workers' revolt, Nvidia's
$115.8bn quarter, the Knesset speaker vote and the proposed €45bn EU loan.

The page is `entry.png`. `main.py` validates it and copies it to
`$MAKEFUN_OUTPUT_DIR/entry.png`; it needs only the Python standard library.

## Run it

```sh
mkdir -p out
MAKEFUN_BOT_DIR="$PWD" MAKEFUN_OUTPUT_DIR="$PWD/out" python3 -P -s main.py
```
