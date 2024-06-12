def biocontroller(robot, x_robot, y_robot):

    wheel_dist, wheel_diam, v_max = getRobotParams(robot)
    v, v_l, v_r = RoboVel2Wheels(x_robot, y_robot)
    r_curv = get_r_curv(wheel_dist, v_l, v_r)
    k_ttpl = get_ttpl_gain(v, v_max, r_curv)
    v_l, v_r = ApplyWheelVel(v_l, v_r, k_ttpl)
    return v_l, v_r


def getRobotParams(robot):
    robot = robot.upper()
    if robot == 'EPUCK':
        wheel_dist = 0.053 # m
        wheel_diam = 0.041 # m
        max_speed = 1200 # steps/s
        steps_per_rev = 20
        v_max = 1.2 # rev/s
        return wheel_dist, wheel_diam, v_max
    else:
        raise ValueError("Error - Robot model " + str(robot) + "is currently unsupported")

def RoboVel2Wheels(x_robot, y_robot):
    """ Maps velocity commands from the robot's coordinate 
        system to velocity commands for each wheel"""
    v = x_robot

    v_l = v * ((0.5 * y_robot) + 0.5)
    v_r = v * (-(0.5 * y_robot) + 0.5)

    return v, v_l, v_r

def get_r_curv(wheel_dist, v_l, v_r):
    """ Calculates radius of curvature
        distance between ICC and robot centre"""
    if v_l == v_r:
        r_curv = 1
    else:
        r_curv = abs(wheel_dist/2 * (v_l + v_r)/(v_r - v_l))
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


