import lgsvl
from lgsvl import ObjectState

from anotherquickstart import DEFAULT_EGO
from anotherquickstart.utilities.scene_util import load_scene, print_current_time_frame

sim, spawns = load_scene()
state = lgsvl.AgentState()
state.transform = spawns[0]

forward = lgsvl.utils.transform_to_forward(spawns[0])
backward = lgsvl.utils.transform_to_backward(spawns[0])

state.velocity = 20 * forward
a = sim.add_agent(DEFAULT_EGO, lgsvl.AgentType.EGO, state)
print("Vehicle bounding box =", a.bounding_box)
print_current_time_frame(sim)
input("Press Enter to drive forward for 5 seconds with velocity = 20")
sim.run(time_limit=5.0)
print_current_time_frame(sim)

input("Press Enter to continue driving for 4 seconds with velocity = 50")
a.state = ObjectState(a.transform, 50 * forward)
sim.run(time_limit=4.0)
print_current_time_frame(sim)

input("Press Enter to driving backward for 3 seconds with velocity = 100")
a.state = ObjectState(a.transform, 100 * backward)
sim.run(time_limit=3.0)
print_current_time_frame(sim)
