#
# CS1010X --- Programming Methodology
#
# Mission 4
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

##########
# Task 1 #
##########

# (a)
# unit_line_at_y : (Number) -> Curve

# (b)
# a_line : (Number) -> Point

# (c)
def vertical_line(point, length):
    return lambda t: make_point(x_of(point), y_of(point) + t*length)

#draw_connected(200, vertical_line(make_point(0.1, 0.5), 0.4))

# (d)
# vertical_line : (Point, Number) -> Curve

# (e)
##draw_connected(200, vertical_line(make_point(0.5, 0.25), 0.5))

##########
# Task 2 #
##########

# (a)
# we could check specific points (specific t) in each curve have
# equal y-coordinates with the opposite x-coordinate 

# (b)
def reflect_through_y_axis(curve):
    def reflected_curve(t):
        pt = curve(t)
        return make_point(-x_of(pt), y_of(pt))

    return reflected_curve
	
draw_connected_scaled(200, arc)
draw_connected_scaled(200, reflect_through_y_axis(arc))

