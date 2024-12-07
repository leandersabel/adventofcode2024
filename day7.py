# https://adventofcode.com/2024/day/7
from itertools import product

import utils
from solution import Solution

available_operators_part_1 = ['+', '*']
available_operators_part_2 = ['+', '*', '||']

class Day7Solution(Solution):

    def parse_input(self):
        return [utils.get_digits(line) for line in self.input_data.splitlines()]

    def solve_part1(self):
        valid_test_values = 0

        for equation in self.parsed_input:
            test_value = equation[0]
            numbers = equation[1:]

            combinations = generate_all_combinations(numbers, available_operators_part_1)

            if any(evaluate_left_to_right(combination) == test_value for combination in combinations):
                valid_test_values += test_value

        return valid_test_values

    def solve_part2(self):
        valid_test_values = 0

        for equation in self.parsed_input:
            test_value = equation[0]
            numbers = equation[1:]

            combinations = generate_all_combinations(numbers, available_operators_part_2)

            if any(evaluate_left_to_right(combination) == test_value for combination in combinations):
                valid_test_values += test_value

        return valid_test_values

def generate_all_combinations(n, o):
    return ["".join(f"{num} {op} " for num, op in zip(n, ops)) + str(n[-1]) for ops in product(o, repeat=len(n) - 1)]

def evaluate_left_to_right(expression):
    tokens = expression.split()
    result = int(tokens[0])

    for i in range(1, len(tokens), 2):
        operator = '' if tokens[i] == '||' else f" {tokens[i]} "  # For part II
        result = eval(f"{result}{operator}{tokens[i + 1]}")
    return result


if __name__ == "__main__":
    solution = Day7Solution(day=7, example=1)
    solution.run(part=1)
    solution.run(part=2)
