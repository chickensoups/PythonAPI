from random import random

import lgsvl
from anotherquickstart import DEFAULT_EGO
from anotherquickstart.utilities.scene_util import load_scene, spawn_agent

sim, spawns = load_scene()
ego, forward, backward = spawn_agent(sim, DEFAULT_EGO, lgsvl.AgentType.EGO, spawns[0], init_forward_distance=5)

input('Enter to add NPC cars')

npc_list = ["Sedan", "SUV"]
right = lgsvl.utils.transform_to_right(spawns[0])

state_1 = lgsvl.AgentState()
state_1.transform.position = spawns[0].position + (9 * forward)
state_1.transform.rotation = spawns[0].rotation
npc_agent, forward, _ = spawn_agent(sim, npc_list[0], lgsvl.AgentType.NPC, spawns[0], state_1)
npc_agent.follow_closest_lane(True, 10)

state_2 = lgsvl.AgentState()
state_2.transform.position = spawns[0].position + (9 * forward) + (4.0 * right)
state_2.transform.rotation = spawns[0].rotation
npc_agent, forward, _ = spawn_agent(sim, npc_list[1], lgsvl.AgentType.NPC, spawns[0], state_2)
npc_agent.follow_closest_lane(True, 10)

input("Press Enter to run")
sim.run(40)
