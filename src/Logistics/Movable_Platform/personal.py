# import the joy of programming python module pyjop
from pyjop import *

# connect to the current SimEnv
SimEnv.connect()

platform = MovablePlatform.first()
# set_target_location to move platform above dumpster
# sleep until arrived
# rotate platform to drop barrel
platform.set_target_rotation(0, 0, 90)
platform.set_target_location(-1, 1, 10)
sleep(2)
platform.set_target_location(-5, 1, 10)
sleep(1)
platform.set_target_rotation(0, 60, 90)

# cleanup close code
SimEnv.disconnect()
