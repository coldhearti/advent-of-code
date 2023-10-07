from dataclasses import dataclass
from typing import List


@dataclass
class Elf:
    calories: int = 0


def get_elves(inputPath):
    elves: List[Elf] = []
    with open(inputPath, mode="r") as fp:
        lines = fp.readlines()
        currElf = Elf()
        for line in lines:
            if line.startswith("\n"):
                elves.append(currElf)
                currElf = Elf()
            else:
                currElf.calories += int(line.rstrip("\n"))
        elves = sorted(elves, key=lambda elf: elf.calories)
    return elves


def solve_part_1(inputPath):
    return get_elves(inputPath)[-1].calories


def solve_part_2(inputPath):
    return sum([elf.calories for elf in get_elves(inputPath)[-3::]])
