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
#varWght = 100
varWdth = 0
step = -1

txt = "إدراك درس"
stepr = 25
varWghtList = [100,200,300,400,500,600,700,800,900]
directionList = [1] * len(varWghtList)  # 1 means increasing, -1 means decreasing

# MAIN
for frame in range(F - 1):
    new_page()
    #grid()  # Toggle for grid view
    #print("Sine step:", sin(step))
    font("../../fonts/variable/Firjar[wdth,wght].ttf")
    fontSize(U * 3.5)
    stroke(None)
    fill(0.0, 1.0, 0.258)
    fontVariations(wdth=100)
    T = FormattedString()
    T.fontSize(U * 3.5)
    T.font("../../fonts/variable/Firjar[wdth,wght].ttf")
    #for j, char in enumerate(txt):
        #varWght = remap(sin(stepr), -1, 1, 100, 900)
        #fontVariations(wght=varWght)
        #T.append(char, fill=(1), fontVariations={"wght":varWght})
    for char, varWght in zip(txt, varWghtList):
        T.append(char, fill=(1), fontVariations={"wght": varWght})
        
    for i in range(len(varWghtList)):
        varWghtList[i] += stepr * directionList[i]
        # Bounce logic
        if varWghtList[i] >= 900:
            varWghtList[i] = 900
            directionList[i] = -1
        elif varWghtList[i] <= 100:
            varWghtList[i] = 100
            directionList[i] = 1        

    text(T, ( M, U *2.25 ))
    step += 0.1
    

# SAVE THE ANIMATION IN THIS SCRIPT'S DIRECTORY
saveImage("dance.gif")

# END DRAWBOT
endDrawing()
