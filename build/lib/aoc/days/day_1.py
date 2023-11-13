from dataclasses import dataclass
from pathlib import Path
from typing import Any, List, Optional


@dataclass
class Elf:
    calories: int = 0


def get_elves(input_path: Path) -> List[Elf]:
    elves: List[Elf] = []
    with open(input_path, mode="r") as fp:
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


def solve_part_1(input_path: Optional[Path]) -> Any:
    if input_path is not None:
        return get_elves(input_path)[-1].calories


def solve_part_2(input_path: Optional[Path]) -> Any:
    if input_path is not None:
        return sum([elf.calories for elf in get_elves(input_path)[-3::]])
