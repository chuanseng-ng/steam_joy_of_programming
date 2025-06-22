from pyjop import *

SimEnv.connect() and SimEnvManager.first().reset(
    await_reset=False
) or MovablePlatform.first().set_target_rotation(
    0, 45, 0
) or MovablePlatform.first().set_target_location(
    -2, 0, 3
) or sleep(
    1
)
