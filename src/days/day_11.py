from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from functools import reduce
from operator import mul
from typing import Callable, List

NUM_CHECK_ROUNDS = 20


@dataclass
class MonkeyTest:
    divisor: int
    true_recipient: int = None
    false_recipient: int = None

    def execute(self, worry_level: int) -> int:
        return self.true_recipient if worry_level % self.divisor == 0 else self.false_recipient


@dataclass
class Monkey:
    starting_items: List[int] = field(default_factory=list)
    operation: Operation = None
    test: MonkeyTest = None


@dataclass
class OperatorWrapper:
    char: str
    func: Callable[[int, int], int]


class Operator(Enum):
    ADD = OperatorWrapper("+", lambda op_1, op_2: op_1 + op_2)
    MULTIPLY = OperatorWrapper("*", lambda op_1, op_2: op_1 * op_2)

    @staticmethod
    def from_char(char: str) -> Operator:
        for op in Operator:
            if op.value.char == char:
                return op


class Operation:
    def __init__(self, operator: Operator, operand: int = None) -> None:
        self._operand = operand
        self._operator = operator

    def execute(self, old: int) -> int:
        if self._operand is None:
            return self._operator.value.func(old, old)
        else:
            return self._operator.value.func(old, self._operand)


def parse_monkeys(input_path):
    monkeys: List[Monkey] = []
    with open(input_path, mode="r") as fp:
        lines = fp.readlines()
        new_monkey: Monkey = None
        for line in lines:
            line = line.strip(" \n")
            if line.startswith("Monkey"):
                if new_monkey is not None:
                    monkeys.append(new_monkey)
                new_monkey = Monkey()
            if new_monkey is not None:
                if line.startswith("Starting items"):
                    new_monkey.starting_items = [int(char) for char in line.split(":")[-1].strip(" \n").split(", ")]
                elif line.startswith("Operation"):
                    operation_string: str = line.split(":")[-1].split("= old")[-1].strip(" \n")
                    operand = operation_string.split(" ")[-1]
                    if operand == "old":
                        operand = None
                    else:
                        operand = int(operand)
                    new_monkey.operation = Operation(Operator.from_char(operation_string[0]), operand)
                elif line.startswith("Test"):
                    divisible_by = int(line.split(":")[-1].split("divisible by ")[-1].strip(" \n"))
                    monkey_test = MonkeyTest(divisible_by)
                    new_monkey.test = monkey_test
                elif line.startswith("If true"):
                    new_monkey.test.true_recipient = int(line.split(":")[-1].split(" throw to monkey ")[-1].strip(" \n"))
                elif line.startswith("If false"):
                    new_monkey.test.false_recipient = int(line.split(":")[-1].split(" throw to monkey ")[-1].strip(" \n"))
        if new_monkey is not None:
            monkeys.append(new_monkey)
    return monkeys


def do_inspection_rounds(monkeys: List[Monkey], num_rounds: int, worry_level_function: Callable[[int], int]):
    monkey_inspection_map = {}
    for _ in range(num_rounds):
        for monkey_idx, monkey in enumerate(monkeys):
            if monkey_idx not in monkey_inspection_map:
                monkey_inspection_map[monkey_idx] = 0
            while len(monkey.starting_items) > 0:
                item = monkey.starting_items.pop(0)
                monkey_inspection_map[monkey_idx] += 1
                item = monkey.operation.execute(item)
                item = worry_level_function(item)
                monkeys[monkey.test.execute(item)].starting_items.append(item)

    return monkey_inspection_map


def solve_part_1(input_path: str):
    NUM_INSPECTION_ROUNDS = 20
    monkeys = parse_monkeys(input_path)
    monkey_inspection_map = do_inspection_rounds(monkeys, NUM_INSPECTION_ROUNDS, lambda val: int(val / 3))
    top_two_monkeys = sorted(list(monkey_inspection_map.items()), key=lambda x: x[1], reverse=True)[0:2]
    level_of_monkey_business = top_two_monkeys[0][1] * top_two_monkeys[1][1]
    return level_of_monkey_business


def solve_part_2(input_path: str):
    NUM_INSPECTION_ROUNDS = 10000
    monkeys = parse_monkeys(input_path)
    common_multiple = reduce(mul, [monkey.test.divisor for monkey in monkeys])
    monkey_inspection_map = do_inspection_rounds(monkeys, NUM_INSPECTION_ROUNDS, lambda val: val % common_multiple)
    top_two_monkeys = sorted(list(monkey_inspection_map.items()), key=lambda x: x[1], reverse=True)[0:2]
    level_of_monkey_business = top_two_monkeys[0][1] * top_two_monkeys[1][1]
    return level_of_monkey_business
