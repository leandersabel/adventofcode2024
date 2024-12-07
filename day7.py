# https://adventofcode.com/2024/day/7
from functools import lru_cache
from multiprocessing import Pool

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

            with Pool() as pool:
                results = pool.map(evaluate_left_to_right, combinations)

            if test_value in results:
                valid_test_values += test_value

        return valid_test_values

    def solve_part2(self):
        valid_test_values = 0

        for equation in self.parsed_input:
            test_value = equation[0]
            numbers = equation[1:]

            combinations = generate_all_combinations(numbers, available_operators_part_2)

            with Pool() as pool:
                results = pool.starmap(
                    evaluate_combination, [(combination, test_value) for combination in combinations])

            if any(results):
                valid_test_values += test_value

        return valid_test_values

def generate_all_combinations(n, o):
    return ["".join(f"{num} {op} " for num, op in zip(n, ops)) + str(n[-1]) for ops in product(o, repeat=len(n) - 1)]

def evaluate_combination(combination, test_value):
    return evaluate_left_to_right(combination) == test_value

@lru_cache(maxsize=None)
def evaluate_left_to_right(expression):
    tokens = expression.split()
    result = int(tokens[0])  # Start with the first number

    for i in range(1, len(tokens), 2):
        operator = tokens[i]
        operand = int(tokens[i + 1])

        if operator == '+':
            result += operand
        elif operator == '*':
            result *= operand
        elif operator == '||':
            result = int(str(result) + str(operand))

    return result



if __name__ == "__main__":
    solution = Day7Solution(day=7, example=None)
    solution.run(part=1)
    solution.run(part=2)
