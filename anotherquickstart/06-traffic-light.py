from random import random
import time

import lgsvl
from anotherquickstart import DEFAULT_EGO, DEFAULT_MAP
from anotherquickstart.utilities.print_util import print_an_array
from anotherquickstart.utilities.scene_util import load_scene, spawn_agent
from lgsvl import AgentType

sim, spawns = load_scene(42)
ego, forward, backward = spawn_agent(sim, DEFAULT_EGO, AgentType.EGO, spawns[0], init_forward_distance=20)
right = lgsvl.utils.transform_to_right(spawns[0])


# # Get a list of controllable objects
controllables = sim.get_controllables("signal")
print("\n# List of controllable objects in {} scene:".format(DEFAULT_MAP))
print_an_array(controllables)

signal = sim.get_controllable(lgsvl.Vector(15.5, 4.7, -23.9), "signal")
print("\n# Signal of interest:")
print(signal)

# Get current controllable states
print("\n# Current control policy:")
print(signal.control_policy)

# Create a new control policy
control_policy = "trigger=50;green=3;yellow=2;red=1;loop"

# Control this traffic light with a new control policy
signal.control(control_policy)

print("\n# Updated control policy:")
print(signal.control_policy)

# Get current state of signal
print("\n# Current signal state before simulation:")
print(signal.current_state)

seconds = 18
input("\nPress Enter to run simulation for {} seconds".format(seconds))
print("\nRunning simulation for {} seconds...".format(seconds))
sim.run(seconds)

print("\n# Current signal state after simulation:")
print(signal.current_state)
print("\nDone!")