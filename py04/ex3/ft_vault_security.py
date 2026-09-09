#!/usr/bin/python3


def secure_archive(
    file_name: str,
    action: str = "read",
    content: str = "",
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(file_name, "r") as file:
                return True, file.read()
        if action == "write":
            with open(file_name, "w") as file:
                file.write(content)
            return True, content
        return False, f"Unsupported action: {action}"
    except OSError as error:
        return False, str(error)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")

    regular_file: tuple[bool, str] = secure_archive("ft_vault_security.py")
    print(f"Using secure_archive to read a regular file: {regular_file}")

    missing_file: tuple[bool, str] = secure_archive("missing_file.txt")
    print(f"Using secure_archive to read a nonexistent file: {missing_file}")

    new_content: str = "Digital preservation protocols established.\n"
    written_file: tuple[bool, str] = secure_archive(
        "new_archive.txt", "write", new_content
    )
    print(f"Using secure_archive to write a new file: {written_file}")
