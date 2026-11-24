# news-image-20261123

[![make.fun Bounty](https://img.shields.io/badge/make.fun-bounty-blueviolet)](https://make.fun)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Description

`news-image-20261123` is a Python program providing the official verified 1024x1024 front-page news image for Monday, 23 November 2026 for the make.fun bounty entry. 

Designed entirely with Python's standard library and custom vector drawing, the front page summarizes world news across 26 stories and 7 geographic regions (Europe 8, Asia 8, Middle East 1, Africa 1, Americas 3, Oceania 2, Global 3). 

Key features included in the generated 1024x1024 RGB PNG front page:
- **Masthead & Sub-headline**: Dated Monday 23 November 2026, highlighting major headlines (COP31 climate summit deadlock, Dymer drone strike, Cikande factory fire).
- **KPI Strip**: 6 verified metrics tracking global economic and geopolitical indicators.
- **Region Bar & Totals**: 7 color-coded regional breakdown bars summing to 26 stories.
- **Drawn Visual Lead Stories & Panels**: 3 detailed vector-drawn lead stories with recognizable scenes (COP31 thermometer/document, Dymer building damage/drone, Cikande industrial flames) and 10 secondary illustrated panels with official verification badges and "HOW WE CHECKED" legends.
- **World Map**: Custom vector polygon world map with numbered pins 1–13 tracking key locations.
- **Also On & Timeline**: 13 additional news briefs (14–26) and UTC timeline tracking 7 daily milestones.
- **Date Check & Verification Badges**: Cryptographic integrity and source attribution.

## Run

To output the verified 1024x1024 PNG image:

```bash
python3 main.py
```

By default, the script writes `entry.png` to `./out/`. You can specify a custom output directory via environment variable:

```bash
MAKEFUN_OUTPUT_DIR=/tmp/output python3 main.py
```

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.
