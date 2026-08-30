#!/usr/bin/python3

import random

achievements_list: list[str] = ["Crafting Genius", "World Savior",
								"Master Explores", "Collector Supreme",
								"Unmatchable", "Boss Slayer", "Unstoppable",
								"Untouchable", "Strategist", "Speed Runner",
								"Survivor", "Treasure Hunter", "First Steps",
								"Sharp Mind"]

def gen_player_achievements() -> set[str]:
	nbr_achievements: int = random.randint(0, 4)
	achievements_generated: int = 0
	player_achievements: set[str] = set()
	while achievements_generated < nbr_achievements:
		random_achievement: int = random.randint(0, len(achievements_list) - 1)
		if not achievements_list[random_achievement] in player_achievements:
			player_achievements.add(achievements_list[random_achievement])
			achievements_generated += 1
	return player_achievements

def ft_achievement_tracker() -> None:
	player1_ach: set[str] = gen_player_achievements()
	player_name1: str = "Alex"
	print(f"Player {player_name1}: {player1_ach}")
	player2_ach: set[str] = gen_player_achievements()
	player_name2: str = "Juan"
	print(f"Player {player_name2}: {player2_ach}")
	player_name3: str = "Maria"
	player3_ach: set[str] = gen_player_achievements()
	print(f"Player {player_name3}: {player3_ach}")
	player4_ach: set[str] = gen_player_achievements()
	player_name4: str = "Rosario"
	print(f"Player {player_name4}: {player4_ach}")
	print()

	#todo: mirar si para que sean comunes tiene que pertenecer a todos o solo a dos.
	common_achievements: set[str] = player1_ach.intersection(
		player2_ach.intersection(player3_ach.intersection(player4_ach)))
	print(f"Common achievements: {common_achievements}")
	print()

	unique_p1: set[str] = player1_ach.difference(
		player2_ach, player3_ach, player4_ach)
	print(f"Only {player_name1} has: {unique_p1}")

	unique_p2: set[str] = player2_ach.difference(
		player1_ach, player3_ach, player4_ach)
	print(f"Only {player_name2} has: {unique_p2}")

	unique_p3: set[str] = player3_ach.difference(
		player2_ach, player1_ach, player4_ach)
	print(f"Only {player_name3} has: {unique_p3}")

	unique_p4: set[str] = player4_ach.difference(
		player2_ach, player3_ach, player1_ach)
	print(f"Only {player_name4} has: {unique_p4}")


if __name__ == "__main__":
	print("=== Achievement Tracker System ===")
	print()
	ft_achievement_tracker()
	print()
	print("=== End of Program ===")

