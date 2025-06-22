#import the joy of programming python module pyjop
from pyjop import *
#connect to the current SimEnv
SimEnv.connect()

#create references to entities in the SimEnv
env = SimEnvManager.first()

while SimEnv.run_main():
    # main loop to retrieve data from the SimEnv, calculate stuff and send commands back into the SimEnv
    # for example, get current time and display it
    # Always move belt0 & belt3 up
    conv0 = ConveyorBelt.find("belt0")
    conv0.set_target_speed(3.0)
    conv2 = ConveyorBelt.find("belt2")
    conv2.set_target_speed(3.0)
    conv3 = ConveyorBelt.find("belt3")
    conv3.set_target_speed(3.0)
    
    item_cnt = 8
    
    for _ in item_cnt:
        # Use RFID0 to check if item is barrel - If yes, move left
        tag0 = RangeFinder.find("scan0").get_rfid_tag()
        conv1 = ConveyorBelt.find("belt1")
        if tag0 == "Barrel":
            conv1.set_target_speed(-3.0)
            sleep(20)
        else:
            conv1.set_target_speed(3.0)
            sleep(20)

        # Use RFID1 to check if item is cone or box - Box = left, cone = right
        tag1 = RangeFinder.find("scan1").get_rfid_tag()
        conv4 = ConveyorBelt.find("belt4")
        if tag1 == "Box":
            conv4.set_target_speed(-3.0)
            sleep(20)
        else:
            conv4.set_target_speed(3.0)
            sleep(20)

        obj_spawn = ObjectSpawner.find("spawner")
        obj_spawn.spawn()
        
    simtime = env.get_sim_time()
    print(f"current time: {simtime} seconds")

	
#cleanup close code
SimEnv.disconnect()