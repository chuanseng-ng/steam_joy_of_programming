# Number 5 in leaderboard - jotalamp
from pyjop import *

SimEnv.connect() and SimEnvManager.first().reset(stop_code=False) or ConveyorBelt.find(
    "belt0"
).set_target_speed(5) or ConveyorBelt.find("belt2").set_target_speed(
    5
) or ConveyorBelt.find(
    "belt3"
).set_target_speed(
    5
) or ConveyorBelt.find(
    "belt1"
).set_target_speed(
    5
)
while SimEnv.run_main():
    if abs(ConveyorBelt.find("belt0").get_current_speed()) > 2:
        ObjectSpawner.find("spawner").spawn()
    if RangeFinder.find("scan0").get_rfid_tag() == "Barrel":
        ConveyorBelt.find("belt1").set_target_speed(-5)
    else:
        ConveyorBelt.find("belt1").set_target_speed(5)
    if RangeFinder.find("scan1").get_rfid_tag() == "Box":
        ConveyorBelt.find("belt4").set_target_speed(-5)
    else:
        ConveyorBelt.find("belt4").set_target_speed(5)
