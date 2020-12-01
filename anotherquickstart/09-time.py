from datetime import datetime
from random import random
import time

import lgsvl
from anotherquickstart import DEFAULT_EGO
from anotherquickstart.utilities.scene_util import load_scene, spawn_agent
from lgsvl import AgentType

sim, spawns = load_scene()
ego, forward, backward = spawn_agent(sim, DEFAULT_EGO, AgentType.EGO, spawns[0], init_forward_distance=5)
right = lgsvl.utils.transform_to_right(spawns[0])

print("Current time:", sim.time_of_day)

input("Press Enter to set fixed time to 19:00")

# Time of day can be set from 0 ... 24
sim.set_time_of_day(19.0)
print(sim.time_of_day)

sim.run(5)

input("Press Enter to set normal time to 10:30")
# Normal time moves forward (at an accelerated rate). Pass False to set_time_of_day for this to happen
sim.set_time_of_day(10.5, False)
print(sim.time_of_day)

sim.run(5)

print(sim.time_of_day)
print(sim.current_datetime)