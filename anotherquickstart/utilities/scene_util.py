import os

import lgsvl
from anotherquickstart import SIMULATOR_HOST_KEY, DEFAULT_SIMULATOR_HOST, DEFAULT_SIMULATION_PORT, DEFAULT_MAP, DEFAULT_EGO
from anotherquickstart.utilities.print_util import print_an_array


def load_scene():
    sim = lgsvl.Simulator(os.environ.get(SIMULATOR_HOST_KEY, DEFAULT_SIMULATOR_HOST), DEFAULT_SIMULATION_PORT)
    print("Current Scene = {}".format(sim.current_scene))
    # Loads the named map in the connected simulator. The available maps can be set up in web interface
    if sim.current_scene == DEFAULT_MAP:
        sim.reset()
    else:
        sim.load(DEFAULT_MAP)
    print("Current Scene = {}".format(sim.current_scene))
    spawns = sim.get_spawn()
    print_an_array(spawns)
    return sim, spawns


def spawn_ego_in_spawn_point(sim, agent_name, spawn_point, forward_distance=0):
    state = lgsvl.AgentState()
    state.transform = spawn_point
    forward = lgsvl.utils.transform_to_forward(spawn_point)
    backward= lgsvl.utils.transform_to_backward(spawn_point)
    state.transform.position += forward_distance * forward
    agent = sim.add_agent(agent_name, lgsvl.AgentType.EGO, state)
    return agent, forward, backward


def print_current_time_frame(sim):
    print("Current time = ", sim.current_time)
    print("Current frame = ", sim.current_frame)
