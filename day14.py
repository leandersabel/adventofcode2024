# https://adventofcode.com/2024/day/14
from collections import defaultdict

import math

import utils
import numpy as np
from solution import Solution

class Day14Solution(Solution):

    def parse_input(self):
        digit_groups = [utils.get_signed_digits(l) for l in self.input_data.splitlines()]
        return [[np.array(d[0:2]), np.array(d[2:4])] for d in digit_groups]

    def solve_part1(self):
        size, time = (101, 103), 100
        quads = defaultdict(int)

        for point, vector in self.parsed_input:
            new_point = teleport(point + vector * time, size)
            quad = get_quadrant(new_point, size)
            if quad:  # Ignores points on the border
                quads[quad] += 1

        return math.prod(x for x in quads.values())

    def solve_part2(self):
        size, tick = (101, 103), 0
        robots, grid = self.parsed_input, defaultdict(int)

        while collisions(grid):
            tick += 1
            moved_robots, grid = [], defaultdict(int)

            for point, vector in robots:
                new_point = teleport(point + vector, size)
                moved_robots.append([new_point, vector])
                grid[new_point] += 1

            robots = moved_robots

        return tick

def teleport(point, size):
    return point[0] % size[0], point[1] % size[1]

def get_quadrant(point, size):
    x_border, y_border = size[0] // 2, size[1] // 2
    return (1 if point[0] < x_border and point[1] < y_border else
            2 if point[0] > x_border and point[1] < y_border else
            3 if point[0] < x_border and point[1] > y_border else
            4 if point[0] > x_border and point[1] > y_border else None)

def collisions(grid):
    return len(grid) == 0 or not all(value < 2 for value in grid.values())

if __name__ == "__main__":
    solution = Day14Solution(day=14, example=None)
    solution.run(part=1)
    solution.run(part=2)