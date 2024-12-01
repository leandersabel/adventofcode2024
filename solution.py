import locale
from abc import ABC, abstractmethod
import time


class Solution(ABC):
    def __init__(self, day, example=None):
        self.day = day
        self.input_data = self.read_input('' if example is None else f"_example{example}")
        self.parsed_input = self.parse_input()
        self.results = [None, None]

    @abstractmethod
    def parse_input(self):
        pass

    @abstractmethod
    def solve_part1(self):
        pass

    @abstractmethod
    def solve_part2(self):
        pass

    def read_input(self, example):
        with open(f"input/day{self.day}{example}.txt", "r") as file:
            return file.read().strip()

    def run(self, part):
        """
        Run the solver algorithm for a given part and print the results.
        :param part: 1 or 2
        :return: None
        """
        start_time = time.time()
        self.results[part-1] = getattr(self, 'solve_part' + str(part))()
        self.print_results(part, self.results[part-1], time.time() - start_time)

    def print_results(self, part, result, duration):
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        f_result = locale.format_string("%d", result, grouping=True) if str(result).isdigit() else ''

        print(f'=== Day {self.day} - Part {part} ===')
        print(f'Result:   {f_result} ({result})')
        print(f'Duration: {duration:.6f} seconds\n')

