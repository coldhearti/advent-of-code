from typing import List
from exc import WORKING_ON_IT
import string


NUM_CHARS = len(string.ascii_letters)


def container_priorities(compartment: str) -> List[int]:
    return [string.ascii_letters.index(char) + 1 for char in compartment]


def priority_counts(priorities: List[int]) -> List[int]:
    return [priorities.count(i) for i in range(1, NUM_CHARS + 1)]


def find_shared_priorities(*containers) -> List[bool]:
    priorities = [container_priorities(container) for container in containers]
    counts = [priority_counts(priority) for priority in priorities]
    return [all([val > 0 for val in x]) for x in zip(*counts)]


def shared_priorities_sum(*shared_priorities: List[bool]) -> List[int]:
    shared_priorities_count = [sum(x) for x in zip(*shared_priorities)]
    return [x * (i + 1) for i, x in enumerate(shared_priorities_count) if x > 0]


def solve_part_1(inputPath):
    all_shared_priorities = []
    with open(inputPath, mode="r") as fp:
        lines = fp.readlines()
        for line in lines:
            line = line.strip("\n")
            compartment_size = len(line) // 2
            compartment_1 = line[:compartment_size]
            compartment_2 = line[compartment_size:]
            all_shared_priorities.append(find_shared_priorities(compartment_1, compartment_2))
    priority_sums = shared_priorities_sum(*all_shared_priorities)
    total_priority_sum = sum(priority_sums)
    # WORKING_ON_IT(__name__)
    return total_priority_sum


def solve_part_2(inputPath):
    all_group_shared_priorities = []
    with open(inputPath, mode="r") as fp:
        lines = fp.readlines()
        for i in range(0, len(lines), 3):
            line_group = lines[i : i + 3]
            line_group = [line.strip("\n") for line in line_group]
            all_group_shared_priorities.append(find_shared_priorities(*line_group))

        # for line_group in:
        #     print(f"Group: {line_group}")
    priority_sums = shared_priorities_sum(*all_group_shared_priorities)
    total_priority_sum = sum(priority_sums)
    return total_priority_sum
