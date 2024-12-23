# https://adventofcode.com/2024/day/10
from collections import defaultdict, namedtuple, deque

from solution import Solution

Point = namedtuple('Point', ('x', 'y'))
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

class Day10Solution(Solution):

    def parse_input(self):
        return [[int(char) for char in row] for row in self.input_data.splitlines()]

    def solve_part1(self):
        grid = self.parsed_input

        trailheads = []

        paths = defaultdict(int)

        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == 0:
                    trailheads.append(Point(x, y))

        for trailhead in trailheads:
            scouts = deque()
            scouts.append(trailhead)
            visited = set()

            while len(scouts) > 0:
                scout = scouts.pop()

                if scout not in visited:
                    visited.add(scout)
                    if grid[scout.y][scout.x] == 9:
                        paths[trailhead] += 1
                    else:
                        valid_next_steps = valid_steps(grid, scout)
                        scouts.extend(valid_next_steps)

        return sum(path for path in paths.values())


    def solve_part2(self):
        grid = self.parsed_input

        trailheads = []

        paths = defaultdict(int)

        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == 0:
                    trailheads.append(Point(x, y))

        for trailhead in trailheads:
            scouts = deque()
            scouts.append(trailhead)

            while len(scouts) > 0:
                scout = scouts.pop()

                if grid[scout.y][scout.x] == 9:
                    paths[trailhead] += 1
                else:
                    valid_next_steps = valid_steps(grid, scout)
                    scouts.extend(valid_next_steps)

        return sum(path for path in paths.values())

def valid_steps(grid, point):
    steps = [Point(point.x + dx, point.y + dy) for dx, dy in directions]
    return [step for step in steps if valid_step(grid, step, len(grid), grid[point.y][point.x])]

def valid_step(grid, point, size, height):
    return 0 <= point.x < size and 0 <= point.y < size and grid[point.y][point.x] == height + 1

if __name__ == "__main__":
    solution = Day10Solution(day=10, example=None)
    solution.run(part=1)
    solution.run(part=2)
