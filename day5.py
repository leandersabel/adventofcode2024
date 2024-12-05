# https://adventofcode.com/2024/day/5
from collections import defaultdict, deque

import utils
from solution import Solution


class Day5Solution(Solution):

    def parse_input(self):
        r_in, o_in = self.input_data.split('\n\n')
        return [utils.get_digits(r) for r in r_in.split('\n')], [utils.get_digits(o) for o in o_in.split('\n')]

    def solve_part1(self):
        rules, orders = self.parsed_input
        graph = build_graph(rules)

        valid_orders = [order for order in orders if check_rules(order, graph)]
        return sum(valid_oder[len(valid_oder) // 2] for valid_oder in valid_orders)

    def solve_part2(self):
        rules, orders = self.parsed_input
        graph = build_graph(rules)

        invalid_orders = deque([order for order in orders if not check_rules(order, graph)])
        fixed_orders = []

        while len(invalid_orders) > 0:
            order = invalid_orders.pop()

            if check_rules(order, graph):
                fixed_orders.append(order)
            else:
                invalid_orders.append(fix_shift_right(order, graph))

        return sum(fixed_order[len(fixed_order) // 2] for fixed_order in fixed_orders)


def build_graph(rules):
    graph = defaultdict(list)
    for rule in rules:
        graph[rule[0]].append(rule[1])
    return graph


def check_rules(order, graph):
    return all(not any(page_rule in order[:p] for page_rule in graph.get(page, [])) for p, page in enumerate(order))


def fix_shift_right(order, graph):
    for p, page in enumerate(order):
        for page_rule in graph.get(page, []):
            if page_rule in order[0:p]:
                order[order.index(page)], order[order.index(page_rule, 0, p)] = page_rule, page
    return order


if __name__ == "__main__":
    solution = Day5Solution(day=5, example=None)
    solution.run(part=1)
    solution.run(part=2)
