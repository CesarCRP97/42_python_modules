#!/usr/bin/python3

def garden_operations(operation_number: int) -> int:
    match operation_number:
        case 0:
            return int("abc")
        case 1:
            return int(2 / 0)
        case 2:
            open("ajsdklja.txt")
        case 3:
            return len(42)
    return 1


def test_error_types():
    for n in range(0, 5):
        try:
            print(f"Correct result : {garden_operations(n)}!!!!")

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
    print("=== End of Program ===")
