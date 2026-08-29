#!/usr/bin/python3

import math

def get_player_pos() -> tuple[int, int, int]:
	message: str = "Enter new coordinates as floats in format 'x,y,z': "

	result: tuple[float, float, float] = [0,0,0]

	user_input: list[str] = input(message).split(",")
	if len(user_input) != 3:
		print("Invalid syntax")
		result = get_player_pos()
	else:
		try:
			for i in range(len(user_input)):
				result[i] = float(user_input[i])
			print(result)
		except ValueError as e:
			print(f"Error on parameter {user_input[i]}: {e}")
	return result

def calculate_distance(coord_1: tuple[float, float, float],
					   coord_2: tuple[float, float, float]) -> float:
	x1: float = coord_1[0]
	x2: float = coord_2[0]
	y1: float = coord_1[1]
	y2: float = coord_2[1]
	z1: float = coord_1[2]
	z2: float = coord_2[2]

	return math.sqrt((x2-x1)**2 +(y2-y1)**2 + (z2-z1)**2)

def	show_coordinates(coordinates: tuple[float, float, float]) -> None:
	x: float = coordinates[0]
	y: float = coordinates[1]
	z: float = coordinates[2]
	message2: str = f"It includes: X={x}, Y={y}, Z={z}"


def ft_coordinate_system() -> None:
	print("Get a first set of coordinates")
	first_set: tuple[float, float, float] = get_player_pos()
	print(f"Got a first tuple: {first_set}")
	show_coordinates(first_set)
	distance_to_center: float = calculate_distance(first_set, (0.0, 0.0, 0.0))
	print(f"Distance to center: {distance_to_center}")
	print()

	print("Get a second set of coordinates")
	second_set: tuple[float, float, float] = get_player_pos()
	first_to_second: float = calculate_distance(first_set, second_set)
	print(f"Distance between the 2 sets of coordinates: {first_to_second}")



if __name__ == "__main__":
	print("=== Game Coordinate System ===")
	print()
	ft_coordinate_system()
	print()
	print("=== End of Program")
