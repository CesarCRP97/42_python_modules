#!/usr/bin/python3

import sys

def parse_arguments(arguments: list[str]) -> dict[str, int]:
	inventory: dict[str, int] = {}
	split_result: tuple[str, int] = ()
	for argument in arguments:
		if ":" not in argument:
			print(f"Error - invalid parameter '{argument}'")
			continue
		split_result = argument.split(":", maxsplit=1)
		if split_result[0] in inventory:
			print(f"Redundant item '{split_result[0]}' - discarding")
			continue
		try:
			inventory[split_result[0]] = int(split_result[1])
		except ValueError as e:
			message: str = f"Quantity error for '{split_result[0]}': {e}"
			print(message)

	return inventory

def inventory_is_empty(inventory: dict[str, int]) -> bool:
	return len(inventory) == 0

def display_inventory(inventory: dict[str, int]) -> None:
	print(f"Got inventory: {inventory}")

def display_list_items(inventory: dict[str, int]) -> None:
	print(f"Item list: {list(inventory.keys())}")

def get_item_most_abundant(inventory: dict[str, int]) -> str:
	most_abundant: str = ""
	max_quantity: int = 0
	if inventory_is_empty(inventory):
		print("The inventory is empty")
		return None
	else:
		for item in inventory:
			if inventory[item] > max_quantity:
				max_quantity = inventory[item]
				most_abundant = item
		return most_abundant

def get_item_least_abundant(inventory: dict[str, int]) -> str:
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
	try:
		for item in inventory:
			abs_percentage: float = inventory[item] / total_items * 100
			print(f"Item {item} represents {round(abs_percentage,1)}%")
	except Exception as e:
		print(f"Error while calculating percentages: {e}")

def update_inventory(inventory: dict[str, int], new_items: dict[str, int]) -> None:
	inventory.update(new_items)

def ft_inventory_system() -> None:
	list_args: list[str] = sys.argv[1:]

	inventory: dict[str, int] = parse_arguments(list_args)
	display_inventory(inventory)
	display_list_items(inventory)
	total_nbr_items: int = get_total_items(inventory)
	print(f"Total quantity of the {len(inventory)} items: {total_nbr_items}")
	list_percentages_items(inventory)
	most: str = get_item_most_abundant(inventory)
	least: str = get_item_least_abundant(inventory)
	if most != None and least != None:
		print(f"Item most abundant: {most} with quantity {inventory[most]}")
		print(f"Item least abundant: {least} with quantity {inventory[least]}")
	new_items: dict[str, int] = {"javelin": 10, "elder_scrolls": 3}
	print(f"Updating inventory with {new_items}")
	update_inventory(inventory, new_items)
	display_inventory(inventory)

# python3 ft_inventory_system.py sword:1 potion:5 shield:2 armor:3 helmet:1 sword:2 hello key:value
if __name__ == "__main__":
	print(f"=== Inventory System Analysis ===")

	ft_inventory_system()

	print("=== End Of Program ===")
