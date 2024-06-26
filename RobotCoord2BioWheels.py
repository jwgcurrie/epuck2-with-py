

def RoboVel2Wheels(x_robot, y_robot):
    """ Maps velocity commands from the robot's coordinate 
        system to velocity commands for each wheel"""
    v = joy_left_y

    v_l = v * ((0.5 * joy_right_x) + 0.5)
    v_r = v * (-(0.5 * joy_right_x) + 0.5)

    return v, v_l, v_r

def get_r_curv(wheel_dist, v_l, v_r):
    """ Calculates radius of curvature
        distance between ICC and robot centre"""
    if v_l == v_r:
        r_curv = 1
    else:
        r_curv = wheel_dist/2 * (v_l + v_r)/(v_r - v_l)
    return r_curv

def get_ttpl_gain(v, v_max, r_curv):
    """ Calculates two-thirds power law gain"""
    k_ttpl = v * (r_curv ** (-1/3))
    k_ttpl = k_ttpl * v_max
    return k_ttpl

def ApplyWheelVel(v_l, v_r, k):
    """ Apply gain k to left and right wheel velocities"""
    v_l = k * v_l
    v_r = k * v_r
    return v_l, v_r

x_robot = 1
y_robot = 0

#RobotSpecs
wheel_dist = 0.053 # m
wheel_diam = 0.041 # m
v_max = 1 # rad/s


v, v_l, v_r = RoboVel2Wheels(x_robot, y_robot)
r_curv = get_r_curv(wheel_dist, v_l, v_r)
k_ttpl = get_ttpl_gain(v, v_max, r_curv)
v_l, v_r = ApplyWheelVel(v_l, v_r, k_ttpl)

print(v_l)