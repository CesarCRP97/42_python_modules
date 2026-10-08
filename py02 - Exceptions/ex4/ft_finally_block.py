#!/usr/bin/python3

class GardenError(Exception):
    def __init__(self,
                 message: str = "Unknown garden error detected!!") -> None:
        self.message: str = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self,
                 message: str = "The tomato plant is wilting!") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name.capitalize() != plant_name:
        raise PlantError(f"Invalid plant name to water: {plant_name}")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system(plants: list[str]) -> None:
    try:
        print("Opening watering system")
        for n in plants:
            water_plant(n)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print()
    print("Testing valid plant...")
    test_watering_system(["Tomato", "Lettuce", "Carrots"])
    print()
    print("Testing invalid plants...")
    test_watering_system(["Tomato", "lettuce", "Carrots"])
    print("Cleanup always happens, even with errors!")
