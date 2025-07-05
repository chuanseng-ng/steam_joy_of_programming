from pyjop import *

SimEnv.connect() and MovablePlatform.first().set_target_location(
    3.26 + RangeFinder.find("B").get_distance(),
    3.41 + RangeFinder.find("C").get_distance(),
    0,
) or RobotArm.first().set_grabber_location(2, 2, 0.4) or sleep(
    3.3
) or RobotArm.first().pickup() or MovablePlatform.first().set_target_location(
    -2.2, 6.3, 0
) or RobotArm.first().set_grabber_location(
    -2.5, -2.5, 1
)
