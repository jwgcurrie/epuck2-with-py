import math
import numpy as np
import matplotlib.pyplot as plt

l = 5.3
r = 4.1/2

v_x = 1
theta_dot = 1 * math.pi

def InverseKinematics(v_x, theta_dot, l, r):
    # Inverse Kinematics for differential drive robot
    phi_dot_L = (v_x/r) - (l * theta_dot)/(2*r)
    phi_dot_R = (v_x/r) + (l * theta_dot)/(2*r)
    return phi_dot_L, phi_dot_R


def ttpl_velocity(phi_dot_L, phi_dot_R):
    if phi_dot_L == -phi_dot_R:
        k = 0.01
    elif phi_dot_L == phi_dot_R:
        k = 1
    else:
        k_scale = 1/3.8
        R = (l/2) * (phi_dot_L + phi_dot_R)/(phi_dot_R - phi_dot_L)
        k = k_scale * (1/R) ** -(1/3)
    
    phi_dot_LB = k * phi_dot_L
    phi_dot_RB = k * phi_dot_R

    return phi_dot_LB, phi_dot_RB

phi_dot_L, phi_dot_R = InverseKinematics(v_x, theta_dot, l, r)
phi_dot_LB, phi_dot_RB = ttpl_velocity(phi_dot_L, phi_dot_R)


#plt.plot(theta_dot, K)
#plt.title("Biological Controller Response")
#plt.xlabel("Angular Velocity (ω) [rad/s]")
#plt.ylabel("Controller Gain (k)")
#plt.show()
