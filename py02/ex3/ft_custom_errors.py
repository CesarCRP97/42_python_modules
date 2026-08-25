#!/usr/bin/python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error detected!!"):
        self.message: str = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message: str = "The tomato plant is wilting!"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Not enough water in the tank!"):
        super().__init__(message)


def ft_custom_errors() -> None:
    print()
    try:
        print("Testing PlantError...")
        raise PlantError()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print()
    try:
        print("Testing WaterError...")
        raise WaterError()
    except WaterError as e:
        print(f"Caught PlantError: {e}")
        print()
    print("Testing catching all garden errors...")
    try:
        raise PlantError()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        raise WaterError()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    ft_custom_errors()
