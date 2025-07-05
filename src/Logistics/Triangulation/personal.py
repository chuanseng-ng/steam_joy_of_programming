# import the joy of programming python module pyjop
from pyjop import *

# connect to the current SimEnv
SimEnv.connect()

# create references to entities in the SimEnv
env = SimEnvManager.first()

while SimEnv.run_main():
    # main loop to retrieve data from the SimEnv, calculate stuff and send commands back into the SimEnv
    # for example, get current time and display it
    simtime = env.get_sim_time()
    print(f"current time: {simtime} seconds")

    range_a = RangeFinder.find("A").get_distance()
    range_b = RangeFinder.find("B").get_distance()
    range_c = RangeFinder.find("C").get_distance()

    mover = MovablePlatform.find("platform")

    mover.set_target_location([3.5 + range_b, 5.3 + range_c, 0])

    sleep(4)

    arm = RobotArm.first()

    sleep(2)
    arm.set_grabber_location([1.8, 0, 0.5])

    sleep(2)
    arm.pickup()

    sleep(1)
    arm.set_grabber_location([-3, 0, 3])
    mover.set_target_location([-1, 0, 0])

    sleep(3)

    arm.release()

    simtime = env.get_sim_time()
    print(f"current time: {simtime} seconds")

# cleanup close code
SimEnv.disconnect()
