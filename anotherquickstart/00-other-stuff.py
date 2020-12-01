import os

import lgsvl
from anotherquickstart import SIMULATOR_HOST_KEY, DEFAULT_SIMULATOR_HOST, DEFAULT_SIMULATION_PORT

sim = lgsvl.Simulator(os.environ.get(SIMULATOR_HOST_KEY, DEFAULT_SIMULATOR_HOST), DEFAULT_SIMULATION_PORT)
print("Current Scene = {}".format(sim.current_scene))
sim.run()
