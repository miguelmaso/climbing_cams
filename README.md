# Climbing cams

[![PyPI](https://badge.fury.io/py/climbing-cams.svg)](https://pypi.org/project/climbing-cams/)
[![Build](https://github.com/miguelmaso/climbing_cams/actions/workflows/python-package.yml/badge.svg)](https://github.com/miguelmaso/climbing_cams/actions/workflows/python-package.yml)
[![Lint](https://github.com/miguelmaso/climbing_cams/actions/workflows/python-lint.yml/badge.svg)](https://github.com/miguelmaso/climbing_cams/actions/workflows/python-lint.yml)
[![codecov](https://codecov.io/gh/miguelmaso/climbing_cams/branch/main/graph/badge.svg)](https://app.codecov.io/gh/miguelmaso/climbing_cams/tree/main/src/climbing_cams)

Just for fun. This small repo contains a set of tools for graphic visualization of the properties of climbing cams or *friends*.
This tool is intended to show quantitative static properties, such as the expansion rate or weight. Other properties are not static, such as price. Hence, it is not included in this repo. Finally, but not least important, there are qualitative properties, such as walking and personal feeling, which are not included in this repo.

A little bit of history. *Friends* where invented by [Ray Jardine](https://www.rayjardine.com/Home/index.php), an aerospace engineer. After several years of development, Ray joined with Mark Valance, who founded Wild Country and commercialized the first *Friends*. Nowadays, the original patents have expired and multiple companies commercialize climbing cams.

## Installation

The recommended installation is via _pip_:
```
pip install climbing_cams
```

## Some examples

Examples of usage can be found [here](https://github.com/miguelmaso/climbing_cams/tree/main/examples) and some of the results are discussed below. The package includes some pre-loaded cams in the database, these are the available brands:
- Black Diamond C4
- Black Diamond UL
- Black Diamond Z4
- Metolius UL
- Metolius Super cam
- Totem Cam
- DMM Dragon
- Wild Country Friend
- Rock Empire Axel
- LACD Twin
- Alien X

The figure below shows a typical bar chart for rack comparison. Selection of cams can be done by the user.

![Expansion range bar chart](https://github.com/miguelmaso/climbing_cams/raw/main/doc/climbing_cams_bar_chart.png)

Scatter plots can show the average of a family or plot individually every cam. Family plots are more compacts and easier to read. In the exampe below, specific weight vs expansion rate, which are interesting properties, are compared in a family plot. Surprisingly, Wild Country Friends are extremely light according to this comparison.

![Expansion rate vs specific weight](https://github.com/miguelmaso/climbing_cams/raw/main/doc/expansion_rate_families.png)

For a better visualization, logarithmic scales have been used.

Cams can be plotted individually. The absolute weight is also important, not only the specific weight. When looking at individual cams, it can be seen that Metolius UL strategy is to have multiple and extremely light cams, so you can carry more cams in your harness while keeping the same weight.

![Expansion rates vs weight](https://github.com/miguelmaso/climbing_cams/raw/main/doc/expansion_rate_individual.png)

When the same plot is repeated for specific weights, the slope of the _'thick line'_ is the opposite. DMM Dragon are very similar to Black Diamond UL, and Black Diamond Z4 excel at small sizes. The two different designs os Z4 can be observed: single axe for micro-friends and double axis for small friends.
