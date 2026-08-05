#!/usr/bin/env python3
"""Relocate a variable font's fvar default to wdth=100/wght=400.

The Firjar sources only have masters at the four width/weight extremes,
so glyphsLib/fontmake cannot place the fvar default at wdth=100/wght=400
(Google Fonts' required default location) without an extra master. This
script performs the equivalent correction after the build: it recomputes
gvar deltas relative to the new default via fontTools varLib.instancer
(so outlines are still true interpolations, not just relabeled), then
fixes the name table, OS/2 metrics and head.macStyle to match.
"""
import argparse
import sys
from pathlib import Path

from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

DEFAULT_LOCATION = {"wdth": 100.0, "wght": 400.0}


def relocate_default(font: TTFont) -> TTFont:
    axis_limits = {}
    for axis in font["fvar"].axes:
        tag = axis.axisTag
        default = DEFAULT_LOCATION.get(tag, axis.defaultValue)
        axis_limits[tag] = (axis.minValue, default, axis.maxValue)

    return instantiateVariableFont(
        font,
        axis_limits,
        inplace=True,
        updateFontNames=False,
    )


def fix_name_table(font: TTFont):
    name = font["name"]
    family = "Firjar"
    subfamily = "Regular"
    full_name = f"{family} {subfamily}"
    ps_name = f"{family}-{subfamily}".replace(" ", "")

    for platform_args in [
        dict(platformID=3, platEncID=1, langID=0x409),
        dict(platformID=1, platEncID=0, langID=0),
    ]:
        name.setName(family, 1, **platform_args)
        name.setName(subfamily, 2, **platform_args)
        name.setName(full_name, 4, **platform_args)
        name.setName(ps_name, 6, **platform_args)

    # Google Fonts convention: nameID 16/17 (typographic family/subfamily)
    # must be omitted when they'd just duplicate nameID 1/2, i.e. for the
    # plain RIBBI "Regular" default instance.
    name.removeNames(nameID=16)
    name.removeNames(nameID=17)


def fix_os2_and_head(font: TTFont):
    os2 = font["OS/2"]
    os2.usWidthClass = 5  # Medium (normal) width
    os2.usWeightClass = 400  # Regular weight

    # Clear BOLD/ITALIC bits, set REGULAR bit.
    os2.fsSelection = (os2.fsSelection & ~0b0110_0001) | 0b0100_0000
    font["head"].macStyle = font["head"].macStyle & ~0b0000_0011


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Path to the built variable font")
    parser.add_argument(
        "-o", "--output", type=Path, help="Output path (defaults to overwriting input)"
    )
    args = parser.parse_args()

    font = TTFont(args.input)

    fvar_tags = {a.axisTag for a in font["fvar"].axes}
    if not set(DEFAULT_LOCATION) <= fvar_tags:
        print(
            f"error: expected axes {sorted(DEFAULT_LOCATION)} not found in "
            f"{args.input} (found {sorted(fvar_tags)})",
            file=sys.stderr,
        )
        sys.exit(1)

    font = relocate_default(font)
    fix_name_table(font)
    fix_os2_and_head(font)

    out_path = args.output or args.input
    font.save(out_path)
    print(f"Fixed VF default -> wdth=100 wght=400: {out_path}")


if __name__ == "__main__":
    main()
