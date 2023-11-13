from __future__ import annotations

import operator
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any, List, Optional

CHECK_SIGNAL_CYCLE_IDXS = [19, 59, 99, 139, 179, 219]
ROW_UPDATE_CYCLES = 40


@dataclass(init=True)
class InstructionInstance:
    instruction: Instruction
    value: int


class Instruction(Enum):
    @dataclass(init=True)
    class Value:
        num_cycles: int
        name: str

    NO_OP = Value(1, "noop")
    ADD_X = Value(2, "addx")


def parse_program(lines: List[str]) -> List[InstructionInstance]:
    program: List[InstructionInstance] = []
    for line in lines:
        line = line.strip("\n")
        if line.startswith(Instruction.NO_OP.value.name):
            program.append(InstructionInstance(Instruction.NO_OP, 0))
        else:
            _, value = line.split(" ")
            program.append(InstructionInstance(Instruction.ADD_X, int(value)))
    return program


def solve_part_1(input_path: Optional[Path]) -> Any:
    if input_path is not None:
        program: List[InstructionInstance]
        with open(input_path, mode="r") as fp:
            lines = fp.readlines()
            program = parse_program(lines)

        signal_strength: List[int] = []
        register_x = 1
        cycles = 0
        for line in program:
            x_inc = 0
            cycle_inc = 0

            if line.instruction is Instruction.NO_OP:
                cycle_inc = line.instruction.value.num_cycles
            else:
                x_inc = line.value
                cycle_inc = line.instruction.value.num_cycles
            for _ in range(cycle_inc):
                cycles += 1
                signal_strength.append(cycles * register_x)
            register_x += x_inc
        return sum(operator.itemgetter(*CHECK_SIGNAL_CYCLE_IDXS)(signal_strength))


def solve_part_2(input_path: Optional[Path]) -> Any:
    if input_path is not None:
        program: List[InstructionInstance]
        with open(input_path, mode="r") as fp:
            lines = fp.readlines()
            program = parse_program(lines)

        register_x = 1
        cycles = 0
        rows: List[str] = []
        crt_x = 0
        curr_row: List[str] = []
        for line in program:
            x_inc = 0
            cycle_inc = 0
            if line.instruction == Instruction.NO_OP:
                cycle_inc = line.instruction.value.num_cycles
            else:
                x_inc = line.value
                cycle_inc = line.instruction.value.num_cycles
            for _ in range(cycle_inc):
                cycles += 1
                if register_x - 1 <= crt_x <= register_x + 1:
                    curr_row.append("#")
                else:
                    curr_row.append(" ")
                crt_x += 1
                if cycles % ROW_UPDATE_CYCLES == 0:
                    rows.append("".join(curr_row))
                    crt_x = 0
                    curr_row = []
            register_x += x_inc
        print_out = "\n" + "\n".join(rows)
        return print_out
