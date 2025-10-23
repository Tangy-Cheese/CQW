import numpy as np
import matplotlib.pyplot as plt

# Outlining Variables:
t = 100  # Number of max time steps
num_positions = 200  # Number of positions on the line
initial_position = num_positions // 2  # Start at Middle
time_to_plot = [100]  # Specific times to plot
j = 1  # Number of iterations for averaging
disorder_strength = 0.9 # Disorder strength parameter W

# Initial state (Eqn. 5):
initial_state = np.zeros((num_positions, 2), dtype=complex)
initial_state[initial_position] = [1 / np.sqrt(2), 1j / np.sqrt(2)]  # Initial Pauli Y Gate Eigenvectors

# Shift operator (Eqn. 4):
def apply_shift_operator(state):
    new_state = np.zeros_like(state)
    new_state[1:, 0] = state[:-1, 0]  # down state shift
    new_state[:-1, 1] = state[1:, 1]  # up state shift
    return new_state

# Coin operator (G_gate) with site-specific disorder
def G_gate(position):
    r_x = r_values[position]  # Use site-specific r value
    G = np.array([[np.sqrt(r_x), np.sqrt(1 - r_x)], [np.sqrt(1 - r_x), -np.sqrt(r_x)]])
    return G

# Aubry andre disorder
golden = ((5 ** 0.5)-1) / 2
beta = 2 * np.pi * np.random.random()  # Random realization parameter
#r_values = np.array([(disorder_strength * np.cos(golden * x + beta) + 2) / 2 for x in range(num_positions)])

# Accumulate probability distributions across all iterations
average_probability_distributions = np.zeros((len(time_to_plot), num_positions))

# Run the walk for j iterations
for iteration in range(j):
    # Assign Aubry-André disorder
    beta = 2 * np.pi * np.random.random()  # Random realization parameter
    r_values = np.array([(disorder_strength * np.cos(golden * x + beta) + 1) / 2 for x in range(num_positions)])
    state = np.copy(initial_state)  # Reset state for each iteration

    # Loop over time steps
    for step in range(t):
        # Apply coin operator with site-specific disorder
        state = np.array([np.dot(G_gate(pos), state[pos]) for pos in range(num_positions)])
        state = apply_shift_operator(state)  # Apply shift operator

        # If this time step is in time_to_plot, store the probability distribution
        if step + 1 in time_to_plot:
            probability_distribution = np.sum(np.abs(state) ** 2, axis=1)  # Eqn. 1
            time_index = time_to_plot.index(step + 1)
            average_probability_distributions[time_index] += probability_distribution  # Accumulate

# Divide by the number of iterations to get the average
average_probability_distributions /= j

# Plotting
positions = np.arange(-initial_position, initial_position)
plt.figure(figsize=(10, 6))

# Plot each average distribution for specified times
for i, distribution in enumerate(average_probability_distributions):
    plt.plot(positions, distribution, label=f"t = {time_to_plot[i]}")

plt.xlabel("Position (x)")
plt.ylabel("Probability")
plt.title("Average Probability Distribution for AA-model Walk")
plt.legend()
plt.show()