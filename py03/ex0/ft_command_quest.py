#!/usr/bin/python3
import sys

if __name__ == "__main__":
	list_args: list[str] = sys.argv[1:]
	argc: int = len(list_args)

	print(f"Program name: {sys.argv[0]}")
	for n in range(argc):
		print(f"Argument {n + 1}: {list_args[n]}")
	print(f"Total arguments: {argc + 1}")
