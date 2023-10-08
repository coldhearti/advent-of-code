from exc import WORKING_ON_IT


def range_contains_range(range_1, range_2):
    if range_1[0] <= range_2[0] and range_1[1] >= range_2[1]:
        return True
    return False


def range_overlaps_range(range_1, range_2):
    check_range = range(range_2[0], range_2[1] + 1)
    if range_1[0] in check_range or range_1[1] in check_range:
        return True
    return False


def parse_sections(line):
    line = line.strip("\n")
    elf_1, elf_2 = line.split(",")
    sections_1 = [int(val) for val in elf_1.split("-")]
    sections_2 = [int(val) for val in elf_2.split("-")]
    return sections_1, sections_2


def solve_part_1(inputPath):
    pairs_containing = 0
    with open(inputPath, mode="r") as fp:
        lines = fp.readlines()
        for line in lines:
            sections_1, sections_2 = parse_sections(line)
            if range_contains_range(sections_1, sections_2) or range_contains_range(sections_2, sections_1):
                pairs_containing += 1
    return pairs_containing


def solve_part_2(inputPath):
    pairs_overlapping = 0
    with open(inputPath, mode="r") as fp:
        lines = fp.readlines()
        for line in lines:
            sections_1, sections_2 = parse_sections(line)
            if range_overlaps_range(sections_1, sections_2) or range_overlaps_range(sections_2, sections_1):
                pairs_overlapping += 1
    return pairs_overlapping
