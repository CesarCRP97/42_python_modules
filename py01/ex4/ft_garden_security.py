
class Plant:
    growth_rate: float = 0.8
    DEFAULT_NAME: str = "Rose"
    DEFAULT_HEIGHT: float = 25.0
    DEFAULT_DAYS: int = 30

    def __init__(self, name: str = DEFAULT_NAME,
                 height: float = DEFAULT_HEIGHT,
                 days: int = DEFAULT_DAYS) -> None:
        self._name: str = name
        self.set_height(height)
        self.set_days(days)

    def show(self, pre_message: str = "", post_message: str = "") -> None:
        print(pre_message + self.get_printable_name() + ": " +
              self.get_printable_height() + ", " +
              self.get_printable_days() + post_message)

    @property
    def name(self) -> str:
        return self._name

    @property
    def height(self) -> float:
        return self._height

    @property
    def days(self) -> int:
        return self._days

    # Getters

    def get_name(self) -> str:
        return self.name

    def get_height(self) -> float:
        return round(self.height, 2)

    def get_days(self) -> int:
        return self.days

    # Setters
    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height
            print(f"Height updated: {self.get_printable_height()}")
        else:
            print(
                f"{self.get_printable_name()}: Error, height can't be negative"
            )
            print("Height update rejected")

    def set_days(self, days: int) -> None:
        if days >= 0:
            self._days = days
            print(f"Age updated: {self.get_printable_days()}")
        else:
            print(
                f"{self.get_printable_name()}: Error, age can't be negative"
            )
            print("Age update rejected")

    # String formatters
    def get_printable_name(self) -> str:
        return self.get_name().capitalize()

    def get_printable_height(self) -> str:
        return str(self.get_height()) + "cm"

    def get_printable_days(self) -> str:
        return str(self.days) + " days old"

    # Object methods
    def grow(self) -> None:
        self._height += self.growth_rate

    def age(self) -> None:
        self._days += 1


def ft_garden_security() -> None:
    plant1: Plant = Plant("Rose", 25.0, 30)

    print("=== Garden Security System ===")
    plant1.show("Plant created: ")
    print()
    plant1.set_height(-3.0)
    plant1.set_days(-4)
    print()
    plant1.show()
    print()
    plant1.set_height(35.0)
    plant1.set_days(42)
    print()
    plant1.show("Current state: ")


if __name__ == "__main__":
    ft_garden_security()
    print("=== End of Program ===")
