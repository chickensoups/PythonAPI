import lgsvl
from lgsvl import ObjectState, AgentType

from anotherquickstart import DEFAULT_EGO
from anotherquickstart.utilities.scene_util import load_scene, print_current_time_frame, spawn_agent

sim, spawns = load_scene()
agent, forward, backward = spawn_agent(sim, DEFAULT_EGO, AgentType.EGO, spawns[0],
                                       init_forward_distance=5, init_velocity=20)

print("Vehicle bounding box =", agent.bounding_box)
print_current_time_frame(sim)
input("Press Enter to drive forward for 5 seconds with velocity = 20")
sim.run(time_limit=5.0)
print_current_time_frame(sim)

input("Press Enter to continue driving for 4 seconds with velocity = 50")
agent.state = ObjectState(agent.transform, 50 * forward)
sim.run(time_limit=4.0)
print_current_time_frame(sim)

input("Press Enter to driving backward for 3 seconds with velocity = 100")
agent.state = ObjectState(agent.transform, 100 * backward)
sim.run(time_limit=3.0)
print_current_time_frame(sim)
