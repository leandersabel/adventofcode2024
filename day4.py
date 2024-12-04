# https://adventofcode.com/2024/day/4
import re

import numpy as np

from solution import Solution


class Day4Solution(Solution):

    def parse_input(self):
        return [list(row) for row in self.input_data.split('\n')]

    def solve_part1(self):
        grid = self.parsed_input
        result = 0

        result += sum(count(row) for row in grid)                               # Horizontal
        result += sum(count(row) for row in np.rot90(grid))                     # Vertical
        result += sum(count(row) for row in vertical_slices(grid))              # Down-Right
        result += sum(count(row) for row in vertical_slices(np.fliplr(grid)))   # Down-Left

        return result

    def solve_part2(self):
        grid = self.parsed_input
        result = 0

        # Iterate over every possible center point in the grid
        for r in range(1, len(grid) - 1):
            for c in range(1, len(grid) - 1):
                dr = grid[r - 1][c - 1] + grid[r][c] + grid[r + 1][c + 1]
                dl = grid[r - 1][c + 1] + grid[r][c] + grid[r + 1][c - 1]

                if ('MAS' in dr or 'SAM' in dr) and ('MAS' in dl or 'SAM' in dl):
                    result += 1

        return result


def count(line):
    return ''.join(line).count('XMAS') + ''.join(line).count('SAMX')


def vertical_slices(grid):
    slices = []
    size = len(grid)

    for c in range(size - 1, 0, -1):  # Start from first row, varying column
        slices.append(''.join(grid[r][c + r] for r in range(size - c)))

    for r in range(size):  # Start from first column, varying row
        slices.append(''.join(grid[r + c][c] for c in range(size - r)))

    return slices


if __name__ == "__main__":
    solution = Day4Solution(day=4, example=None)
    solution.run(part=1)
    solution.run(part=2)
