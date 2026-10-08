#!/usr/bin/python3
import sys


def create_scores_list(list_scores: list[str]) -> list[int]:
    new_list: list[int] = []

    if len(list_scores) == 0:
        raise ValueError("No scores provided.")
    for score in list_scores:
        if score.isnumeric():
            new_list.append(int(score))
    if len(new_list) == 0:
        raise ValueError("No valid scores!!!")
    return new_list


def print_scores(scores: list[int]) -> None:
    message: str = f"Scores processed: [{scores[0]}"
    for score in scores[1:]:
        message += f", {score}"
    message += "]"
    print(message)


def scores_average(scores: list[int]) -> float:
    return sum(scores) / len(scores)


def score_range(scores: list[int]) -> int:
    low_score: int = min(scores)
    high_score: int = max(scores)
    return (high_score - low_score)


def ft_score_analytics(list_args: list[str]) -> None:
    print("=== Player Score Analytics ===")

    scores: list[int] = create_scores_list(list_args)
    print_scores(scores)
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {scores_average(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {score_range(scores)}")


def format_printable_error_system_message(argv: list[str]) -> str:
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
