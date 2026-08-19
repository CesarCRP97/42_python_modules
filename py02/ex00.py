
def input_temperature(temp_str: str) -> int:
    print(f"Input data is  '{temp_str}'")
    return int(temp_str)


def test_temperature():
    try:
        temperature: int = input_temperature("25")
        print(f"Temperature is now {temperature}ºC")
        print()
        temperature = input_temperature("abc")
        print(f"Temperature is now {temperature}ºC")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
    finally:
        print()


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature()
    print("All tests completed - program didn't crash!")
