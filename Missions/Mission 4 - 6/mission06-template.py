#
# CS1010X --- Programming Methodology
#
# Mission 6
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from diagnostic import *
from hi_graph_connect_ends import *

# Mission 6 requires certain functions from Mission 5 to work.
# Do copy any relevant functions that you require in the space below:

def your_gosper_curve_with_angle(level, angle_at_level):
    if level == 0:
        return unit_line
    else:
        return your_gosperize_with_angle(angle_at_level(level))(your_gosper_curve_with_angle(level-1, angle_at_level))

def your_gosperize_with_angle(theta):
    def inner_gosperize(curve_fn):
        return put_in_standard_position(connect_ends(rotate(theta)(curve_fn), rotate(-theta)(curve_fn)))
    return inner_gosperize


# Do not copy any other functions beyond this line #
##########
# Task 1 #
##########

# Example from the mission description on the usage of time function:
# profile_fn(lambda: gosper_curve(1000)(0.1), 500)

# Choose a significant level for testing for all three sets of functions.

# -------------
# gosper_curve:
# -------------
# write down and invoke the function that you are using for this testing
# in the space below


# print(profile_fn(lambda: gosper_curve(100)(0.5), 100))

# Time measurements
# Time 1: 38.82500500003516
# Time 2: 42.89385200002016
# Time 3: 38.55044099998395
# Time 4: 39.824899999985064
# Time 5: 40.56851899997582
# Average Time: 40.13254340000003


# ------------------------
# gosper_curve_with_angle:
# ------------------------
# write down and invoke the function that you are using for this testing
# in the space below

# print(profile_fn(lambda: gosper_curve_with_angle(100, lambda lvl: pi/4)(0.5), 100))


# Time measurements
# Time 1: 41.613575999917884
# Time 2: 42.256070000121326
# Time 3: 40.11137699990286
# Time 4: 41.946874000132084
# Time 5: 40.4862329999105
# Average Time: 41.28282599999693


#
# -----------------------------
# your_gosper_curve_with_angle:
# -----------------------------
# write down and invoke the function that you are using for this testing
# in the space below

# print(profile_fn(lambda: your_gosper_curve_with_angle(100, lambda lvl: pi/4)(0.5), 100))

# Time measurements
# Time 1: 7690.441696999983
# Time 2: 7701.689351000027
# Time 3: 7689.341229000092
# Time 4: 7657.732155000076
# Time 5: 7730.275185999972
# Average Time: 7693.89592360003
#  


# Conclusion:
# It seems that more customized functions will have a slight speed advantage as compared to customizable functions. This could come from the customizable functions requiring more arguments, more time required to compute more values to get to where the customized function already was.

##########
# Task 2 #
##########

#  1) Yes.

#  2) curve parameter at the nth level is actually the (n-1)th level gosper-curve.

##########
# Task 3 #
##########

#
# Fill in this table:
#
#                    level      rotate       joe_rotate
#                      1          3              4
#                      2          5              10
#                      3          7              22
#                      4          9              46
#                      5          11             94
#
#  Evidence of exponential growth in joe_rotate.
