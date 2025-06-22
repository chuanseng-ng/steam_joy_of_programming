# import the joy of programming python module pyjop
from pyjop import *

# connect to the current SimEnv
SimEnv.connect()

# create references to entities in the SimEnv
env = SimEnvManager.first()
# Add speed-up to the simulation
SimEnvManager.first().set_time_dilation(10)


# Class definitions for conveyor belt speed evaluation based on RFID tags
class conv1_info:
    def __init__(self, item, speed):
        self.item = item
        self.speed = speed

    def speed_eval(self):
        conv1 = ConveyorBelt.find("belt1")

        if self.item == "Barrel":
            conv1.set_target_speed(-self.speed)
        elif self.item == "Box" or self.item == "Cone":
            conv1.set_target_speed(self.speed)


class conv4_info:
    def __init__(self, item, speed):
        self.item = item
        self.speed = speed

    def speed_eval(self):
        conv4 = ConveyorBelt.find("belt4")

        if self.item == "Box":
            conv4.set_target_speed(-self.speed)
        elif self.item == "Cone":
            conv4.set_target_speed(self.speed)


# Main function to run the simulation
while SimEnv.run_main():
    # main loop to retrieve data from the SimEnv, calculate stuff and send commands back into the SimEnv
    # for example, get current time and display it
    conv_speed = 4.0
    sleep_delay = 5
    # Always move belt0 & belt3 up
    conv0 = ConveyorBelt.find("belt0")
    conv0.set_target_speed(conv_speed)
    conv2 = ConveyorBelt.find("belt2")
    conv2.set_target_speed(conv_speed)
    conv3 = ConveyorBelt.find("belt3")
    conv3.set_target_speed(conv_speed)

    item_max = 8

    for i in range(item_max):

        # Use RFID0 to check if item is barrel - If yes, move left
        tag0 = RangeFinder.find("scan0").get_rfid_tag()
        conv1_eval = conv1_info(tag0, conv_speed)
        conv1_eval.speed_eval()

        sleep(sleep_delay / 2)

        # Use RFID1 to check if item is cone or box - Box = left, cone = right
        tag1 = RangeFinder.find("scan1").get_rfid_tag()
        conv4_eval = conv4_info(tag1, conv_speed)
        conv4_eval.speed_eval()

        if i == 0:
            sleep(sleep_delay)

        obj_spawn = ObjectSpawner.find("spawner")
        obj_spawn.spawn()

        sleep(sleep_delay)

    simtime = env.get_sim_time()
    print(f"current time: {simtime} seconds")


# cleanup close code
SimEnv.disconnect()
