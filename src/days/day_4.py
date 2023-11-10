from pathlib import Path
from typing import Any, List, Optional, Tuple


def range_contains_range(range_1: List[int], range_2: List[int]) -> bool:
    if range_1[0] <= range_2[0] and range_1[1] >= range_2[1]:
        return True
    return False


def range_overlaps_range(range_1: List[int], range_2: List[int]) -> bool:
    check_range = range(range_2[0], range_2[1] + 1)
    if range_1[0] in check_range or range_1[1] in check_range:
        return True
    return False


def parse_sections(line: str) -> Tuple[List[int], List[int]]:
    line = line.strip("\n")
    elf_1, elf_2 = line.split(",")
    sections_1 = [int(val) for val in elf_1.split("-")]
    sections_2 = [int(val) for val in elf_2.split("-")]
    return sections_1, sections_2


def solve_part_1(input_path: Optional[Path]) -> Any:
    if input_path is not None:
        pairs_containing = 0
        with open(input_path, mode="r") as fp:
            lines = fp.readlines()
            for line in lines:
                sections_1, sections_2 = parse_sections(line)
                if range_contains_range(sections_1, sections_2) or range_contains_range(sections_2, sections_1):
                    pairs_containing += 1
        return pairs_containing


def solve_part_2(input_path: Optional[Path]) -> Any:
    if input_path is not None:
        pairs_overlapping = 0
        with open(input_path, mode="r") as fp:
            lines = fp.readlines()
            for line in lines:
                sections_1, sections_2 = parse_sections(line)
                if range_overlaps_range(sections_1, sections_2) or range_overlaps_range(sections_2, sections_1):
                    pairs_overlapping += 1
        return pairs_overlapping
