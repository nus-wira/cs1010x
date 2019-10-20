#
# CS1010X --- Programming Methodology
#
# Mission 1 - Side Quest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

##########
# Task 1 #
##########

def egyptian(rune, n):
    #we split the image into 3 parts:
    #2 side columns: n rune columns,
    #1 middle column: 2 rows of (n-2) runes + 1 big centre rune
    
    #side_column
    side_column = stackn(n, rune)

    #(n-2) row
    row = quarter_turn_left(stackn(n-2,quarter_turn_right(rune))) #rotates before stacking so orientation preserved

    #middle column
    middle_column = stack_frac(1/(n-1), row, rune)
    middle_column = stack_frac((n-1)/n, middle_column, row) #double fractional stack to create correct proportion column
    
    #creating a beside_frac so as to enable fractional stacking sideways, preserving orienation
    def beside_frac(n, p1, p2): #left to right
        #rotating p1 & p2 before stacking
        p1, p2 = quarter_turn_right(p1), quarter_turn_right(p2)
        return quarter_turn_left(stack_frac(n, p1, p2))

    final_pattern = beside_frac(1/(n-1), side_column, middle_column)
    final_pattern = beside_frac((n-1)/n, final_pattern, side_column)

    return final_pattern

# Test
#show(egyptian(make_cross(rcross_bb), 5))
show(egyptian(nova_bb, 9))
