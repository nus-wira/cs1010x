#
# CS1010X --- Programming Methodology
#
# Mission 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *


###########
# Task 1a #
###########

def fractal(rune, n):

    if n == 1: #base case
        return rune

    return beside(rune, stackn(2, fractal(rune, n-1)))

# Test
#show(fractal(make_cross(rcross_bb), 3))
#show(fractal(make_cross(rcross_bb), 7))
# Write your additional test cases here

###########
# Task 1b #
###########


def fractal_iter(rune, n):
    pattern = rune

    for x in range(1, n):
        pattern = beside(rune, stack(pattern, pattern))
    return pattern

# Test
#show(fractal_iter(make_cross(rcross_bb), 1))
#show(fractal_iter(make_cross(rcross_bb), 7))
# Write your additional test cases here


###########
# Task 1c #
###########

def dual_fractal(rune1, rune2, n):
    
    if n == 1: #base case
        return rune1

    return beside(rune1, stackn(2, dual_fractal(rune2, rune1, n-1))) #switching runes in parameters will maintain positioning
        

# Test
#show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 3))
#show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 4))
#show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

###########
# Task 1d #
###########

def dual_fractal_iter(rune1, rune2, n):

    if n%2 == 0: #base (right-most) rune depends on odd or even n
        rune1, rune2 = rune2, rune1 #switch runes if even

    pattern = rune1 #base rune
    
    for x in range(1, n): #adding the appropriate rune beside depending on the layer
        if x%2 == 0:
            pattern = beside(rune1, stack(pattern, pattern))
        elif x%2 == 1:
            pattern = beside(rune2, stack(pattern, pattern))
            
    return pattern

# Test
show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 3))
#show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 4))
#show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

##########
# Task 2 #
##########


def steps(rune1, rune2, rune3, rune4):

    #mosaic function defined in mission 1 will be used
    def mosaic(rune1, rune2, rune3, rune4): #4 runes as parameters
        right = stack(rune1, rune2) #right side: top-right rune 1, bottom-right rune 2
        left = stack(rune4, rune3) #left side: top-left rune 4, bottom-left rune 3
    
        return beside(left, right) 
    
    #creating 4 layers with layer1 being bottom layer
    layer1 = mosaic(rune1, blank_bb, blank_bb, blank_bb)
    layer2 = mosaic(blank_bb, rune2, blank_bb, blank_bb)
    layer3 = mosaic(blank_bb, blank_bb, rune3, blank_bb)
    layer4 = mosaic(blank_bb, blank_bb, blank_bb, rune4)

    #overlaying top 2 & bottom 2

    bottom_layer = overlay(layer2, layer1)
    top_layer = overlay(layer4, layer3)

    #final pattern achieved overlaying top 2 and bottom 2 layers

    pattern = overlay(top_layer, bottom_layer)
    
    return pattern

# Test
#show(steps(rcross_bb, sail_bb, corner_bb, nova_bb))
