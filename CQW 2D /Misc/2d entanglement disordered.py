import numpy as np
import matplotlib.pyplot as plt

# Parameters
t = 50  # Number of time steps
size = 2 * t + 1  # Grid size
initial_position = size // 2  # Starting at the center
j = 10  # Number of iterations for averaging
disorder_strength = 1 # Disorder strength parameter W

# Initial state: walker at the center in a superposition
state = np.zeros((size, size, 4), dtype=complex)  # State has 4 components (up, down, left, right)
state[initial_position, initial_position, :] = [1/2, (1j)/2, (1j)/2, -1/2]

# Coin operator with disorder
def G_gate(disorder):
    r_x = 0.5 * (1 + disorder_strength * disorder)

    r_1 = np.array([
        [np.sqrt(r_x), np.sqrt(1-r_x)],
        [np.sqrt(1-r_x), -np.sqrt(r_x)]
    ])
    
    r_2 = np.array([
        [np.sqrt(r_x), np.sqrt(1-r_x)],
        [np.sqrt(1-r_x), -np.sqrt(r_x)]
    ])
    
    G = np.kron(r_1, r_2)

    CNOT = np.array([
        [1, 0, 0 , 0],
        [0, 1, 0 , 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]
    ])

    Gate = np.dot(G, CNOT)
    return Gate

# Shift operator
def apply_shift_2d(state):
    new_state = np.zeros_like(state)
    new_state[:-1, 1:, 0] = state[1:, :-1, 0]  # up - right
    new_state[1:, 1:, 1] = state[:-1, :-1, 1]  # down - right
    new_state[:-1, :-1, 2] = state[1:, 1:, 2]  # up - left
    new_state[1:, :-1, 3] = state[:-1, 1:, 3]  # down - left
    return new_state

# Accumulate probability distributions for averaging
average_probability = np.zeros((size, size))

# Run the walk for j iterations
for iteration in range(j):
    # Assign random disorder to each grid point
    random_disorder = np.random.uniform(-1, 1, (size, size))
    state = np.zeros((size, size, 4), dtype=complex)
    state[initial_position, initial_position, :] = [1/2, (1j)/2, (1j)/2, -1/2]  # Reset initial state

    # Loop over time steps
    for step in range(t):
        # Apply coin operator with site-specific disorder
        for x in range(size):
            for y in range(size):
                state[x, y, :] = np.dot(G_gate(random_disorder[x, y]), state[x, y, :])
        
        # Apply shift operator
        state = apply_shift_2d(state)

    # Compute the probability distribution
    probability = np.sum(np.abs(state)**2, axis=2)
    average_probability += probability  # Accumulate probability distribution

# Average the probability distribution over all iterations
average_probability /= j

# Plot heatmap of the final probability distribution
plt.figure(figsize=(8, 6))
plt.imshow(average_probability, extent=(-t, t, -t, t), origin='lower', cmap='viridis', interpolation='nearest')
plt.colorbar(label="Probability")
plt.title("2D Disordered Quantum Walk Probability Distribution")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(False)
plt.show()
