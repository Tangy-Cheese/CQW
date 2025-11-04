import numpy as np
import math
import matplotlib.pyplot as plt
t = 50 # Number of time steps
size = 2 * t + 1
state = np.zeros((size, size, 4), dtype=complex)
initial_position = size // 2

# Initial state: walker at the center in a superposition
state[initial_position, initial_position, :] = [1/2, (1j)/2, (1j)/2, - 1/2]

# Coin operator: Generalized 4-state Hadamard
coin_operator =  (1/2)* np.array([
    [1,  1,  1,  1],
    [1,  -1,  -1,  1],
    [1,  1,  -1,  -1],
    [1,  -1,  1,  -1],
])

# Shift operator
def apply_shift_2d(state):
    new_state = np.zeros_like(state)
    new_state[:-1, 1:, 0] = state[1:, :-1, 0]  # up - right
    new_state[1:, 1:, 1] = state[:-1, :-1, 1]  # down - right
    new_state[:-1, :-1, 2] = state[1:, 1:, 2]  # up - left
    new_state[1:, :-1, 3] = state[:-1, 1:, 3]  # down - left
    return new_state

# Quantum walk evolution
for step in range(t):
    # Apply coin operator
    for x in range(size):
        for y in range(size):
            state[x, y, :] = np.dot(coin_operator, state[x, y, :])
    # Apply shift operator
    state = apply_shift_2d(state)

print(state)
