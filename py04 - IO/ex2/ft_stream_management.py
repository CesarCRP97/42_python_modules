#!/usr/bin/python3

import sys
import typing


def write_error(message: str) -> None:
    sys.stderr.write(f"[STDERR] {message}\n")


def read_archive(file_name: str) -> str | None:
    file: typing.IO[str] | None = None
    try:
        file = open(file_name, "r")
        content: str = file.read()
        return content
    except OSError as error:
        write_error(f"Error opening file '{file_name}': {error}")
    finally:
        if file is not None:
            file.close()
            print(f"File '{file_name}' closed.")
    return None


def transform_content(content: str) -> str:
    transformed: str = ""
    for line in content.splitlines():
        transformed += f"{line}#\n"
    return transformed


def get_output_file_name() -> str:
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    return sys.stdin.readline().rstrip("\n")


def save_archive(file_name: str, content: str) -> None:
    file: typing.IO[str] | None = None
    print(f"Saving data to '{file_name}'")
    try:
        file = open(file_name, "w")
        file.write(content)
        print(f"Data saved in '{file_name}'.")
    except OSError as error:
        write_error(f"Error saving file '{file_name}': {error}")
        write_error("Data not saved.")
    finally:
        if file is not None:
            file.close()


def archive_file(file_name: str) -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")
    content: str | None = read_archive(file_name)
    if content is None:
        return
    print(content, end="" if content.endswith("\n") else "\n")
    print("Transforming data:")
    transformed: str = transform_content(content)
    print(transformed, end="")
    new_file_name: str = get_output_file_name()
    if new_file_name:
        save_archive(new_file_name, transformed)
    else:
        print("Data not saved.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
    else:
        archive_file(sys.argv[1])
