from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple

from days import (
    day_1,
    day_2,
    day_3,
    day_4,
    day_5,
    day_6,
    day_7,
    day_8,
    day_9,
    day_10,
    day_11,
    day_12,
    day_13,
    day_14,
    day_15,
    day_16,
    day_17,
    day_18,
    day_19,
    day_20,
    day_21,
    day_22,
    day_23,
    day_24,
    day_25,
)
from exc import NotImplementedError, UnderConstructionError
from termcolor import colored

__version__ = "0.0.2"
__desc__ = "Advent Of Code 2022 solutions."

art = r"""
     ___       __                 __  ____  __________          __
    /   | ____/ /   _____  ____  / /_/ __ \/ __/ ____/___  ____/ /__
   / /| |/ __  / | / / _ \/ __ \/ __/ / / / /_/ /   / __ \/ __  / _ \
  / ___ / /_/ /| |/ /  __/ / / / /_/ /_/ / __/ /___/ /_/ / /_/ /  __/
 /_/  |_\__,_/ |___/\___/_/ /_/\__/\____/_/  \____/\____/\__,_/\___/

             ______      __    ____                    __
            / ____/___  / /___/ / /_  ___  ____ ______/ /_
           / /   / __ \/ / __  / __ \/ _ \/ __ `/ ___/ __/
          / /___/ /_/ / / /_/ / / / /  __/ /_/ / /  / /_
          \____/\____/_/\__,_/_/ /_/\___/\__,_/_/   \__/

"""

print(f"{colored(art, 'blue')}")
print("Solving...")


def print_solution(msg: str, answer: Any):
    print(colored(f"\n{msg}:\n\n{' '*4}{answer}", "green"))
    print(colored(f"\n{'-'*50}", "blue"))


