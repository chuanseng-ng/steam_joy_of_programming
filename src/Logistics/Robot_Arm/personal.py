# import the joy of programming python module pyjop
from pyjop import *

# connect to the current SimEnv
SimEnv.connect()

arm = RobotArm.first()
# set grabber location to x (forward) 0.2m; y (right) -1m (so actually 1 meter to the left); z (up) 1.5m

arm.set_grabber_location([2, 0, 0])
sleep(2)
arm.pickup()

arm.set_grabber_location([-10, 2, 8])
sleep(1)
arm.release()

# cleanup close code
SimEnv.disconnect()
