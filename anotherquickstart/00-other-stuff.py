import os

import lgsvl
from anotherquickstart import SIMULATOR_HOST_KEY, DEFAULT_SIMULATOR_HOST, DEFAULT_SIMULATION_PORT, DEFAULT_MAP
from anotherquickstart.utilities.print_util import print_an_array

sim = lgsvl.Simulator(os.environ.get(SIMULATOR_HOST_KEY, DEFAULT_SIMULATOR_HOST), DEFAULT_SIMULATION_PORT)
print("Current Scene = {}".format(sim.current_scene))
sim.run()
