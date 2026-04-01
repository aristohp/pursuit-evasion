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
from collections import deque

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
    
    def bfs(self, start: tuple, goal: tuple) -> int:
        queue = deque([(start, 0)])
        visited_cells = {start}
        while queue:
            position, distance = queue.popleft()
            if position == goal:
                return distance
            for neighbor in self.get_legal_move(position):
                if neighbor not in visited_cells:
                    visited_cells.add(neighbor)
                    neighbor_distance = distance + 1
                    queue.append((neighbor, neighbor_distance))
        return float('inf')
    
    def is_connected(self, pos1: tuple, pos2: tuple) -> bool:
        return self.bfs(pos1, pos2) != float('inf')
    

class Agent:
    def __init__(self, position: tuple, speed: int, role: str) -> None:
        self.position = position
        self.speed = speed
        self._role = role.lower()

    def _manhattan(self, pos1: tuple, other_pos: tuple) -> int:
        distance = abs(pos1[0] - other_pos[0]) + abs(pos1[1] - other_pos[1])
        return distance

    def choose_move(self, legal_moves: list[tuple], other_pos: tuple, grid: Grid) -> tuple:
        if self._role == 'pursuer':
            chosen_move = min(legal_moves, key=lambda move: grid.bfs(move, other_pos))
        else:
            chosen_move = max(legal_moves, key=lambda move: self._manhattan(move, other_pos))
        return chosen_move


class Game:
    def __init__(self, grid: Grid, pursuer: Agent, evader: Agent) -> None:
        self._grid = grid
        self.pursuer = pursuer
        self.evader = evader

    def is_caught(self) -> bool:
        return self.pursuer.position == self.evader.position
    
    def run(self) -> tuple:
        if not self._grid.is_connected(self.pursuer.position, self.evader.position):
            return (False, 'Never ran')
        max_turns = 1000
        turn = 0
        while not self.is_caught() and turn < max_turns:
            pursuer_position = self.pursuer.position
            evader_position = self.evader.position

            # Check legal moves of pursuer and evader
            pursuer_legal = self._grid.get_legal_move(pursuer_position)
            evader_legal = self._grid.get_legal_move(evader_position)

            self.pursuer.position = self.pursuer.choose_move(pursuer_legal, evader_position, self._grid)
            self.evader.position = self.evader.choose_move(evader_legal, pursuer_position, self._grid)

            turn += 1
        return (self.is_caught(), turn)
    

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

if __name__ == "__main__":
    grid = Grid(ROWS, COLUMNS, walls)
    pursuer = Agent((1,1), 1, "pursuer")
    evader = Agent((4,4), 1, "evader")
    game = Game(grid, pursuer, evader)
    print(game.run())
    