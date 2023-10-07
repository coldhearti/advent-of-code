from typing import List
from exc import WORKING_ON_IT
import string


NUM_CHARS = len(string.ascii_letters)


def compartment_priorities(compartment: str) -> List[int]:
    return [string.ascii_letters.index(char) + 1 for char in compartment]


def priority_counts(priorities: List[int]):
    return [priorities.count(i) for i in range(1, NUM_CHARS + 1)]


def solve_part_1(inputPath):
    all_priority_counts = []
    with open(inputPath, mode="r") as fp:
        lines = fp.readlines()
        for line in lines:
            line = line.strip("\n")
            compartment_size = len(line) // 2
            compartment_1 = line[:compartment_size]
            compartment_2 = line[compartment_size:]
            compartment_1_priorities = compartment_priorities(compartment_1)
            compartment_2_priorities = compartment_priorities(compartment_2)
            compartment_1_priority_counts = priority_counts(compartment_1_priorities)
            compartment_2_priority_counts = priority_counts(compartment_2_priorities)
            compartment_priority_counts_sum = [
                1 if ((x[0] > 0 and x[1]) > 0) else 0 for x in zip(compartment_1_priority_counts, compartment_2_priority_counts)
            ]
            all_priority_counts.append(compartment_priority_counts_sum)

    priority_counts_sum = [sum(x) for x in zip(*all_priority_counts)]
    priority_sums = [x * (i + 1) for i, x in enumerate(priority_counts_sum) if x > 0]

    total_priority_sum = sum(priority_sums)
    # WORKING_ON_IT(__name__)
    return total_priority_sum


def solve_part_2(inputPath):
    WORKING_ON_IT(__name__)
