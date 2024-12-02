# https://adventofcode.com/2024/day/1

import utils
from solution import Solution


class Day1Solution(Solution):

    def parse_input(self):
        numbers = utils.get_digits(self.input_data)
        return [sorted(numbers[0::2]), sorted(numbers[1::2])]

    def solve_part1(self):
        l1, l2 = self.parsed_input
        return sum(abs(n1 - n2) for n1, n2 in zip(l1, l2))

    def solve_part2(self):
        l1, l2 = self.parsed_input
        return sum(n * l2.count(n) for n in l1)


if __name__ == "__main__":
    solution = Day1Solution(day=1, example=None)
    solution.run(part=1)
    solution.run(part=2)
