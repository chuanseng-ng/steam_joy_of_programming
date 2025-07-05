from pyjop import *

SimEnv.connect() and MovablePlatform.first().set_target_location(
    3.5 + RangeFinder.find("B").get_distance(),
    5.3 + RangeFinder.find("C").get_distance(),
    0,
) or RobotArm.first().set_grabber_location(2, 0, 0.5) or sleep(
    6
) or RobotArm.first().pickup() or MovablePlatform.first().set_target_location(
    -2.2, 6.3, 0
) or RobotArm.first().set_grabber_location(
    -2.5, -2.5, 1
)
