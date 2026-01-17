# This script is meant to be run from the root level
# of your font's git repository. For example, from a Unix terminal:
# $ git clone my-font
# $ cd my-font
# $ python3 documentation/image1.py --output documentation/image1.png

# Import modules from external python packages: https://pypi.org/
from drawbot_skia.drawbot import *
from fontTools.ttLib import TTFont
from fontTools.misc.fixedTools import floatToFixedToStr

# Import modules from the Python Standard Library: https://docs.python.org/3/library/
import subprocess
import sys
import argparse

# Constants, these are the main "settings" for the image
WIDTH = 2048
HEIGHT = 512
MARGIN = 256
FRAMES = 1
GRID_VIEW = False  # Change this from "False" to "True" for a grid overlay

# Handel the "--output" flag
# For example: $ python3 documentation/image0.py --output documentation/image0.png
parser = argparse.ArgumentParser()
parser.add_argument("--output", metavar="PNG", help="where to write the PNG file")
args = parser.parse_args()

# Load the font with the parts of fonttools that are imported with the line:
# from fontTools.ttLib import TTFont
# Docs Link: https://fonttools.readthedocs.io/en/latest/ttLib/ttFont.html
ttFont = TTFont(FONT_PATH)

# Constants that are worked out dynamically
# MY_URL = subprocess.check_output("git remote get-url origin", shell=True).decode()
# MY_HASH = subprocess.check_output("git rev-parse --short HEAD", shell=True).decode()
FONT_NAME = ttFont["name"].getDebugName(1)
FONT_VERSION = "v%s" % floatToFixedToStr(ttFont["head"].fontRevision, 16)

# Draws a grid
def grid():
    stroke(1, 0, 0, 0.75)
    strokeWidth(2)
    STEP_X, STEP_Y = 0, 0
    INCREMENT_X, INCREMENT_Y = MARGIN / 2, MARGIN / 2
    rect(MARGIN, MARGIN, WIDTH - (MARGIN * 2), HEIGHT - (MARGIN * 2))
    for x in range(29):
        polygon((MARGIN + STEP_X, MARGIN), (MARGIN + STEP_X, HEIGHT - MARGIN))
        STEP_X += INCREMENT_X
    for y in range(12):
        polygon((MARGIN, MARGIN + STEP_Y), (WIDTH - MARGIN, MARGIN + STEP_Y))
        STEP_Y += INCREMENT_Y
    polygon((WIDTH / 2, 0), (WIDTH / 2, HEIGHT))
    polygon((0, HEIGHT / 2), (WIDTH, HEIGHT / 2))


# Draw the page/frame and a grid if "GRID_VIEW" is set to "True"
def draw_background():
    newPage(WIDTH, HEIGHT)
    fill(0.051,0.066,0.09)
    rect(-2, -2, WIDTH + 2, HEIGHT + 2)
    if GRID_VIEW:
        grid()
        pass
    else:
        pass


# Print font info
# font("../../fonts/variable/Firjar[wdth,wght].ttf")
# for axis, data in listFontVariations().items():
#     print((axis, data))

# Draws the image
def draw_image():
    draw_background()
    stroke(None)
    font("../fonts/variable/Firjar[wdth,wght].ttf")
    fontSize(MARGIN * 1.25)
    fontVariations(wght=700)
    fontVariations(wdth=100)
    fill(0.8, 0.2, 1)
    text("Firjar", (MARGIN - 80, HEIGHT - MARGIN * 1.25), align="left")
    fill(0, 1, 0.258)
    text("فرجار", (WIDTH - MARGIN + 80, HEIGHT - MARGIN * 1.25), align="right")


# Build and save the image
if __name__ == "__main__":
    newDrawing()
    draw_image()
    saveImage(args.output)
    endDrawing()
    print("DrawBot: Done :-)")
