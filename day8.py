# https://adventofcode.com/2024/day/8
from collections import namedtuple, defaultdict
from itertools import combinations

import numpy as np

from solution import Solution

Point = namedtuple('Point', ('x', 'y'))

class Day8Solution(Solution):

    def parse_input(self):
        grid = [list(line) for line in self.input_data.splitlines()]
        antennas = defaultdict(list)

        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val != '.':
                    antennas[val].append(Point(x, y))

        return antennas, len(grid)

    def solve_part1(self):
        antennas, size = self.parsed_input

        antinodes = set()
        for antennas_of_type in antennas.values():
            for p1, p2 in combinations(antennas_of_type, 2):
                for point in extend_points(p1, p2):
                    if 0 <= point.x < size and 0 <= point.y < size:
                        antinodes.add(point)

        return len(antinodes)

    def solve_part2(self):
        antennas, size = self.parsed_input

        antinodes = set()
        for antennas_of_type in antennas.values():
            for p1, p2 in combinations(antennas_of_type, 2):
                for point in extend_line(p1, p2, size):
                    if 0 <= point.x < size and 0 <= point.y < size:
                        antinodes.add(point)

        return len(antinodes)

def extend_points(p1, p2, scale = 1):
    direction = np.array([p2.x - p1.x, p2.y - p1.y])
    ext_p1 = np.array([p1.x, p1.y]) - direction * scale
    ext_p2 = np.array([p2.x, p2.y]) + direction * scale
    return [Point(int(ext_p1[0]), int(ext_p1[1])), Point(int(ext_p2[0]), int(ext_p2[1]))]

def extend_line(p1, p2, size):
    direction = np.array([p2.x - p1.x, p2.y - p1.y])
    gcd = abs(np.gcd(direction[0], direction[1]))  # Simplify direction vector
    step = direction // gcd  # Integer steps in x and y
    points = set()

    for sign in (-1, 1):
        current = np.array([p1.x, p1.y])
        while abs(current[0]) <= size and abs(current[1]) <= size:
            points.add(Point(int(current[0]), int(current[1])))
            current += sign * step

    return points

if __name__ == "__main__":
    solution = Day8Solution(day=8, example=None)
    solution.run(part=1)
    solution.run(part=2)