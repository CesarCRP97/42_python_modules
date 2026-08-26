#!/usr/bin/python3

def input_temperature(temp_str: str) -> int:
    print(f"Input data is  '{temp_str}'")
    conversion: int = int(temp_str)
    if 0 <= conversion <= 40:
        print(f"Temperature is now {conversion}ºC")
        return int(conversion)
    elif conversion > 40:
        raise ValueError(f"{conversion}ºC is too hot for plants (max 40ºC)")
    else:
        raise ValueError(f"{conversion}ºC is too cold for plants (min 0ºC)")


def test_temperature() -> None:
    temperatures = ["25", "abc", "100", "-30"]

    for temp in temperatures:
        try:
            input_temperature(temp)
            print()
        except Exception as e:
            print(f"Caught input_temperature error: {e}")
            print()


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature()
    print("All tests completed - program didn't crash!")
