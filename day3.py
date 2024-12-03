# https://adventofcode.com/2024/day/3
import math
import re

import utils
from solution import Solution


class Day3Solution(Solution):

    def parse_input(self):
        return re.findall(r'(mul\(\d+,\d+\))', self.input_data)

    def solve_part1(self):
        instructions = re.findall(r'(mul\(\d+,\d+\))', self.input_data)
        pairs = [utils.get_digits(mult) for mult in instructions]

        return sum(pair[0] * pair[1] for pair in pairs)

    def solve_part2(self):
        instructions = re.findall(r'(do\(\)|don\'t\(\)|mul\(\d+,\d+\))', self.input_data)

        val = 0
        enabled = True

        for instruction in instructions:
            if instruction == "don\'t()":
                enabled = False
            elif instruction == "do()":
                enabled = True
            elif enabled:
                val += math.prod(utils.get_digits(instruction))

        return val


if __name__ == "__main__":
    solution = Day3Solution(day=3, example=None)
    solution.run(part=1)
    solution.run(part=2)
