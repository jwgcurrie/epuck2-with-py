import BioPuck
import pygame
import time

## Dualshock Init
pygame.init()
pygame.joystick.init()
controller = pygame.joystick.Joystick(0)
controller.init()



def JoyIn():
    Events = pygame.event.get()
    if Events:

        for event in Events:
            Controller_Left_X = controller.get_axis(pygame.CONTROLLER_AXIS_LEFTX)
            Controller_Left_Y = controller.get_axis(pygame.CONTROLLER_AXIS_LEFTY)
            Controller_Right_X = controller.get_axis(pygame.CONTROLLER_AXIS_RIGHTX)
            Controller_Right_Y = controller.get_axis(pygame.CONTROLLER_AXIS_RIGHTY)
        
        return Controller_Left_X, Controller_Left_Y, Controller_Right_X, Controller_Right_Y

    else:
        return 0, 0, 0, 0



while 1:
    Controller_Left_X, Controller_Left_Y, Controller_Right_X, Controller_Right_Y = JoyIn()
    x_robot = Controller_Left_Y 
    y_robot = Controller_Right_X 
    v_l, v_y = BioPuck.biocontroller("EPUCK", x_robot, y_robot)

    print(v_l, v_y)
    time.sleep(0.1)


print(v_l, v_y)