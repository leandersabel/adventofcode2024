# https://adventofcode.com/2024/day/2
import re

from solution import Solution


class Day2Solution(Solution):

    def parse_input(self):
        return [[int(x) for x in re.findall(r'\d+', line)] for line in self.input_data.split('\n')]

    def solve_part1(self):
        return sum(is_safe(report) for report in self.parsed_input)

    def solve_part2(self):
        safe_reports = 0

        for r, report in enumerate(self.parsed_input):
            if is_safe(report):
                safe_reports += 1
            else:
                permutations = [report[:i] + report[i + 1:] for i in range(len(report))]
                if any(is_safe(perm) for perm in permutations):
                    safe_reports += 1

        return safe_reports


def is_safe(report):
    # Calculate a sorted list of the difference between adjacent levels
    difference = sorted([b - a for a, b in zip(report, report[1:])])
    # Check level safety conditions: All in- or decreasing and always between |1| and |3|
    return difference[0] > 0 and 0 < difference[-1] <= 3 or 0 > difference[0] >= -3 and difference[-1] < 0


if __name__ == "__main__":
    solution = Day2Solution(day=2, example=None)
    solution.run(part=1)
    solution.run(part=2)
