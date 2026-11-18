# makefun-news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/aaa1112-hyl/makefun-news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/aaa1112-hyl/makefun-news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

A front-page-style image summing up Wednesday 18 November 2026's world news in one 1024×1024 picture. Lead story: the Quad meets in Manila — Trump, Modi, Takaichi and Albanese agree critical-minerals deals at the first Quad leaders' summit in two years, with Trump heading on to Shenzhen for APEC. Also covered: Ukraine strikes the Crimea bridge (a Kerch Bridge road span collapsed in Kyiv's biggest drone attack of the war; Russia hit bridges in Kyiv in reply); Iran drones target U.S. radar in Bahrain (the IRGC claimed a strike on the radar at Sheikh Isa Air Base; Bahrain said its defences intercepted the attack, with no damage reported); and an "Also today" strip — Canada–China extend trade deals as Xi meets Carney ahead of APEC, Britain sanctions Israeli settlement firms, the U.S. loses measles-free status, Nvidia beats estimates as Jensen Huang's return is debated, Mongolia's president resigns amid graft charges, and Dhoni retires from the IPL to mentor Chennai Super Kings.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies `entry.png` to `/output/entry.png`. No network, deterministic — both runs write the same bytes. `generate_image.py` is the dev-time generator (Pillow + DejaVu fonts) that drew `entry.png` from the headlines above.

Sources checked 2026-11-18: Nikkei Asia, Japan Times, Reuters (via Devdiscourse), NY Post, Outlook India, The Manila Times, NDTV.

---

<sub>Entered on [make.fun](https://make.fun/?ref=fhvxzr4c&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
