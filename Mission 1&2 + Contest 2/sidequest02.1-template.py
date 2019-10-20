#
# CS1010X --- Programming Methodology
#
# Mission 2 - Side Quest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *
from math import sin, cos, pi

##########
# Task 1 #
##########

def tree(n, rune):
    
##    stack = scale(1/n, rune)
##    
##    for i in range(1, n):
##        layer = scale((i+1)/n, rune) #each layer going down scaled down to appropriate size
##        stack = overlay_frac(i/(i+1), stack, layer) #dynamic ratio depending on the layer
##    
##    return stack

    if n == 1:
        return rune

    #to be stacked onto the nth rune
    top_stack = scale((n-1)/n, tree(n-1, rune))
    
    return overlay_frac((n-1)/n, top_stack, rune)

# Test
show(tree(7, circle_bb))
#show(tree(9, heart_bb))


##########
# Task 2 #
##########

# use help(math) to see functions in math module
# e.g to find out value of sin(pi/2), call math.sin(math.pi/2)

def helix(rune, n):

    #given constants
    scale_ratio = 2/n
    radius = (1/2) - (1/n)
    rune = scale(scale_ratio, rune) #reduce rune size

    #defining a position function: where each point of the circle will lie
    def position(n, index, radius):
        
        angle = 2*math.pi/n
        
        x = radius*math.sin(angle*index)
        y = radius*math.cos(angle*index)

        return x, y #returns coordinates

    #first rune
    x, y = position(n, 0, radius)
    stack = translate(x, y, rune)

    #positioning subsequent runes, then stacking
    for i in range(1, n):
        x, y = position(n, i, radius)
        layer = translate(x, y, rune)
        stack = overlay_frac(i/(i+1), stack, layer) #similar to task 1
    
    return stack

# Test
#show(helix(make_cross(rcross_bb), 12))
