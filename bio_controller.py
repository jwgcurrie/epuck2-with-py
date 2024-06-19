import math
l = 0.053
r = 0.041/2

v_x = 10
theta_dot = math.pi * 0
def InverseKinematics(v_x, theta_dot, l, r):
    # Inverse Kinematics for differential drive robot
    phi_dot_L = (v_x/r) - (l * theta_dot)/(2*r)
    phi_dot_R = (v_x/r) + (l * theta_dot)/(2*r)
    return phi_dot_L, phi_dot_R



phi_dot_L, phi_dot_R = InverseKinematics(v_x, theta_dot, l, r)
if not phi_dot_L == phi_dot_R:
    R = (l/2) * (phi_dot_L + phi_dot_R)/(phi_dot_R - phi_dot_L)
    k = (1/R) ** -(1/3)
else R = 

phi_dot_LB = k * phi_dot_L
phi_dot_RB = k * phi_dot_R
print(phi_dot_RB)