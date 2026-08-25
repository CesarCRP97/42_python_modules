#!/usr/bin/python3

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
        else:
            print(
                f"{self.get_printable_name()}: Error, height can't be negative"
            )
            print("Height update rejected")

    def set_days(self, days: int) -> None:
        if days >= 0:
            self._days = days
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

    # todo: try how many iterations makes
    def age(self, days=1) -> None:
        if days <= 0:
            print("Invalid quantity of days to age!!! :(")
        for i in range(days):
            self._days += 1
            self.grow()


class Flower(Plant):
    def __init__(self, name: str,
                 height: float,
                 days: int,
                 color: str) -> None:
        super().__init__(name, height, days)
        self._color: str = color
        self._bloomed: bool = False

    @property
    def color(self) -> str:
        return self._color

    @property
    def bloomed(self) -> bool:
        return self._bloomed

    def get_color(self) -> str:
        return self.color

    def get_bloomed(self) -> bool:
        return self.bloomed

    def bloom(self) -> None:
        self._bloomed = True

    def show(self, pre_message: str = "", post_message: str = "") -> None:
        super().show(pre_message, post_message)
        print(f" Color: {self.color}")
        print(self.get_blooming_message())

    def get_blooming_message(self) -> str:
        if (self.bloomed):
            return (f" {self.get_printable_name()}: is blooming beautifully!")
        else:
            return (f" {self.get_printable_name()} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str,
                 height: float,
                 days: int,
                 trunk_diameter: float = 5.0) -> None:
        super().__init__(name, height, days)
        self._trunk_diameter: float = trunk_diameter

    @property
    def trunk_diameter(self) -> float:
        return self._trunk_diameter

    def get_trunk_diameter(self) -> float:
        return round(self.trunk_diameter, 2)

    def show(self, pre_message: str = "", post_message: str = "") -> None:
        super().show(pre_message, post_message)
        print(f" Trunk diameter: {self.get_printable_trunk_diameter()}")

    def produce_shade(self) -> None:
        message: str = f"Tree {self.get_printable_name()}"
        h: str = self.get_printable_height()
        w: str = self.get_printable_trunk_diameter()
        message += f" now produces a shade of {h} long and {w} wide."
        print(message)

    def get_printable_trunk_diameter(self) -> str:
        return str(self.get_trunk_diameter()) + "cm"


class Vegetable(Plant):
    def __init__(self, name: str,
                 height: float,
                 days: int,
                 harvest_season: str = "September",
                 nutritional_value: int = 0) -> None:
        super().__init__(name, height, days)
        self._harvest_season: str = harvest_season
        self._nutritional_value = nutritional_value

    @property
    def harvest_season(self) -> str:
        return self._harvest_season

    @property
    def nutritional_value(self) -> int:
        return self._nutritional_value

    def get_harvest_season(self) -> str:
        return self.harvest_season.capitalize()

    def get_nutritional_value(self) -> int:
        return self.nutritional_value

    def show(self, pre_message: str = "", post_message: str = "") -> None:
        super().show(pre_message, post_message)
        print(f" Harvest season: {self.get_printable_harvest_season()}")
        print(f" Nutritional value: {self.get_printable_nutritional_value()}")

    def get_printable_harvest_season(self) -> str:
        return self.get_harvest_season()

    def get_printable_nutritional_value(self) -> str:
        return str(self.get_nutritional_value()) + " kcal"


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower: Flower = Flower("Rose", 15.0, 10, "Red")
    flower.show()
    print("[asking the rose to bloom]")
    flower.bloom()
    flower.show()
    print()

    print("=== Tree")
    tree: Tree = Tree("Oak", 200.0, 365, 5.0)
    tree.show()
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    print()

    print("=== Vegetable")
    vegetable: Vegetable = Vegetable("Tomato", 5.0, 10, "April")
    vegetable.show()
    print("[make tomato grow and age for 20 days]")
    vegetable.age(20)
    vegetable.show()


if __name__ == "__main__":
    ft_plant_types()
    print("=== End of Program ===")
