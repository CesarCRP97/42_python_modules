#!/usr/bin/python3

import sys
import typing


def recover_file(file_name: str) -> None:
    file: typing.IO[str] | None = None

    print(f"Accessing file '{file_name}'")
    try:
        file = open(file_name, "r")
        content: str = file.read()
        print(content, end="" if content.endswith("\n") else "\n")
    except OSError as error:
        print(f"Error opening file '{file_name}': {error}")
    finally:
        if file is not None:
            file.close()
            print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")

    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        recover_file(sys.argv[1])

    print("=== End of Program ===")
