from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from functools import reduce
from operator import mul
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

NUM_CHECK_ROUNDS = 20


@dataclass
class MonkeyTest:
    divisor: int
    true_recipient: Optional[int] = None
    false_recipient: Optional[int] = None

    def execute(self, worry_level: int) -> int:
        if self.true_recipient is None or self.false_recipient is None:
            raise RuntimeError(
                "Recipient was None, executable test is not fully defined!",
            )
        is_divisible = worry_level % self.divisor == 0
        return self.true_recipient if is_divisible else self.false_recipient


@dataclass
class Monkey:
    starting_items: List[int] = field(default_factory=list)
    operation: Optional[Operation] = None
    test: Optional[MonkeyTest] = None


@dataclass
class OperatorWrapper:
    char: str
    func: Callable[[int, int], int]


class Operator(Enum):
    ADD = OperatorWrapper("+", lambda op_1, op_2: op_1 + op_2)
    MULTIPLY = OperatorWrapper("*", lambda op_1, op_2: op_1 * op_2)

    @staticmethod
    def from_char(char: str) -> Optional[Operator]:
        for op in Operator:
            if op.value.char == char:
                return op
        return None


class Operation:
    def __init__(
        self,
        operator: Operator,
        operand: Optional[int] = None,
    ) -> None:
        self._operand = operand
        self._operator = operator

    def execute(self, old: int) -> int:
        if self._operand is None:
            return self._operator.value.func(old, old)
        else:
            return self._operator.value.func(old, self._operand)


def parse_monkeys(input_path: Path) -> List[Monkey]:
    monkeys: List[Monkey] = []
    with open(input_path, mode="r") as fp:
        lines = fp.readlines()
        new_monkey: Optional[Monkey] = None
        for line in lines:
            line = line.strip(" \n")
            if line.startswith("Monkey"):
                if new_monkey is not None:
                    monkeys.append(new_monkey)
                new_monkey = Monkey()
            if new_monkey is not None:
                if line.startswith("Starting items"):
                    item_chars = line.split(":")[-1].strip(" \n").split(", ")
                    new_monkey.starting_items = [int(char) for char in item_chars]
                elif line.startswith("Operation"):
                    operation_string = line.split(":")[-1]
                    operation_string = operation_string.split("= old")[-1]
                    operation_string = operation_string.strip(" \n")
                    operand = operation_string.split(" ")[-1]
                    if operand == "old":
                        operand = None
                    else:
                        operand = int(operand)
                    operator = Operator.from_char(operation_string[0])
                    if operator is not None:
                        new_monkey.operation = Operation(operator, operand)
                elif line.startswith("Test"):
                    divisible_by = line.split(":")[-1]
                    divisible_by = divisible_by.split("divisible by ")[-1]
                    divisible_by = int(divisible_by.strip(" \n"))
                    monkey_test = MonkeyTest(divisible_by)
                    new_monkey.test = monkey_test
                elif line.startswith("If true") and new_monkey.test is not None:
                    true_recipient = line.split(":")[-1]
                    true_recipient = true_recipient.split(" throw to monkey ")[-1]
                    true_recipient = int(true_recipient.strip(" \n"))
                    new_monkey.test.true_recipient = true_recipient
                elif line.startswith("If false") and new_monkey.test is not None:
                    false_recipient = line.split(":")[-1]
                    false_recipient = false_recipient.split(" throw to monkey ")[-1]
                    false_recipient = int(false_recipient.strip(" \n"))
                    new_monkey.test.false_recipient = false_recipient
        if new_monkey is not None:
            monkeys.append(new_monkey)
    return monkeys


def do_inspection_rounds(
    monkeys: List[Monkey],
    num_rounds: int,
    worry_level_function: Callable[[int], int],
) -> Dict[int, int]:
    monkey_inspection_map: Dict[int, int] = {}
    for _ in range(num_rounds):
        for monkey_idx, monkey in enumerate(monkeys):
            if monkey_idx not in monkey_inspection_map:
                monkey_inspection_map[monkey_idx] = 0
            if monkey.operation is not None and monkey.test is not None:
                while len(monkey.starting_items) > 0:
                    item = monkey.starting_items.pop(0)
                    monkey_inspection_map[monkey_idx] += 1
                    item = monkey.operation.execute(item)
                    item = worry_level_function(item)
                    monkeys[monkey.test.execute(item)].starting_items.append(item)

    return monkey_inspection_map


def solve_part_1(input_path: Optional[Path]) -> Any:
    if input_path is not None:
        NUM_INSPECTION_ROUNDS = 20
        monkeys = parse_monkeys(input_path)
        monkey_inspection_map = do_inspection_rounds(
            monkeys,
            NUM_INSPECTION_ROUNDS,
            lambda val: int(val / 3),
        )
        top_two_monkeys = sorted(
            list(monkey_inspection_map.items()),
            key=lambda x: x[1],
            reverse=True,
        )[0:2]
        level_of_monkey_business = top_two_monkeys[0][1] * top_two_monkeys[1][1]
        return level_of_monkey_business


def solve_part_2(input_path: Optional[Path]) -> Any:
    if input_path is not None:
        NUM_INSPECTION_ROUNDS = 10000
        monkeys = parse_monkeys(input_path)

        def check(monkey: Monkey) -> int:
            return monkey.test.divisor if monkey.test is not None else 1

        divisors = [check(monkey) for monkey in monkeys]
        common_multiple = reduce(mul, divisors)
        monkey_inspection_map = do_inspection_rounds(
            monkeys,
            NUM_INSPECTION_ROUNDS,
            lambda val: val % common_multiple,
        )
        top_two_monkeys = sorted(
            list(monkey_inspection_map.items()),
            key=lambda x: x[1],
            reverse=True,
        )[0:2]
        level_of_monkey_business = top_two_monkeys[0][1] * top_two_monkeys[1][1]
        return level_of_monkey_business
