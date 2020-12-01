import lgsvl
from lgsvl import ObjectState
from anotherquickstart import DEFAULT_EGO
from anotherquickstart.utilities.scene_util import load_scene, spawn_ego_in_spawn_point, print_current_time_frame

sim, spawns = load_scene()
agent, forward, backward = spawn_ego_in_spawn_point(sim, DEFAULT_EGO, spawns[0], 5)

print_current_time_frame(sim)
input("Press Enter to start driving")
print('Step 1: Go straight in 3 seconds')
agent.state = ObjectState(agent.transform, 15 * forward)
sim.run(time_limit=3.0)
print_current_time_frame(sim)
print('Step 2: Drift in 10 seconds')
# VehicleControl objects can only be applied to EGO vehicles
# You can set the steering (-1 ... 1), throttle and braking (0 ... 1), handbrake and reverse (bool)
c = lgsvl.VehicleControl()
c.throttle = 1
c.steering = -1.0
# a True in apply_control means the control will be continuously applied ("sticky").
# False means the control will be applied for 1 frame
agent.apply_control(c, True)
agent.state = ObjectState(agent.transform, 0 * forward)
sim.run(time_limit=10)
print_current_time_frame(sim)
