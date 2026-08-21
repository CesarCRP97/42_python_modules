
def input_temperature(temp_str: str) -> int:
    print(f"Input data is  '{temp_str}'")
    conversion: int = int(temp_str)
    print(f"Temperature is now {conversion}ºC")
    return int(conversion)


def test_temperature():
    try:
        input_temperature("25")
        print()
        input_temperature("abc")

    except Exception as e:
        print(f"Caught input_temperature error: {e}")
        print()


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature()
    print("All tests completed - program didn't crash!")
