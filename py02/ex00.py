
def input_temperature(temp_str: str) -> int:
    if (not temp_str.isnumeric()):
        raise ValueError("The string is not numeric")
    return int(temp_str)


def test_temperature():
    

if __name__ == "__main__":
    test_temperature()
    print("=== End of Program ===")
