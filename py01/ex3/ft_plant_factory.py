
class Plant:
    growth_rate: float = 0.8

    def __init__(self, name: str = "Rose",
                 height: float = 25.0,
                 days: int = 30) -> None:
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


def ft_plant_factory() -> None:
    plant1: Plant = Plant("Rose", 25.0, 30)
    plant2: Plant = Plant("Sunflower", 120.5, 60)
    plant3: Plant = Plant("Cactus", 18.0, 200)
    plant4: Plant = Plant("Tulip", 35.2, 45)
    plant5: Plant = Plant("Bamboo", 250.0, 365)

    print("=== Plant Factory Output ===")
    plant1.show()
    plant2.show()
    plant3.show()
    plant4.show()
    plant5.show()


if __name__ == "__main__":
    ft_plant_factory()
    print("=== End of Program ===")
