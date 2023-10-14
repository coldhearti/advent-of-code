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


def map_visibility(map: np.ndarray):
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
    return visible_map


def solve_part_1(input_path: str):
    map: np.ndarray
    with open(input_path, mode="r") as fp:
        map = parse_map(fp.readlines())
    visible_map = map_visibility(map)
    return visible_map.sum()


def get_coord_bound(row: np.ndarray, x, reverse=False):
    x_t = x
    val = row[x]
    step = -1
    if reverse:
        step = 1
    x_t += step
    while 0 < x_t < row.shape[0]:
        test = row[x_t]
        if test >= val:
            break
        x_t += step
    return min(row.shape[0] - 1, max(0, x_t))


def solve_part_2(input_path: str):
    map: np.ndarray
    with open(input_path, mode="r") as fp:
        map = parse_map(fp.readlines())
    map_shape = map.shape
    max_score = 0
    for y in range(map_shape[0]):
        row = map[y]
        for x in range(map_shape[1]):
            col = map.T[x]
            x_t0 = get_coord_bound(row, x)
            x_t1 = get_coord_bound(row, x, reverse=True)
            y_t0 = get_coord_bound(col, y)
            y_t1 = get_coord_bound(col, y, reverse=True)
            score = (x - x_t0) * (x_t1 - x) * (y - y_t0) * (y_t1 - y)
            if score > max_score:
                max_score = score
    return max_score
