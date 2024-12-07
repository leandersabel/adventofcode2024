# https://adventofcode.com/2024/day/6
from collections import deque
from copy import deepcopy
from enum import Enum
from multiprocessing import Pool

from solution import Solution

direction = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

class Status(Enum):
    MOVING = 0
    OUT = 1
    LOOP = 2

class Day6Solution(Solution):

    def parse_input(self):
        return [list(row) for row in self.input_data.split('\n')]

    def solve_part1(self):
        grid = deepcopy(self.parsed_input)
        guard = next((r, row.index('^')) for r, row in enumerate(grid) if '^' in row)

        while guard not in [Status.OUT, Status.LOOP]:
            guard = move_guard(grid, guard, set())

        return sum(row.count('x') for row in grid) + 1


    def solve_part2(self):
        grid = self.parsed_input
        variants = generate_variants(grid)

        with Pool() as pool:
            results = pool.map(simulate_variant, variants)

        return sum(results)


def move_guard(grid, guard, visited):
    r, c = guard

    while collision(grid, r, c):
        grid[r][c] = turn_right.get(grid[r][c])

    dr, dc = direction.get(grid[r][c])

    if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0]):
        if (r, c, grid[r][c]) not in visited:
            visited.add((r, c, grid[r][c]))
            grid[r + dr][c + dc] = grid[r][c]
            grid[r][c] = 'x'                        # For part 1
            return r + dr, c + dc
        else: return Status.LOOP                    # For part 2
    else: return Status.OUT

def collision(grid, r, c):
    dr, dc = direction.get(grid[r][c])

    if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0]):
        return grid[r + dr][c + dc] == '#'

def generate_variants(grid):
    variants = []

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '.':
                new_grid = [list(row) for row in grid]
                new_grid[r][c] = '#'
                variants.append(new_grid)

    return variants

def simulate_variant(grid):
    visited = set()
    guard = next((r, row.index('^')) for r, row in enumerate(grid) if '^' in row)

    while guard not in [Status.OUT, Status.LOOP]:
        guard = move_guard(grid, guard, visited)

    return guard == Status.LOOP


if __name__ == "__main__":
    solution = Day6Solution(day=6, example=None)
    solution.run(part=1)
    solution.run(part=2)

