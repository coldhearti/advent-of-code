from typing import List
from exc import under_construction
import numpy as np


def check_visibility(row: np.ndarray):
    highest = -1
    visible = np.zeros(row.shape, dtype=bool)
    for idx, el in enumerate(row):
        if el > highest:
            highest = el
            visible[idx] = True
    return visible


def parse_map(lines):
    rows = [[int(char) for char in line.strip(" \n")] for line in lines]
    return np.array(rows, dtype=int)


def solve_part_1(input_path: str):
    map: np.ndarray
    with open(input_path, mode="r") as fp:
        map = parse_map(fp.readlines())
    visible_map = np.zeros(map.shape, dtype=bool)
    for row_idx, row in enumerate(map):
        left = check_visibility(row)
        right = np.flip(check_visibility(np.flip(row)))
        visible_map[row_idx] = np.logical_or(left, right)

    for col_idx, col in enumerate(map.T):
        left = check_visibility(col)
        right = np.flip(check_visibility(np.flip(col)))

        visible = np.logical_or(left, right)
        visible_map.T[col_idx] = np.logical_or(visible_map.T[col_idx], visible)

    return visible_map.sum()


@under_construction
def solve_part_2(input_path: str):
    map: np.ndarray
    with open(input_path, mode="r") as fp:
        map = parse_map(fp.readlines())

    map_shape = map.shape

    for y in range(map_shape[0]):
        for x in range(map_shape[1]):
            map[y, x]
