# Yarn Substitution Toolkit

Reusable records and a small, dependency-free purchasing calculator for knitters and crocheters comparing replacement yarns.

The accompanying worked guide is at [YarnSwapGuide](https://yarnswapguide.com/drops-air-yarn-substitute/).

## Files

- `data/yarn-specifications.csv`: eleven dated product records, with manufacturer URLs. Alternatives are editorial candidates, not proven equivalents. Some fields are not published; do not replace those with zero.
- `templates/colour-purchase.csv`: a per-colour order record, with clearly labelled hypothetical examples and blank rows. This CSV is not an automatically recalculating spreadsheet.
- `templates/paired-swatch.csv`: blank paired comparison measurements. No physical test results are included.
- `checklist.md`: a short substitution decision and measurement checklist.
- `calculate.py`: a command-line calculator using exact decimal inputs and rounding up separately for every colour. Python standard library only.
- `test_calculate.py`: boundary, rounding and invalid-input checks.

## Run

Use Python 3.10 or later. From this folder:

```sh
python calculate.py --metres-per-ball 75 --colour Main=360 --colour Contrast=60
python calculate.py --metres-per-ball 75 --colour Red=80 --colour Blue=80 --colour Cream=80
python -m unittest -v
```

First example: five main-colour balls plus one contrast-colour ball. Second example: two balls of each colour, six in total. Pooling the second example's 240 m would suggest four balls and would ignore the separate colour requirements.

`--extra-per-colour` adds your chosen extra metres to every colour; its default is zero, not a recommended allowance. Needles, swatches, waste and pattern-specific requirements are not inferred. Different yarn lengths require separate calculator runs.

Formula: `balls for a colour = ceil((required metres + chosen extra metres) / metres per replacement ball)`. Convert original grams first if necessary: `required metres = original grams / original grams per ball * original metres per ball`.

## Evidence limits

The specification snapshot was compiled from manufacturer product pages on the dates recorded in the CSV, not from laboratory tests. Labels can change; check the exact product and your ball label. Standard label gauges do not establish the same fabric, care response, consumption or finished fit. Blank swatch fields mean no measured result, not a pass.

The calculator tests establish software arithmetic only. They are not yarn trials. Sample purchasing inputs are hypothetical and do not belong to a real garment pattern. No affiliation with, or endorsement by, the yarn manufacturers is claimed.

## Reuse and corrections

Original code, checklist and template structure are MIT licensed; see `LICENSE`. Manufacturer names, trademarks and third-party source pages remain their owners' property. The licence does not grant rights to third-party photographs or page text. Retain source links and retrieval dates when reusing the factual specification records. For a correction, include the exact product, manufacturer source and date; never submit invented swatch results.
