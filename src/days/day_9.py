from dataclasses import dataclass, field
from enum import Enum
from typing import List

from exc import not_implemented


class MovementDirection(Enum):
    LEFT = "L"
    UP = "U"
    RIGHT = "R"
    DOWN = "D"

    @staticmethod
    def from_string(string: str):
        for dir in MovementDirection:
            if dir.value == string:
                return dir
        return None


@dataclass
class Move:
    direction: MovementDirection
    step_size: int


def init_set(x, y):
    return lambda: set([(x, y)])


@dataclass
class Knot:
    x: int = 0
    y: int = 0
    visited: set = field(default_factory=init_set(x, y))


class Rope:
    tail: Knot = Knot()
    head: Knot = Knot()

    def __update_tail(self):
        delta_x = self.head.x - self.tail.x
        delta_y = self.head.y - self.tail.y
        abs_delta_x = abs(delta_x)
        abs_delta_y = abs(delta_y)
        if abs_delta_x > 0 and abs_delta_y > 0:
            # DIAGONAL MOVE
            if abs_delta_x > abs_delta_y:
                # MOVE NEXT TO HEAD
                self.tail.y = self.head.y
                if delta_x > 0:
                    self.tail.x += 1
                else:
                    self.tail.x -= 1
                abs_delta_x -= 1
                self.tail.visited.add((self.tail.x, self.tail.y))
            elif abs_delta_x < abs_delta_y:
                # MOVE ON TOP OR UNDER THE HEAD
                self.tail.x = self.head.x
                if delta_y > 0:
                    self.tail.y += 1
                else:
                    self.tail.y -= 1
                abs_delta_y -= 1
                self.tail.visited.add((self.tail.x, self.tail.y))

        # LATERAL MOVE
        if abs_delta_x > 0:
            if delta_x > 0:
                self.__update_knot_coord(self.tail, 1, abs_delta_x - 1)
            else:
                self.__update_knot_coord(self.tail, -1, abs_delta_x - 1)
        if abs_delta_y > 0:
            if delta_y > 0:
                self.__update_knot_coord(self.tail, 1, abs_delta_y - 1, True)
            else:
                self.__update_knot_coord(self.tail, -1, abs_delta_y - 1, True)

    def __update_knot_coord(self, knot: Knot, step: int, step_size: int, vertical=False):
        for _ in range(step_size):
            if vertical:
                knot.y += step
            else:
                knot.x += step
            knot.visited.add((knot.x, knot.y))

    def move_head(self, move: Move):
        match move.direction:
            case MovementDirection.UP:
                self.__update_knot_coord(self.head, -1, move.step_size, True)
            case MovementDirection.DOWN:
                self.__update_knot_coord(self.head, 1, move.step_size, True)
            case MovementDirection.LEFT:
                self.__update_knot_coord(self.head, -1, move.step_size, False)
            case MovementDirection.RIGHT:
                self.__update_knot_coord(self.head, 1, move.step_size, False)
        self.__update_tail()


def solve_part_1(input_path: str):
    moves: List[Move] = []
    with open(input_path, mode="r") as fp:
        lines = fp.readlines()
        for line in lines:
            dir, step = line.split(" ")
            moves.append(Move(MovementDirection.from_string(dir), int(step)))

    rope = Rope()
    for move in moves:
        rope.move_head(move)
    return len(rope.tail.visited)


@not_implemented
def solve_part_2(input_path: str):
    ...
