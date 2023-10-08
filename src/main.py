from typing import List
from termcolor import colored
from days import (
    day_1,
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
    day_2,
    day_20,
    day_21,
    day_22,
    day_23,
    day_24,
    day_25,
    day_3,
    day_4,
    day_5,
    day_6,
    day_7,
    day_8,
    day_9,
)
from exc import NotStartedError, WorkingOnItError

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


def print_solution(msg, answer):
    print(colored(f"\n{msg}:\n\n{' '*4}{answer}", "green"))
    print(colored(f"\n{'-'*50}", "blue"))


def main():
    solutions = {
        "Day 1 part 1, Elf calorie maximum": (day_1.solve_part_1, "./inputs/day_1"),
        "Day 1 part 2, Three top elves calories": (day_1.solve_part_2, "./inputs/day_1"),
        "Day 2 part 1, Rock-Paper-Scissors score": (day_2.solve_part_1, "./inputs/day_2"),
        "Day 2 part 2, Rock-Paper-Scissors strategy score": (day_2.solve_part_2, "./inputs/day_2"),
        "Day 3 part 1, Rucksack priorities sum": (day_3.solve_part_1, "./inputs/day_3"),
        "Day 3 part 2, Group rucksack priorities sum": (day_3.solve_part_2, "./inputs/day_3"),
        "Day 4 part 1, Section assignments contained same range": (day_4.solve_part_1, "./inputs/day_4"),
        "Day 4 part 2, Section assignments overlaped": (day_4.solve_part_2, "./inputs/day_4"),
        "Day 5, ----": (day_5.solve, None),
        "Day 6, ----": (day_6.solve, None),
        "Day 7, ----": (day_7.solve, None),
        "Day 8, ----": (day_8.solve, None),
        "Day 9, ----": (day_9.solve, None),
        "Day 10, ----": (day_10.solve, None),
        "Day 11, ----": (day_11.solve, None),
        "Day 12, ----": (day_12.solve, None),
        "Day 13, ----": (day_13.solve, None),
        "Day 14, ----": (day_14.solve, None),
        "Day 15, ----": (day_15.solve, None),
        "Day 16, ----": (day_16.solve, None),
        "Day 17, ----": (day_17.solve, None),
        "Day 18, ----": (day_18.solve, None),
        "Day 19, ----": (day_19.solve, None),
        "Day 20, ----": (day_20.solve, None),
        "Day 21, ----": (day_21.solve, None),
        "Day 22, ----": (day_22.solve, None),
        "Day 23, ----": (day_23.solve, None),
        "Day 24, ----": (day_24.solve, None),
        "Day 25, ----": (day_25.solve, None),
    }

    errors: List[str] = []
    in_progress: List[str] = []
    for description, solver in solutions.items():
        try:
            print_solution(description, solver[0](*solver[1::]))
        except NotStartedError as e:
            errors.append(str(e))
        except WorkingOnItError as e:
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
