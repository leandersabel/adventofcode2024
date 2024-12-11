# https://adventofcode.com/2024/day/11
from collections import defaultdict
from functools import lru_cache

import utils
from solution import Solution


class Day11Solution(Solution):

    def parse_input(self):
        return list(utils.get_digits(self.input_data))

    def solve_part1(self):
        stones = self.parsed_input
        number_of_runs = 25

        for _ in range(number_of_runs):
            updated_stones = []
            for stone in stones:
                updated_stones.extend(update_stone(stone))
            stones = updated_stones
        return len(stones)

    def solve_part2(self):
        stones = defaultdict(int)
        for stone in  self.parsed_input:
            stones[stone] += 1

        number_of_runs = 75
        for _ in range(number_of_runs):
            updated_stones = defaultdict(int)

            for stone, counter in stones.items():
                for new_stone in update_stone(stone):
                    updated_stones[new_stone] += counter
            stones = updated_stones

        return sum(x for x in stones.values())


@lru_cache(maxsize=None)
def update_stone(stone):
    if stone == 0:
        return [1]

    length = len(str(stone))
    if length % 2 == 0:
        divisor = 10 ** (length // 2)
        return [stone // divisor, stone % divisor]
    else:
        return [stone * 2024]


if __name__ == "__main__":
    solution = Day11Solution(day=11, example=None)
    solution.run(part=1)
    solution.run(part=2)
