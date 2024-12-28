# https://adventofcode.com/2024/day/13
import math

import utils
from solution import Solution
from sympy import symbols, Eq, solve


class Day13Solution(Solution):

    def parse_input(self):
        return [utils.get_digits(m) for m in  self.input_data.split('\n\n')]

    def solve_part1(self):
        tokens = 0

        for machine in self.parsed_input:
            ax, ay, bx, by, x, y = machine
            tokens += solve_linear_equation_in_tokens(ax, ay, bx, by, x, y)

        return tokens

    def solve_part2(self):
        tokens = 0

        for machine in self.parsed_input:
            ax, ay, bx, by, x, y = machine
            x, y = x + 10000000000000, y + 10000000000000

            tokens += solve_linear_equation_in_tokens(ax, ay, bx, by, x, y)

        return tokens

def solve_linear_equation_in_tokens(ax, ay, bx, by, x, y):
    a, b = symbols('a b', intger=True)
    solutions = solve((Eq(ax * a + bx * b, x), Eq(ay * a + by * b, y)), (a, b), dict=True)

    # Filter out non-integer solutions
    valid = [sol for sol in solutions if sol[a].is_Integer and sol[b].is_Integer]

    # Calculate the price in tokens
    return min(v[a] * 3 + v[b] for v in valid) if valid else 0

if __name__ == "__main__":
    solution = Day13Solution(day=13, example=None)
    solution.run(part=1)
    solution.run(part=2)
