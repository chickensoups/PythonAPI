#!/usr/bin/env python3
#
# Copyright (c) 2019-2020 LG Electronics, Inc.
#
# This software contains code licensed as described in LICENSE.
#

import math
import random
from environs import Env
import lgsvl

env = Env()

sim = lgsvl.Simulator(env.str("LGSVL__SIMULATOR_HOST", "127.0.0.1"), env.int("LGSVL__SIMULATOR_PORT", 8181))
if sim.current_scene == "BorregasAve":
    sim.reset()
else:
    sim.load("BorregasAve")

spawns = sim.get_spawn()

state = lgsvl.AgentState()
state.transform = spawns[0]
sim.add_agent(env.str("LGSVL__VEHICLE_0", "Lincoln2017MKZ (Apollo 5.0)"), lgsvl.AgentType.EGO, state)

sx = spawns[0].position.x
sy = spawns[0].position.y
sz = spawns[0].position.z

mindist = 10.0
maxdist = 40.0

random.seed(0)

while True:
    input("Press Enter to spawn NPC")

    # Creates a random point around the EGO
    angle = random.uniform(0.0, 2 * math.pi)
    dist = random.uniform(mindist, maxdist)

    point = lgsvl.Vector(sx + dist * math.cos(angle), sy, sz + dist * math.sin(angle))

    # Creates an NPC on a lane that is closest to the random point
    state = lgsvl.AgentState()
    state.transform = sim.map_point_on_lane(point)
    sim.add_agent("Sedan", lgsvl.AgentType.NPC, state)
