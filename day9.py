# https://adventofcode.com/2024/day/9

from copy import copy
from solution import Solution

class Day9Solution(Solution):

    def parse_input(self):
        disk = []
        for r, record in enumerate(self.input_data):
            disk.extend([(r // 2 if r % 2 == 0 else '.')] * int(record))
        return disk


    def solve_part1(self):
        disk = copy(self.parsed_input)
        free_space = next_free(disk, 0)
        file_pointer = len(disk) - 1

        while free_space < file_pointer - 1:
            free_space = next_free(disk, free_space)
            disk[free_space], disk[file_pointer] = disk[file_pointer], '.'
            file_pointer -= 1

        return sum(f * file for f, file in enumerate(disk) if file != '.')


    def solve_part2(self):
        disk = copy(self.parsed_input)
        file = len(disk) - 1

        while file >= 0:
            length = file_length(disk, file)
            space = next_free_group(disk, length)

            if 0 < space < file:
                disk[space:space + length] = [disk[file]] * length
                disk[file - length + 1:file + 1] = ['.'] * length

            file = file - length

        return sum(f * file for f, file in enumerate(disk) if file != '.')


def next_free(disk, last_free):
    return next((i for i, x in enumerate(disk[last_free:len(disk)]) if x == '.')) + last_free


def next_free_group(disk, length):
    for i in range(len(disk) - length + 1):
        if all(x == '.' for x in disk[i:i + length]):
            return i
    return -1


def file_length(disk, start_index):
    current_value = disk[start_index]
    block_start = next((i for i in range(start_index, -1, -1) if disk[i] != current_value), -1)
    return start_index - block_start


if __name__ == "__main__":
    solution = Day9Solution(day=9, example=None)
    solution.run(part=1)
    solution.run(part=2)
