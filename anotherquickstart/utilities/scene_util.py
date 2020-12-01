import os

import lgsvl
from anotherquickstart import SIMULATOR_HOST_KEY, DEFAULT_SIMULATOR_HOST, DEFAULT_SIMULATION_PORT, DEFAULT_MAP
from anotherquickstart.utilities.print_util import print_an_array


def load_scene(seed=None):
    sim = lgsvl.Simulator(os.environ.get(SIMULATOR_HOST_KEY, DEFAULT_SIMULATOR_HOST), DEFAULT_SIMULATION_PORT)
    print("Current Scene = {}".format(sim.current_scene))
    # Loads the named map in the connected simulator. The available maps can be set up in web interface
    if seed is not None:
        sim.load(DEFAULT_MAP, seed)
    else:
        if sim.current_scene == DEFAULT_MAP:
            sim.reset()
        else:
            sim.load(DEFAULT_MAP)
    print("Current Scene = {}".format(sim.current_scene))
    spawns = sim.get_spawn()
    print_an_array(spawns)
    return sim, spawns


def spawn_agent(sim, agent_name, agent_type, spawn_point, state=None,
                init_forward_distance=0, init_velocity=0):
    forward = lgsvl.utils.transform_to_forward(spawn_point)
    backward = lgsvl.utils.transform_to_backward(spawn_point)
    if state is None:
        state = lgsvl.AgentState()
        state.transform = spawn_point
        state.transform.position += init_forward_distance * forward
        state.velocity = init_velocity * forward
    agent = sim.add_agent(agent_name, agent_type, state)
    return agent, forward, backward


def print_current_time_frame(sim):
    print("Current time = ", sim.current_time)
    print("Current frame = ", sim.current_frame)
