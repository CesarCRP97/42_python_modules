

class Plant:
    growth_rate: float = 0.8

    def __init__(self, name: str, height: float, days: int) -> None:
        self.name: str = name
        self.height: float = height
        self.days: int = days

    def show(self) -> None:
        print(self.get_printable_name() + ": " + self.get_printable_height() +
              ", " + self.get_printable_days())

    # Getters
    def get_name(self) -> str:
        return self.name

    def get_height(self) -> float:
        return round(self.height, 2)

    def get_days(self) -> int:
        return self.days

    # String formatters
    def get_printable_name(self) -> str:
        return self.get_name().capitalize()

    def get_printable_height(self) -> str:
        return str(self.get_height()) + "cm"

    def get_printable_days(self) -> str:
        return str(self.days) + " days old"

    # Object methods
    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self.days += 1


def ft_plant_growth() -> None:
    print("=== Garden Plant Growth ===")

    plant1: Plant = Plant("Rose", 25.0, 30)
    plant1.show()
    initial_height: float = plant1.get_height()
    for i in range(0, 7):
        print("=== Day", i + 1, "===")
        plant1.grow()
        plant1.age()
        plant1.show()
    height_diff_str: str = str(round(plant1.get_height() - initial_height, 2))
    print(
        f"Growth this week: {height_diff_str}cm")


if __name__ == "__main__":
    ft_plant_growth()
    print("=== End of Program ===")
