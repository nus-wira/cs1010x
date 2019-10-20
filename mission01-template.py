#
# CS1010X --- Programming Methodology
#
# Mission 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *


##########
# Task 1 #
##########

def mosaic(rune1, rune2, rune3, rune4): #4 runes as parameters
    right = stack(rune1, rune2) #right side: top-right rune 1, bottom-right rune 2
    left = stack(rune4, rune3) #left side: top-left rune 4, bottom-left rune 3
    
    return beside(left, right) 


# Test
#show(mosaic(rcross_bb, sail_bb, corner_bb, nova_bb))

##########
# Task 2 #
##########

def simple_fractal(rune): #single rune as paramter
    return beside(rune, #single rune beside 
                  stack(rune,rune)) #2 stacked identical runes

# Test
#show(simple_fractal(make_cross(rcross_bb)))


