import numpy as np
import matplotlib.pyplot as plt
import random
import os

os.system("cls")

# ------------------- User Inputs -------------------
try:
    L = int(input("Enter the lattice size L (e.g. 10, 20, 50): "))
    initial_iter = int(input("Enter the initial iteration count (e.g. 1000): "))
    max_iters = int(input("Enter the maximum iterations (e.g. 10000): "))
    kelvin_temp = float(input("Enter the temperature in Kelvins (e.g. 273, 298, 310): "))
except ValueError:
    print("Invalid input. Using defaults.")
    L = 20
    max_iters = 100
    initial_iter = 10
    kelvin_temp = 298.0

# Sigmoid squishify function: maps Kelvin -> simulation temp (0–10)
def sigmoid_scaled_temperature(kelvin, center=298, scale=0.1):
    """Squishify the Kelvin input using a sigmoid and scale to 0-10."""
    sigmoid = 1 / (1 + np.exp(-scale * (kelvin - center)))
    return 10 * sigmoid  # map [0, 1] -> [0, 10]

# Convert to simulation temperature using sigmoid mapping
temperature = sigmoid_scaled_temperature(kelvin_temp)

# Calculate step size and number of plots (~6)
num_plots = int(input("Enter number of plots to be plotted:"))
step_size = max(1, (max_iters - initial_iter) // (num_plots - 1))

# Recalculate num_plots based on range and step_size (in case inputs were weird)
# actual_range = max_iters - initial_iter
# num_plots = actual_range // step_size + 1

# Compute local energy (count occupied neighbors)
def local_energy(x, y, lattice):
    neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    return sum(lattice[nx, ny] for nx, ny in neighbors if 0 <= nx < L and 0 <= ny < L)

# Create appropriate subplot grid
rows = (num_plots + 4) // 5  # 5 columns per row
cols = min(num_plots, 5)
fig, axes = plt.subplots(rows, cols, figsize=(3 * cols, 3 * rows))
axes = axes.flatten()

# Loop over different iteration values
for idx, iters in enumerate(range(initial_iter, max_iters + 1, step_size)):
    if idx >= num_plots:
        break

    lattice = np.zeros((L, L), dtype=int)

    for _ in range(iters):
        x = random.randint(0, L-1)
        y = 0

        # Move down until blocked
        while y < L-1 and lattice[x, y+1] == 0:
            y += 1

        lattice[x, y] = 1

        # Attempt diffusion using Metropolis-Hastings
        for _ in range(10):
            nx = x + random.choice([-1, 0, 1])
            if 0 <= nx < L:
                delta_E = local_energy(nx, y, lattice) - local_energy(x, y, lattice)
                if delta_E < 0 or np.exp(-delta_E / temperature) > random.random():
                    lattice[x, y], lattice[nx, y] = 0, 1
                    x = nx

    # Plot the lattice
    axes[idx].imshow(lattice, cmap='gray_r', origin='lower')
    axes[idx].set_title(f"Iterations: {iters}")
    axes[idx].set_xticks([])
    axes[idx].set_yticks([])

# Hide any extra subplots
for j in range(num_plots, len(axes)):
    axes[j].axis('off')

plt.tight_layout()
plt.show()