def main():
    solutions: Dict[str, Tuple[Callable[[Optional[Path]], Any], Optional[str]]] = {
        "Day 1 part 1, Calorie maximum": (
            day_1.solve_part_1,
            "./inputs/day_1",
        ),
        "Day 1 part 2, Three top calories": (
            day_1.solve_part_2,
            "./inputs/day_1",
        ),
        "Day 2 part 1, Rock-Paper-Scissors score": (
            day_2.solve_part_1,
            "./inputs/day_2",
        ),
        "Day 2 part 2, Rock-Paper-Scissors strategy score": (
            day_2.solve_part_2,
            "./inputs/day_2",
        ),
        "Day 3 part 1, Content priorities sum": (
            day_3.solve_part_1,
            "./inputs/day_3",
        ),
        "Day 3 part 2, Grouped content priorities sum": (
            day_3.solve_part_2,
            "./inputs/day_3",
        ),
        "Day 4 part 1, Section assignments contained same range": (
            day_4.solve_part_1,
            "./inputs/day_4",
        ),
        "Day 4 part 2, Section assignments overlaped": (
            day_4.solve_part_2,
            "./inputs/day_4",
        ),
        "Day 5 part 1, Top of stacks after moves": (
            day_5.solve_part_1,
            "./inputs/day_5",
        ),
        "Day 5 part 2, Top of stacks after combined moves": (
            day_5.solve_part_2,
            "./inputs/day_5",
        ),
        "Day 6 part 1, Characters processed before first start-of-packet": (
            day_6.solve_part_1,
            "./inputs/day_6",
        ),
        "Day 6 part 2, Characters processed before first start-of-message": (
            day_6.solve_part_2,
            "./inputs/day_6",
        ),
        "Day 7 part 1, Directory sizes total": (
            day_7.solve_part_1,
            "./inputs/day_7",
        ),
        "Day 7 part 2, Smallest directory of required size": (
            day_7.solve_part_2,
            "./inputs/day_7",
        ),
        "Day 8 part 1, Number of visible trees": (
            day_8.solve_part_1,
            "./inputs/day_8",
        ),
        "Day 8 part 2, Highest possible scenic score": (
            day_8.solve_part_2,
            "./inputs/day_8",
        ),
        "Day 9 part 1, Number of positions the rope tail visited": (
            day_9.solve_part_1,
            "./inputs/day_9",
        ),
        "Day 9 part 2, Number of positions the rope tail visited": (
            day_9.solve_part_2,
            "./inputs/day_9",
        ),
        "Day 10 part 1, Sum of signal strengths": (
            day_10.solve_part_1,
            "./inputs/day_10",
        ),
        "Day 10 part 2, Drawn image": (
            day_10.solve_part_2,
            "./inputs/day_10",
        ),
        "Day 11 part 1, Level of monkey business after 20 rounds": (
            day_11.solve_part_1,
            "./inputs/day_11",
        ),
        "Day 11 part 2, Level of monkey business after 10 000 rounds": (
            day_11.solve_part_2,
            "./inputs/day_11",
        ),
        "Day 12 part 1, ----": (
            day_12.solve_part_1,
            None,
        ),
        "Day 12 part 2, ----": (
            day_12.solve_part_2,
            None,
        ),
        "Day 13 part 1, ----": (
            day_13.solve_part_1,
            None,
        ),
        "Day 13 part 2, ----": (
            day_13.solve_part_2,
            None,
        ),
        "Day 14 part 1, ----": (
            day_14.solve_part_1,
            None,
        ),
        "Day 14 part 2, ----": (
            day_14.solve_part_2,
            None,
        ),
        "Day 15 part 1, ----": (
            day_15.solve_part_1,
            None,
        ),
        "Day 15 part 2, ----": (
            day_15.solve_part_2,
            None,
        ),
        "Day 16 part 1, ----": (
            day_16.solve_part_1,
            None,
        ),
        "Day 16 part 2, ----": (
            day_16.solve_part_2,
            None,
        ),
        "Day 17 part 1, ----": (
            day_17.solve_part_1,
            None,
        ),
        "Day 17 part 2, ----": (
            day_17.solve_part_2,
            None,
        ),
        "Day 18 part 1, ----": (
            day_18.solve_part_1,
            None,
        ),
        "Day 18 part 2, ----": (
            day_18.solve_part_2,
            None,
        ),
        "Day 19 part 1, ----": (
            day_19.solve_part_1,
            None,
        ),
        "Day 19 part 2, ----": (
            day_19.solve_part_2,
            None,
        ),
        "Day 20 part 1, ----": (
            day_20.solve_part_1,
            None,
        ),
        "Day 20 part 2, ----": (
            day_20.solve_part_2,
            None,
        ),
        "Day 21 part 1, ----": (
            day_21.solve_part_1,
            None,
        ),
        "Day 21 part 2, ----": (
            day_21.solve_part_2,
            None,
        ),
        "Day 22 part 1, ----": (
            day_22.solve_part_1,
            None,
        ),
        "Day 22 part 2, ----": (
            day_22.solve_part_2,
            None,
        ),
        "Day 23 part 1, ----": (
            day_23.solve_part_1,
            None,
        ),
        "Day 23 part 2, ----": (
            day_23.solve_part_2,
            None,
        ),
        "Day 24 part 1, ----": (
            day_24.solve_part_1,
            None,
        ),
        "Day 24 part 2, ----": (
            day_24.solve_part_2,
            None,
        ),
        "Day 25 part 1, ----": (
            day_25.solve_part_1,
            None,
        ),
        "Day 25 part 2, ----": (
            day_25.solve_part_2,
            None,
        ),
    }

    errors: List[str] = []
    in_progress: List[str] = []
    for description, solver in solutions.items():
        try:
            if solver[1] is not None:
                input_path = Path(solver[1])
                print_solution(description, solver[0](input_path))
            else:
                print_solution(description, solver[0](None))
        except NotImplementedError as e:
            errors.append(str(e))
        except UnderConstructionError as e:
            in_progress.append(str(e))

    errors[::4] = [f"\n{err}" for err in errors[::4]]
    in_progress[::4] = [f"\n{prog}" for prog in in_progress[::4]]
    if len(in_progress) > 0:
        print(colored(f"Under construction:{', '.join(in_progress)}", "yellow"))
    if len(errors) > 0:
        print(colored(f"Not implemented yet:{', '.join(errors)}", "red"))

    prog_string = f"Total Progress: {round(100*(-len(in_progress) - len(errors) + len(solutions)) / len(solutions), 3)} %"

    print(f"\n{prog_string}")


if __name__ == "__main__":
    main()
