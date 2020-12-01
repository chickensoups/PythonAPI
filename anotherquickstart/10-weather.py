from random import random
import time

import lgsvl
from anotherquickstart import DEFAULT_EGO
from anotherquickstart.utilities.scene_util import load_scene, spawn_agent
from lgsvl import AgentType

sim, spawns = load_scene()
ego, forward, backward = spawn_agent(sim, DEFAULT_EGO, AgentType.EGO, spawns[0], init_forward_distance=5)
right = lgsvl.utils.transform_to_right(spawns[0])

print(sim.weather)

input("Press Enter to set rain to 80%")
sim.weather = lgsvl.WeatherState(rain=0.8, fog=0, wetness=0, cloudiness=0, damage=0)
print(sim.weather)
sim.run(10)

input("Press Enter to set fog to 70%")
sim.weather = lgsvl.WeatherState(rain=0.8, fog=0.7, wetness=0, cloudiness=0, damage=0)
print(sim.weather)
sim.run(5)

input("Press Enter to set wetness to 6%")
sim.weather = lgsvl.WeatherState(rain=0.8, fog=0.3, wetness=0.6, cloudiness=0, damage=0)
print(sim.weather)
sim.run(5)

input("Press Enter to reset to 0")
sim.weather = lgsvl.WeatherState(rain=0, fog=0, wetness=0, cloudiness=0, damage=0)
print(sim.weather)
sim.run(5)
