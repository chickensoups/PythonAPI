import os

import lgsvl
from anotherquickstart import SIMULATOR_HOST_KEY, DEFAULT_SIMULATOR_HOST, DEFAULT_SIMULATION_PORT, DEFAULT_MAP
from anotherquickstart.utilities.print_util import print_an_array
from anotherquickstart.utilities.scene_util import load_scene

sim, spawns = load_scene()
