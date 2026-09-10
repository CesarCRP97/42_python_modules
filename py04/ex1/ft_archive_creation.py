#!/usr/bin/python3

import sys
import typing


def read_archive(file_name: str) -> str | None:
    file: typing.IO[str] | None = None
    try:
        file = open(file_name, "r")
        content: str = file.read()
        return content
    except OSError as error:
        print(f"Error opening file '{file_name}': {error}")
    finally:
        if file is not None:
            file.close()
            print(f"File '{file_name}' closed.")
    return None

def display_lines(content: str) -> None:
    print("---\n")
    print(content, end="" if content.endswith("\n") else "\n")
    print("\n---")

def transform_content(content: str) -> str:
    transformed: str = ""
    for line in content.splitlines():
        transformed += f"{line}#\n"
    return transformed


def save_archive(file_name: str, content: str) -> None:
    file: typing.IO[str] | None = None
    try:
        file = open(file_name, "w")
        file.write(content)
        print(f"Data saved in '{file_name}'.")
    except OSError as error:
        print(f"Error saving file '{file_name}': {error}")
    finally:
        if file is not None:
            file.close()


def ft_archive_creation(file_name: str) -> None:
    print(f"Accessing file '{file_name}'")
    content: str | None = read_archive(file_name)
    if content is None:
        return
    display_lines(content)
    print("Transforming data:")
    transformed: str = transform_content(content)
    display_lines(transformed)

    input_message:str = "Enter new file name (nothing to avoid saving it): "
    new_file_name: str = input(input_message)
    if new_file_name:
        save_archive(new_file_name, transformed)
    else:
        print("Not saving data.")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===\n")
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
    else:
        ft_archive_creation(sys.argv[1])
    print("=== End of Program ===")
