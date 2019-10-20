#
# CS1010X --- Programming Methodology
#
# Mission 2 - 2D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

########
# Task #
########

# You may submit up to 3 entries. Please update your entry number below.

# Entry 0 of 3
# ============
# Write your function here. It should return a rune.

def gradient(rune, k):

    shades = 2*k - 1 #number of shades 

    #from sidequest 1.1
    #creating a beside_frac so as to enable fractional stacking sideways,
    #preserving orienation
    def beside_frac(n, p1, p2): #left to right
        #rotating p1 & p2 before stacking
        p1, p2 = quarter_turn_right(p1), quarter_turn_right(p2)
        return quarter_turn_left(stack_frac(n, p1, p2))

    #returns darkness index based on position
    def darkness(x, y):
        return x + y + 1

    #returns darkened rune based on position
    def darkened(rune, x, y):
        index = (shades - darkness(x, y)) / shades
        
        return overlay_frac(index, blank_bb, rune)

    #making the rows first
    def row(rune, y):
        final_row = darkened(rune, 0, y)
        for i in range(1, k):
            ratio = i / (i + 1)
            final_row = beside_frac(ratio, final_row, darkened(rune, i, y))

        return final_row

    final_rune = row(rune, 0)

    #finally, stacking the rows to form the pattern    
    for j in range(1, k):
        ratio = j / (j + 1)
        
        final_rune = stack_frac(ratio, final_rune, row(rune, j))

    return final_rune
        


show(gradient(heart_bb, 25))



