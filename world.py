# Pursuit-Evasion Simulator
# Started: March 2026
#
# Goal: model the cops & robbers problem on a 2D grid
# Agent 1: Pursuer
# Agent 2: Evader
# Environment: grid with obstacles

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors
import random as r

class Grid:
    def __init__(self, rows: int, cols: int, walls: list[tuple]) -> None:
        self.rows = rows
        self.cols = cols
        self._walls = set(walls)
    
    def get_legal_move(self, position: tuple) -> list[tuple]:
        x, y = position
        possible_moves = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        legal_move = []
        for move in possible_moves:
            c_x, c_y = move
            if move not in self._walls:
                if 0 <= c_x <= self.rows - 1 and 0 <= c_y <= self.cols - 1:
                    legal_move.append(move)
                    
        return legal_move
    

class Agent:
    def __init__(self, position: tuple, speed: int):
        self.position = position
        self.speed = speed
    
    def _manhattan(self, pos1: tuple, other_pos: tuple):
        distance = abs(pos1[0] - other_pos[0]) + abs(pos1[1] - other_pos[1])
        return distance

    def choose_move(self, legal_moves: list[tuple], other_pos: tuple) -> tuple:
        chosen_move = min(legal_moves, key=lambda move: self._manhattan(move, other_pos))
        return chosen_move

# Grid dimensions
ROWS = 10
COLUMNS = 10

# Create an empty grid (0 = free cell)
grid = np.zeros((ROWS, COLUMNS))

# Set obstacles
walls = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),
         (1,0),(1,6),(1,9),(2,0),(2,2),(2,4),(2,5),(2,6),(2,8),(2,9),
         (3,0),(3,2),(3,9),(4,0),(4,2),(4,6),(4,7),(4,8),(4,9),(5,0),
         (5,1),(5,2),(5,6),(5,9),(6,0),(6,2),(6,3),(6,4),(6,6),(6,9),
         (7,0),(7,6),(7,7),(7,9),(8,0),(8,2),(8,9),(9,2),(9,9),(9,3),
         (9,4),(9,5),(9,6),(9,7),(9,8),(9,9)
         ]

# Create walls
for wall in walls:
    row, col = wall
    grid[row][col] = 1

grid[1][1] = 2 # pursuer
grid[8][8] = 3 # evader

# Agent class
# Attributes: position, speed
# methods: choose_move()

# Colours
colours = ["white","#203354","red","green"]
cmap = matplotlib.colors.ListedColormap(colours)

# Draw the grid
fig, ax = plt.subplots()
ax.imshow(grid, cmap=cmap, vmin = 0, vmax = 3)

# Grid lines
for x in range(COLUMNS + 1):
    ax.axvline(x - 0.5, color="gray", linewidth = 0.5)
for y in range(ROWS + 1):
    ax.axhline(y - 0.5, color="gray", linewidth = 0.5)

ax.set_xticks([])
ax.set_yticks([])
ax.set_title("Pursuit-Evasion Grid")

plt.show()
