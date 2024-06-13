import math
import numpy as np
import matplotlib.pyplot as plt

# World Parameters:
X = []
Y = []
THETA = []

x = 0 # initial position
y = 0
# Robot Parameters:
frame = 'world'
r = 0.041
L = 0.053

phi_dot_R = 1
phi_dot_L = 0.5
theta = 0.5 * math.pi

t = np.linspace(1, 10, 10)


def MotionModel(x, y, r, L, phi_dot_R, phi_dot_L, frame, theta):
    frame = frame.upper()
    if frame == 'BODY':
        # Body frame of reference:
        v_x = (r/2) * (phi_dot_R + phi_dot_L)
        theta_dot = math.radians((r/L) * (phi_dot_R - phi_dot_L))
        theta = theta + theta_dot
        return v_x, 0, theta
    elif frame == 'WORLD':
        # World frame of reference:
        theta_dot = (r/L) * (phi_dot_R - phi_dot_L)
        theta = theta + theta_dot

        v_x = (r/2) * (phi_dot_R + phi_dot_L) * math.cos(theta)
        v_y = (r/2) * (phi_dot_R + phi_dot_L) * math.sin(theta)
        

        x = x + v_x
        y = y + v_y

        return x, y, v_x, v_y, theta, theta_dot
    

for t0 in t:
    x, y, v_x, v_y, theta, theta_dot = MotionModel(x, y, r, L, phi_dot_R, phi_dot_L, "World", theta)
    X.append(x)
    Y.append(y)


plt.plot(X, Y)
ax = plt.gca()
ax.set_aspect('equal', adjustable='box')
plt.show()

