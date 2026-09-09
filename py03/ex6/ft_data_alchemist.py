#!/usr/bin/python3

import random

name_list: list[str] = [
    "julito", "segismundo", "aparicio", "nicasio",
    "Recaredo", "Roberto", "Nicolás", "héctor", "ClaRiCIO"
]


def ft_data_alchemist() -> None:
    capitalized_names: list[str] = [name.capitalize() for name in name_list]
    only_capitalized_names: list[str] = [name for name in name_list
                                    if name == name.capitalize()]
    scoreboard: dict[str, int] = {name: random.randint(0,1000)
                                           for name in capitalized_names}
    print(f"Original list: {name_list}\n")
    print(f"new list of all capitalized names: {capitalized_names}\n")
    print(f"New list of capitalized names: {only_capitalized_names}\n")
    print(f"Score dict: {scoreboard}\n")
    try:
        average: float = sum(scoreboard.values()) / len(scoreboard)
        print(f"Average score: {round(average, 2)}\n")
        new_scores: dict[str, int] = {name: random.randint(int(average), 1000)
                                            for name in scoreboard}
        print(f"High scores: {new_scores}\n")
    except ZeroDivisionError as e:
        print("Zero elements in the list, so impossible to do a division")


if __name__ == "__main__":
    print(f"=== Inventory System Analysis ===")
    print()
    ft_data_alchemist()
    print()
    print("=== End Of Program ===")
