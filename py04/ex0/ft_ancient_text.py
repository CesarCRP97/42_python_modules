#!/usr/bin/python3

import sys
import typing


def recover_file(file_name: str) -> None:
    file: typing.IO[str] | None = None
    try:
        file = open(file_name, "r")
        content: str = file.read()
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{file_name}'")
        print(content, end="" if content.endswith("\n") else "\n")
    except OSError as error:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{file_name}'")
        print(f"Error opening file '{file_name}': {error}")
    finally:
        if file is not None:
            file.close()
            print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        recover_file(sys.argv[1])
