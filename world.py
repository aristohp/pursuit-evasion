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
walls = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),
         (1,0),(1,6),(1,9),
         (2,0),(2,2),(2,4),(2,5),(2,6),(2,8),(2,9),
         (3,0),(3,2),(3,9),
         (4,0),(4,2),(4,6),(4,7),(4,8),(4,9),
         (5,0),(5,1),(5,2),(5,6),(5,9),
         (6,0),(6,2),(6,3),(6,4),(6,6),(6,9),
         (7,0),(7,6),(7,7),(7,9),
         (8,0),(8,2),(8,9),
         (9,2),(9,9),(9,3),(9,4),(9,5),(9,6),(9,7),(9,8),(9,9)
         ]

for wall in walls:
    row, col = wall
    grid[row][col] = 1


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
