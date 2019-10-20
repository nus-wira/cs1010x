#
# CS1010X --- Programming Methodology
#
# Mission 5 - Sidequest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

##########
# Task 1 #
##########


# Visually, the two circles are exactly the same.

# However, the same point in both circles can correspond to different values of t.
# If a point on the circle was a function of t starting from t = 0 to t = 1,
# i.e. from the top of the circle going clockwise around,
# the point will have a constant speed for unit_circle,
# but will speed up as it goes for alternative_unit_circle.

# This is because of the t^2 term being present in alternative unit_circle and
# not unit_circle. If we were to use calculus to find the speed of each curve,
# unit_circle would have speed 2*pi and alternative_unit_circle speed 4*pi*t.
# The speed of unit_circle's point is constant, while alternative_unit_circle's
# is a linear polynomial w.r.t t.


##########
# Task 2 #
##########

# (a)
def spiral(t):
    return make_point(t*sin(2*pi*t), t*cos(2*pi*t))

# draw_connected_scaled(1000, spiral)

# (b)
def heart(t):
    #from mission 4
    def reflect_through_y_axis(curve):
        def reflected_curve(t):
            pt = curve(t)
            return make_point(-x_of(pt), y_of(pt))
        return reflected_curve
    
    return connect_rigidly(spiral, reflect_through_y_axis(spiral))(t)
    
draw_connected_scaled(1000, heart)
