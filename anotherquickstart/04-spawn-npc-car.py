import lgsvl
from anotherquickstart import DEFAULT_EGO
from anotherquickstart.utilities.scene_util import load_scene, spawn_agent

sim, spawns = load_scene()
ego, forward, backward = spawn_agent(sim, DEFAULT_EGO, lgsvl.AgentType.EGO, spawns[0], init_forward_distance=5)

input('Enter to add NPC cars')

npc_list = ["Sedan", "SUV", "Jeep", "Hatchback"]
right = lgsvl.utils.transform_to_right(spawns[0])

for i, name in enumerate(npc_list):
    state = lgsvl.AgentState()
    # Spawn NPC vehicles 10 meters ahead of the EGO
    state.transform.position = spawns[0].position + (10 * forward) - (4.0 * i * right)
    state.transform.rotation = spawns[0].rotation
    spawn_agent(sim, name, lgsvl.AgentType.NPC, spawns[0], state)
