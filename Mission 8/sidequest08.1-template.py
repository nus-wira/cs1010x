#
# CS1010S --- Programming Methodology
#
# Sidequest 8.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from planets import *

# Set up the environment of the simulation
planets = (Earth, Mars, Moon)

plot_planets(planets, Mars)

##########
# Task 1 #
##########
# a)
# Follows trigonometry angle.
# E.g. 0 degree -> East
# E.g. 90 degree -> North
def get_velocity_component(angle, velocity):
    vx = velocity * cos(angle*2*pi/360)
    vy = velocity * sin(angle*2*pi/360)

    return vx, vy

print(get_velocity_component(30, 50)) #(43.30127018922194, 24.999999999999996)
# note that the exact values of each component may differ slightly due to differences in precision

# b)
def calculate_total_acceleration(planets, current_x, current_y):

    ax, ay = 0, 0
    
    for planet in planets:
        
        x_coord = get_x_coordinate(planet)
        y_coord = get_y_coordinate(planet)
        mass = get_mass(planet)
        rx, ry = x_coord - current_x, y_coord - current_y
        r = hypot(rx, ry)

        ax_p, ay_p = G*mass*rx/r**3, G*mass*ry/r**3
        ax += ax_p
        ay += ay_p

    return ax, ay

print(calculate_total_acceleration(planets, 0.1, 0.1)) #(-1511.54410020574, -1409.327982470404)

# c)
# Do not change the return statement
def f(t, Y):
    [rx, ry, vx, vy] = Y
    ax, ay = calculate_total_acceleration(planets, rx, ry)
    return np.array([vx, vy, ax, ay])

np.set_printoptions(precision=3)
print(f(0.5, [0.1, 0.1, 15.123, 20.211])) #[ 15.123 20.211 -1511.544 -1409.328]

##########
# Task 2 #
##########

# Uncomment and change the input parameters to alter the path of the spacecraft
vx, vy = get_velocity_component(77, 27.3)


##############################################################################################
# Uncomment the following line to start the plot
start_spacecraft_animation(vx, vy, f)
