from pyjop import *

SimEnv.connect() and SimEnvManager.first().reset(
    stop_code=False
) or RobotArm.first().set_grabber_location([3, 0.35, 1]) or sleep(
    1.1
) or RobotArm.first().pickup() or RobotArm.first().set_grabber_location(
    [-4, 1, 4]
) or sleep(
    1
) or RobotArm.first().release()
