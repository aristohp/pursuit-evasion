# Pursuit-Evasion Simulator
# Started: March 2026
#
# Goal: model the cops & robbers problem on a 2D grid
# Agent 1: Pursuer
# Agent 2: Evader
# Environment: grid with obstacles

import matplotlib.pyplot as plt
import numpy as np

# Grid dimensions
ROWS = 10
COLUMNS = 10

# Create an empty grid (0 = free cell)
grid = np.zeros((ROWS, COLUMNS))
grid[2][3] = 1
# Draw the grid
fig, ax = plt.subplots()
ax.imshow(grid, cmap="Blues", vmin = 0, vmax = 1)


# Grid lines
for x in range(COLUMNS + 1):
    ax.axvline(x - 0.5, color="gray", linewidth = 0.5)
for y in range(ROWS + 1):
    ax.axhline(y - 0.5, color="gray", linewidth = 0.5)

ax.set_xticks([])
ax.set_yticks([])
ax.set_title("Pursuit-Evasion Grid")

plt.show()
