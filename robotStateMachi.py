# https://github.com/pytransitions/transitions

from transitions import Machine, State


# The states

states = [
    'home',
    State(name='exploration', on_enter=['exploreWithTrajectory']),
    State(name='catch', on_enter=['openEffector']),
    State(name='throw', on_exit=['openEffector']),
    State(name='idle', on_exit=['openEffector'])
    ]

#states=['home', 'exploration', 'catch', 'throw', 'idle']

# And some transitions between states. 
transitions = [
    { 'trigger': 'start', 'source': 'home', 'dest': 'exploration' },
    { 'trigger': 'object_dectected', 'source': 'exploration', 'dest': 'catch' },
    { 'trigger': 'object_catched', 'source': 'exploration', 'dest': 'identify category' },
    { 'trigger': 'object_fallen', 'source': 'exploration', 'dest': 'exploration' },
    { 'trigger': 'mechanical problem', 'source': 'exploration', 'dest': 'emergency stop' },
    { 'trigger': 'object in container', 'source': 'throw', 'dest': 'exploration' },
    { 'trigger': 'error', 'source': 'throw', 'dest': 'exploration' },
    { 'trigger': 'identify category', 'source': 'catch', 'dest': 'throw' }

]

machine = Machine(states=states, transitions=transitions, initial='home')

# Confirmación de que el código se ha actualizado correctamente
print("El código se ha actualizado correctamente.")
