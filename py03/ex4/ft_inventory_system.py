#!/usr/bin/python3

import sys

# todo: mirar que hay alguna cantidad que no sea 0.


def parse_arguments(arguments: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    if len(arguments) == 0:
        raise ValueError("No arguments to parse")
    for argument in arguments:
        try:
            split_result = argument.split(":", maxsplit=1)
            if len(split_result) != 2:
                raise ValueError(f"Invalid parameter '{argument}'")
            if not split_result[0] or not split_result[1]:
                raise ValueError(f"Invalid parameter '{argument}'")
            item = split_result[0]
            if item in inventory:
                raise ValueError(f"Redundant item '{item}'")
            if int(split_result[1]) < 0:
                error_message: str = "Quantity must be zero or positive,"
                error_message += "you can't have negative stuf!"
                raise ValueError(error_message)
            inventory[item] = int(split_result[1])
        except ValueError as e:
            print(e)
            continue
    return inventory


def inventory_is_empty(inventory: dict[str, int]) -> bool:
    return len(inventory) == 0


def display_inventory(inventory: dict[str, int]) -> None:
    print(f"Got inventory: {inventory}")


def display_list_items(inventory: dict[str, int]) -> None:
    print(f"Item list: {list(inventory.keys())}")


def get_item_most_abundant(inventory: dict[str, int]) -> str | None:
    most_abundant: str = ""
    max_quantity: int = -1
    if inventory_is_empty(inventory):
        print("The inventory is empty")
        return None
    else:
        for item in inventory:
            if inventory[item] > max_quantity:
                max_quantity = inventory[item]
                most_abundant = item
        return most_abundant


def get_item_least_abundant(inventory: dict[str, int]) -> str | None:
    if inventory_is_empty(inventory):
        print("The inventory is empty")
        return None
    else:
        least_abundant: str = list(inventory.keys())[0]
        min_quantity: int = inventory[least_abundant]
        for item in inventory:
            if inventory[item] < min_quantity:
                min_quantity = inventory[item]
                least_abundant = item
    return least_abundant


def get_total_items(inventory: dict[str, int]) -> int:
    total_nbr_items: int = 0
    for item in inventory:
        total_nbr_items += inventory[item]
    return total_nbr_items


def list_percentages_items(inventory: dict[str, int]) -> None:
    total_items: int = get_total_items(inventory)
    if total_items == 0:
        print("Cannot calculate percentages: total quantity is zero")
        return
    for item in inventory:
        abs_percentage: float = inventory[item] / total_items * 100
        print(f"Item {item} represents {round(abs_percentage,1)}%")


def update_inventory(inventory: dict[str, int], new_items: dict[str, int]
                     ) -> None:
    inventory.update(new_items)


def ft_inventory_system() -> None:
    list_args: list[str] = sys.argv[1:]
    try:
        inventory: dict[str, int] = parse_arguments(list_args)
        display_inventory(inventory)
        display_list_items(inventory)
        total_nbr_items: int = get_total_items(inventory)
        print(f"Total quantity of the {len(inventory)}",
              f"items: {total_nbr_items}")
        list_percentages_items(inventory)
        most: str | None = get_item_most_abundant(inventory)
        least: str | None = get_item_least_abundant(inventory)
        if most is not None and least is not None:
            print(f"Item most abundant: {most} with quantity",
                  f"{inventory[most]}")
            print(f"Item least abundant: {least}",
                  f"with quantity {inventory[least]}")
        new_items: dict[str, int] = {"javelin": 10, "elder_scrolls": 3}
        print(f"Updating inventory with {new_items}")
        update_inventory(inventory, new_items)
        display_inventory(inventory)
    except ValueError as e:
        print(f"Value Error detected: {e}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    ft_inventory_system()

    print("=== End Of Program ===")
