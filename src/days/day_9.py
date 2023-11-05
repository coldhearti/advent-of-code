from dataclasses import dataclass
from enum import Enum
from typing import List


@dataclass
class DirectionArguments:
    char: str
    step_x: int
    step_y: int


class Direction(Enum):
    UP = DirectionArguments("U", 0, -1)
    DOWN = DirectionArguments("D", 0, 1)
    LEFT = DirectionArguments("L", -1, 0)
    RIGHT = DirectionArguments("R", 1, 0)

    @staticmethod
    def from_string(string: str):
        for dir in Direction:
            if dir.value.char == string:
                return dir
        return None


@dataclass
class Move:
    direction: Direction
    step_size: int


class Knot:
    def __init__(self) -> None:
        self.x: int = 0
        self.y: int = 0
        self.visited: set = set([(self.x, self.y)])

    def step_position(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y
        self.visited.add((self.x, self.y))


class RopeElement:
    def __init__(self, head: Knot = None) -> None:
        self.head = head
        if self.head is None:
            self.head = Knot()
        self.tail: Knot = Knot()

    def update_tail(self):
        delta_x = self.head.x - self.tail.x
        delta_y = self.head.y - self.tail.y

        # Limit the deltas to be in [-1, 1]
        abs_delta_x = abs(delta_x)
        if abs_delta_x > 0:
            delta_x = min(max(-1, delta_x), 1)
        abs_delta_y = abs(delta_y)
        if abs_delta_y > 0:
            delta_y = min(max(-1, delta_y), 1)

        # Diagonal move conditionals
        h_move = abs_delta_x > 0
        v_move = abs_delta_y > 0
        diag_move = abs_delta_x > 1 or abs_delta_y > 1

        if h_move and v_move and diag_move:
            # Diagonal move.
            self.tail.step_position(delta_x, delta_y)
        elif abs_delta_x >= 2:
            # Horizontal move.
            self.tail.step_position(delta_x, 0)
        elif abs_delta_y >= 2:
            # Vertical move.
            self.tail.step_position(0, delta_y)

    def move_head(self, move: Move):
        for _ in range(move.step_size):
            # Step through the move to update tail properly
            self.head.step_position(move.direction.value.step_x, move.direction.value.step_y)
            self.update_tail()


class Rope:
    def __init__(self, num_knots=10) -> None:
        self.head = Knot()
        self.elements: List[RopeElement] = [RopeElement(self.head)]
        root = self.elements[0]
        for _ in range(num_knots - 2):  # -2 to ensure correct number of initializations
            root = RopeElement(root.tail)
            self.elements.append(root)
        self.tail = self.elements[-1].tail

    def move_head(self, move: Move):
        for _ in range(move.step_size):
            # Step through the move to ensure proper tail updates
            self.head.step_position(move.direction.value.step_x, move.direction.value.step_y)
            for element in self.elements:
                element.update_tail()


def parse_moves(input_path):
    moves: List[Move] = []
    with open(input_path, mode="r") as fp:
        lines = fp.readlines()
        for line in lines:
            dir, step = line.split(" ")
            moves.append(Move(Direction.from_string(dir), int(step)))
    return moves


def solve_part_1(input_path: str):
    moves = parse_moves(input_path)
    rope = RopeElement()
    for move in moves:
        rope.move_head(move)
    return len(rope.tail.visited)


def solve_part_2(input_path: str):
    moves = parse_moves(input_path)
    rope = Rope(10)
    for move in moves:
        rope.move_head(move)

    return len(rope.tail.visited)
