#
# CS1010X --- Programming Methodology
#
# Mission 2 - 3D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

########
# Task #
########

# You may submit up to three entries. Please update your entry number below.

# Entry 0 of 3
# ============
# Write your function here. It should return a rune.
def tree_mod(center_x, center_y, rune, n):


    #defining a position function: where each circle will lie
    def position_scale(index):

        pos_ratio = (n-index)/n
        
        x = pos_ratio*center_x
        y = pos_ratio*center_y

        scale_ratio = (index+1)/(n+1)

        return x, y, scale_ratio #returns coordinates

    #first rune
    x, y, scale_ratio = position_scale(0)
   
    stack = translate(x, y, scale(scale_ratio, rune))

    #positioning subsequent runes, then stacking
    for i in range(1, n+1):
        x, y, scale_ratio = position_scale(i)
        print(x,y)
        layer = translate(x, y, scale(scale_ratio, rune))
        stack = overlay_frac(i/(i+1), stack, layer) #similar to task 1
    
    return stack



# Use one of the following methods to display your rune:
# stereogram(<your rune>)
# anaglyph(<your rune>)
# hollusion(<your rune>)

show(hollusion(tree_mod(0.25,0.25,circle_bb,25)))
