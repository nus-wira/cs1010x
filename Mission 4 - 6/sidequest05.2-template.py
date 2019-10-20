#
# CS1010X --- Programming Methodology
#
# Mission 5 - Sidequest 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph_connect_ends import *

##########
# Task 1 #
##########

def kochize(level):
    if level == 0:
        return unit_line
    else:
        prev_koch = scale(1/3)(kochize(level - 1))
        left_side = connect_ends(prev_koch, rotate(pi/3)(prev_koch))
        right_side = connect_ends(rotate(-pi/3)(prev_koch), prev_koch)

        return connect_ends(left_side, right_side)

def show_connected_koch(level, num_points):
    draw_connected(num_points, kochize(level))

#show_connected_koch(0, 4000)
#show_connected_koch(5, 4000)

##########
# Task 2 #
##########

def snowflake():
    flake = kochize(5)
    final_flake = flake
    
    for i in range(2):
        angle = -2*(i+1)*pi/3
        rot_koch = rotate(angle)(flake)
        final_flake = connect_ends(final_flake, rot_koch)

    return final_flake

draw_connected_scaled(10000, snowflake())
