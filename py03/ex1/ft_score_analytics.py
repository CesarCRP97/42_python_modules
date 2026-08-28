#!/usr/bin/python3
import sys

def create_scores_list(list_scores: list[str]) -> list[int]:
	new_list: list[int] = []

	if len(list_scores) == 0:
		raise ValueError("No scores provided.")
	for score in list_scores:
		if not score.isnumeric():
			raise ValueError(f"Some argument is not numeric!")
		new_list.append(int(score))
	return new_list


def print_scores(scores: list[int]) -> None:
	message: str = f"Scores processed: [{scores[0]}"
	for score in scores[1:]:
		message += f", {score}"
	message += "]"
	print(message)


def scores_sumatory(scores: list[int]) -> int:
	sumatory: int = 0
	for score in scores:
		sumatory += score
	return sumatory


def scores_average(scores: list[int]) -> float:
	return scores_sumatory(scores) / len(scores)


def lowest_score(scores: list[int]) -> int:
	lowest_score: int = scores[0]
	for score in scores[1:]:
		if score < lowest_score:
			lowest_score = score
	return lowest_score


def highest_score(scores: list[int]) -> int:
	highest_score: int = scores[0]
	for score in scores[1:]:
		if score > highest_score:
			highest_score = score
	return highest_score


def score_range(scores: list[int]) -> int:
	low_score: int = lowest_score(scores)
	high_score: int = highest_score(scores)
	return (high_score - low_score)

def ft_score_analytics(list_args: list[str]) -> None:
	print("=== Player Score Analytics ===")

	scores: list[int] = create_scores_list(list_args)
	print_scores(scores)
	print(f"Total players: {len(scores)}")
	print(f"Total score: {scores_sumatory(scores)}")
	print(f"Average score: {scores_average(scores)}")
	print(f"High score: {highest_score(scores)}")
	print(f"Low score: {lowest_score(scores)}")
	print(f"Score range: {score_range(scores)}")

def format_printable_error_system_message(argv: list[str]) -> str:
	message: str = f"Usage: python3 {argv[0]} <score1> <score2> ..."
	message_optional: str = f"Usage: python3 {argv[0]} "
	for score in argv[1:]:
		message_optional += f" {score}"
	message_optional += " ..."
	return message_optional

if __name__ == "__main__":
	list_args: list[str] = sys.argv[1:]
	argc: int = len(list_args)
	try:
		ft_score_analytics(list_args)
	except ValueError as e:
		print(f"{e} {format_printable_error_system_message(sys.argv)}")
