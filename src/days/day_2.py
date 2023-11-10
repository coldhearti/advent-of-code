from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Optional


class Points(Enum):
    DRAW = 3
    LOST = 0
    WIN = 6

    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class StrategyMap(Enum):
    LOSE = "X"
    DRAW = "Y"
    WIN = "Z"

    def get_result(self: StrategyMap, opponent_shape: ShapeMap) -> ShapeMap:
        match self:
            case StrategyMap.WIN:
                return opponent_shape.loses_against
            case StrategyMap.LOSE:
                return opponent_shape.wins_against
            case StrategyMap.DRAW:
                return opponent_shape

    @staticmethod
    def parse_strategy(char: str) -> Optional[StrategyMap]:
        for strategy in StrategyMap:
            if strategy.value == char:
                return strategy
        return None


@dataclass(init=True)
class Shape:
    opponent_char: str
    player_char: str
    score: int


class ShapeMap(Enum):
    ROCK = Shape("A", "X", Points.ROCK.value)
    PAPER = Shape("B", "Y", Points.PAPER.value)
    SCISSORS = Shape("C", "Z", Points.SCISSORS.value)

    @property
    def loses_against(self) -> ShapeMap:
        loser_map = {
            ShapeMap.ROCK: ShapeMap.PAPER,
            ShapeMap.PAPER: ShapeMap.SCISSORS,
            ShapeMap.SCISSORS: ShapeMap.ROCK,
        }
        return loser_map[self]

    @property
    def wins_against(self) -> ShapeMap:
        winner_map = {
            ShapeMap.ROCK: ShapeMap.SCISSORS,
            ShapeMap.PAPER: ShapeMap.ROCK,
            ShapeMap.SCISSORS: ShapeMap.PAPER,
        }
        return winner_map[self]

    @staticmethod
    def parse_shape(char: str) -> Optional[ShapeMap]:
        for shape in ShapeMap:
            if char in [shape.value.player_char, shape.value.opponent_char]:
                return shape
        return None

    def get_result(self: ShapeMap, opponent_shape: ShapeMap) -> int:
        match self.name:
            case opponent_shape.name:
                return Points.DRAW.value + self.value.score
            case opponent_shape.loses_against.name:
                return Points.WIN.value + self.value.score
            case _:
                return Points.LOST.value + self.value.score


def solve_part_1(input_path: Optional[Path]) -> Any:
    if input_path is not None:
        score = 0
        with open(input_path, mode="r") as fp:
            lines = fp.readlines()
            for line in lines:
                line = line.rstrip("\n")
                opponent, player = line.split(" ")
                opponent = ShapeMap.parse_shape(opponent)
                player = ShapeMap.parse_shape(player)
                if player is not None and opponent is not None:
                    score += player.get_result(opponent)
        return score


def solve_part_2(input_path: Optional[Path]) -> Any:
    if input_path is not None:
        score = 0
        with open(input_path, mode="r") as fp:
            lines = fp.readlines()
            for line in lines:
                line = line.rstrip("\n")
                opponent, player = line.split(" ")
                opponent = ShapeMap.parse_shape(opponent)
                if opponent is not None:
                    strategy = StrategyMap.parse_strategy(player)
                    if strategy is not None:
                        player = strategy.get_result(opponent)
                        score += player.get_result(opponent)
        return score
