# https://adventofcode.com/2024/day/12
from itertools import product

from solution import Solution

from copy import deepcopy
from shapely.geometry import Polygon
from shapely.ops import unary_union

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, right, down, left

class Day12Solution(Solution):

    def parse_input(self):
        return [list(row) for row in self.input_data.splitlines()]

    def solve_part1(self):
        regions = get_regions(deepcopy(self.parsed_input))
        return sum(len(region) * get_perimeter_length(region) for region in regions)

    def solve_part2(self):
        regions = get_regions(deepcopy(self.parsed_input))

        sides = 0
        for region in regions:
            perimeter = get_perimeter(region).normalize().simplify(0.1, preserve_topology=True)
            exterior_sides = len(perimeter.exterior.coords) - 1
            interior_sides = sum(len(hole.coords) - 1 for hole in perimeter.interiors)
            sides += (exterior_sides + interior_sides )* len(region)

        return sides


def get_regions(grid):
    regions = []

    for y, x in product(range(len(grid)), range(len(grid[0]))):
        if grid[y][x] != '#':
            region = flood_fill(grid, (x, y), grid[y][x], set())
            regions.append(region)

    return regions

def flood_fill(grid, start, value, region):
    x, y = start

    if start not in region and  (0 <= x < len(grid[0]) and 0 <= y < len(grid)) and grid[y][x] == value:
        grid[y][x] = '#'
        region.add(start)
        [flood_fill(grid, (x + dx, y + dy), value, region) for dx, dy in directions]

    return region

def get_perimeter(region):
    # Convert points into 1x1 cells on the grid and merge the cells into a larger polygon
    cells = [Polygon([(x, y), (x + 1, y), (x + 1, y + 1), (x, y + 1)]) for x, y in region]
    return unary_union(cells)

def get_perimeter_length(region):
    return int(get_perimeter(region).length)

if __name__ == "__main__":
    solution = Day12Solution(day=12, example=None)
    solution.run(part=1)
    solution.run(part=2)
