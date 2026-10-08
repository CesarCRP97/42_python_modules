#!/usr/bin/python3

def garden_operations(operation_number: int) -> int:
    match operation_number:
        case 0:
            return int("abc")
        case 1:
            return int(2 / 0)
        case 2:
            open("/non/existent/file")
        case 3:
            "gola caracola" + 1
    return 1


def test_error_types() -> None:
    for n in range(0, 5):
        try:
            print(f"Testing operation {n}...")
            garden_operations(n)
            print("Operation completed succesfully")

        except ValueError as e:
            print(f"Catched a Value error: {e}")
        except ZeroDivisionError as e:
            print(f"Catched a Zero Division Error: {e}")
        except FileNotFoundError as e:
            print(f"Catched a File not Found Error: {e}")
        except TypeError as e:
            print(f"Catched a Type Error: {e}")
        except Exception as e:
            print(f"Catched an Unknown Exception: {e}")


if __name__ == "__main__":
    print("=== Testing Differents Errors ===")
    test_error_types()
    print()
    print("All error types tested successfully!")
