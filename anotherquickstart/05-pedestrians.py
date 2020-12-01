from random import random
import time

import lgsvl
from anotherquickstart import DEFAULT_EGO
from anotherquickstart.utilities.scene_util import load_scene, spawn_agent
from lgsvl import AgentType

sim, spawns = load_scene()
ego, forward, backward = spawn_agent(sim, DEFAULT_EGO, AgentType.EGO, spawns[0], init_forward_distance=5)
right = lgsvl.utils.transform_to_right(spawns[0])

# The list of available pedestrians can be found in PedestrianManager prefab
names = [
    "Bob",
    "EntrepreneurFemale",
    "Howard",
    "Johny",
    "Pamela",
    "Presley",
    "Robin",
    "Stephen",
    "Zoe",
]

i = 0
pedestrians = []
for name in names:
    state = lgsvl.AgentState()
    state.transform.position = (
        spawns[0].position
        + (5 + (1.0 * (i // 16))) * forward
        + (5 - (1.0 * (i % 16))) * right
    )
    state.transform.rotation = spawns[0].rotation
    print("({}) adding {}".format(i + 1, name))
    p = sim.add_agent(name, lgsvl.AgentType.PEDESTRIAN, state)
    pedestrians.append(p)
    p.walk_randomly(True)
    time.sleep(0.2)
    i += 1

input("Press Enter to walk")

sim.run(10)

# input("Press Enter to stop")
for p in pedestrians:
    p.walk_randomly(False)

sim.run(5)

# input("Press Enter to start again")
for p in pedestrians:
    p.walk_randomly(True)

sim.run(10)
