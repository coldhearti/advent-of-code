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

__version__ = "0.0.1"
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
        "Day 1, Elf calorie maximum": (day_1.solve_part_1, "./inputs/day_1"),
        "Day 2 part 1, Rock-Paper-Scissors score": (day_2.solve_part_1, "./inputs/day_2"),
        "Day 2 part 2, Rock-Paper-Scissors strategy score": (day_2.solve_part_2, "./inputs/day_2"),
        "Day 3, ----": (day_3.solve, None),
        "Day 4, ----": (day_4.solve, None),
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

    last_was_error = False
    for description, solver in solutions.items():
        try:
            print_solution(description, solver[0](*solver[1::]))
            last_was_error = False
            input("Next?")
        except NotStartedError as e:
            if not last_was_error:
                print(colored(f"\n{'-'*50}", "blue"))
            if last_was_error:
                print(colored(f"{e}", "red"))
            else:
                print(colored(f"\n{e}", "red"))
            last_was_error = True
        except WorkingOnItError as e:
            if not last_was_error:
                print(colored(f"\n{'-'*50}", "blue"))
            if last_was_error:
                print(colored(f"{e}", "yellow"))
            else:
                print(colored(f"\n{e}", "yellow"))
            last_was_error = True


if __name__ == "__main__":
    main()
