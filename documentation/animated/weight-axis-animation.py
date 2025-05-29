# RENDER THIS DOCUMENT WITH DRAWBOT: https://www.drawbot.com
# $ pip install git+https://github.com/typemytype/drawbot
# $ gifsicle -i animated-vf-specimen-001.gif -O3 --colors 32 -o anim-001.gif

# Note: The monospace font Input is used in this document and needs
# to be installed for an exact rebuild: https://input.fontbureau.com/

from drawBot import *
import math


# CONSTANTS
W = 1024  # Width
H = 256  # Height
M = 64  # Margin
U = 32  # Unit (Grid Unit)
F = 64  # Frames (Animation)


# REMAP INPUT RANGE TO VARIABLE FONT AXIS RANGE
# (E.G. SINE WAVE(-1,1) to WGHT(100,900))
def remap(value, input_min, input_max, output_min, output_max):
    input_span = input_max - input_min  # FIND INPUT RANGE SPAN
    output_span = output_max - output_min  # FIND OUTPUT RANGE SPAN
    value_scaled = float(value - input_min) / float(input_span)
    return output_min + (value_scaled * output_span)


# DRAWS A GRID
def grid():
    strokeWidth(0.5)
    stroke(1, 0, 0, 0.5)
    step_X = 0
    step_Y = 0
    increment_X = U
    increment_Y = U
    for x in range(28):
        polygon((M + step_X, M), (M + step_X, H - M))
        step_X += increment_X
    for y in range(6):
        polygon((M, M + step_Y), (W - M, M + step_Y))
        step_Y += increment_Y
    fill(None)
    rect(M, M, W - (2 * M), H - (2 * M))


# NEW PAGE
def new_page():
    newPage(W, H)
    frameDuration(1 / 24)
    fill(0.051,0.066,0.09)
    rect(-2, -2, W + 2, H + 2)


# START DRAWBOT
newDrawing()


# TEST FONTS
# font("../../fonts/variable/Firjar[wdth,wght].ttf")
# for axis, data in listFontVariations().items():
#    print((axis, data))
# for eachFontName in installedFonts():
#    print(eachFontName)


# SET ANIMATION VARIABLES
varWght = 0
varWdth = 0
step = -1


# MAIN
for frame in range(F - 1):
    new_page()
    #grid()  # Toggle for grid view
    #print("Sine step:", sin(step))
    font("../../fonts/variable/Firjar[wdth,wght].ttf")
    fontSize(U * 3.5)
    stroke(None)
    fill(0.0, 1.0, 0.258)
    varWght = remap(sin(step), -1, 1, 100, 900)
    varWdth = remap(sin(step), -1, 1, 75, 125)
    fontVariations(wght=varWght)
    fontVariations(wdth=100)
    text("Balanced متوازن", ( M, U *2.25 ))
    step += 0.1
    # AUXILIARY TEXT INFO
    fill(1)
    font("../../fonts/variable/Firjar[wdth,wght].ttf")
    fontVariations(wght=400)
    fontVariations(wdth=100)
    stroke(None)
    fontSize(U / 1.5)
    text("Firjar Variable Font: Weight Axis Range (100 - 900) wght = ", (M, U * 6.25))
    text(str(int(varWght)), (M * 12.5, U * 6.25))
    stroke(1)
    strokeWidth(2)
    line((M, H - M-10), (W - M, H - M-10))

# SAVE THE ANIMATION IN THIS SCRIPT'S DIRECTORY
saveImage("weight-axis-animation.gif")

# END DRAWBOT
endDrawing()
