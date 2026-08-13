
class Plant:
    growth_rate: float = 0.8
    DEFAULT_NAME: str = "Rose"
    DEFAULT_HEIGHT: float = 25.0
    DEFAULT_DAYS: int = 30

    class Statistics:
        def __init__(self) -> None:
            self._grow_stats: int = 0
            self._age_stats: int = 0
            self._show_stats: int = 0

        def register_grow(self) -> None:
            self._grow_stats += 1

        def register_age(self) -> None:
            self._age_stats += 1

        def register_show(self) -> None:
            self._show_stats += 1

        def display_stats(self) -> None:
            grow: str = f"{self._grow_stats} grow"
            age: str = f"{self._age_stats} age"
            show: str = f"{self._show_stats} show"
            print(f"Stats: {grow}, {age}, {show}")

    def __init__(self, name: str = DEFAULT_NAME,
                 height: float = DEFAULT_HEIGHT,
                 days: int = DEFAULT_DAYS) -> None:
        self._name: str = name
        self.set_height(height)
        self.set_days(days)
        self._statistics: Plant.Statistics = self.Statistics()

    @property
    def name(self) -> str:
        return self._name

    @property
    def height(self) -> float:
        return self._height

    @property
    def days(self) -> int:
        return self._days

    def init_stats(self) -> None:
        self._grow_stats: int = 0
        self._age_stats: int = 0
        self._show_stats: int = 0

    # Getters

    def get_name(self) -> str:
        return self.name

    def get_height(self) -> float:
        return round(self.height, 2)

    def get_days(self) -> int:
        return self.days

    def get_stats(self) -> tuple[int, int, int]:
        return self._grow_stats, self._age_stats, self._show_stats

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
    def show(self, pre_message: str = "", post_message: str = "") -> None:
        print(pre_message + self.get_printable_name() + ": " +
              self.get_printable_height() + ", " +
              self.get_printable_days() + post_message)
        self._statistics.register_show()

    def grow(self) -> None:
        self._height += self.growth_rate
        self._statistics.register_grow()

    def age(self, days=1) -> None:
        if days <= 0:
            print("Invalid quantity of days to age!!! :(")
        else:
            for i in range(days):
                self._days += 1
                self.grow()
            self._statistics.register_age()

    def display_statistics(self) -> None:
        self._statistics.display_stats()

    @staticmethod
    def more_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def create_plant(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Tree(Plant):

    class Statistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls: int = 0

        def register_shade(self) -> None:
            self._shade_calls += 1

        def display_stats(self) -> None:
            super().display_stats()
            print(f" Shade: {self._shade_calls}")

    def __init__(self, name: str,
                 height: float,
                 days: int,
                 trunk_diameter: float = 5.0) -> None:
        super().__init__(name, height, days)
        self._trunk_diameter: float = trunk_diameter
        self.init_stats()

    @property
    def trunk_diameter(self) -> float:
        return self._trunk_diameter

    def init_stats(self) -> None:
        self._shade_stats: int = 0

    def get_trunk_diameter(self) -> float:
        return round(self.trunk_diameter, 2)

    def get_stats(self) -> tuple[int, int, int, int]:
        plant_stats: tuple = super().get_stats()
        return plant_stats + (self._shade_stats,)

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.get_printable_trunk_diameter()}")

    def produce_shade(self) -> None:
        message: str = f"Tree {self.get_printable_name()}"
        h: str = self.get_printable_height()
        w: str = self.get_printable_trunk_diameter()
        message += f" now produces a shade of {h} long and {w} wide."
        self._shade_stats += 1
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

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.get_printable_harvest_season()}")
        print(f" Nutritional value: {self.get_printable_nutritional_value()}")

    def get_printable_harvest_season(self) -> str:
        return self.get_harvest_season()

    def get_printable_nutritional_value(self) -> str:
        return str(self.get_nutritional_value()) + " kcal"


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

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        print(self.get_blooming_message())

    def get_blooming_message(self) -> str:
        if (self.bloomed):
            return (f" {self.get_printable_name()}: is blooming beautifully!")
        else:
            return (f" {self.get_printable_name()} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name: str,
                 height: float,
                 days: int,
                 color: str,
                 ) -> None:
        super().__init__(name, height, days, color)
        self._seeds: int = 0

    @property
    def seeds(self) -> int:
        return self._seeds

    def bloom(self, seeds: int) -> None:
        super().bloom()
        self._seeds = seeds

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.get_printable_seeds()}")

    def get_printable_seeds(self) -> str:
        return str(self.seeds)


def show_plant_statistics(plant: Plant) -> None:
    plant.display_statistics()


def ft_garden_analytics() -> None:
    print("=== Garden Statistics ===")
    print("=== Check year-old")
    a: int = 30
    b: int = 400
    print(f"Is {str(a)} days more than a year? -> {Plant.more_than_year(a)}")
    print(f"Is {str(b)} days more than a year? -> {Plant.more_than_year(b)}")
    print()

    print("=== Flower")
    flower: Flower = Flower("Rose", 15.0, 10, "Red")
    flower.show()
    print("[statistics for Rose]")
    show_plant_statistics(flower)
    print("[asking the rose to grow and bloom]")
    flower.grow()
    flower.bloom()
    flower.show()
    print("[statistics for Rose]")
    show_plant_statistics(flower)
    print()

    print("=== Tree")
    tree: Tree = Tree("Oak", 200.0, 365, 5.0)
    tree.show()
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    print("[statistics for Oak]")
    tree.display_statistics()
    print()

    print("=== Seed")
    seed: Seed = Seed("sunflower", 5.0, 10, "Yellow")
    seed.show()
    print("[make sunflower grow, age and bloom]")
    seed.bloom(42)
    seed.age(20)
    seed.show()
    print("[statistics for Sunflower]")
    seed.display_statistics()
    print()

    print("=== Anonymous")
    anonymous: Plant = Plant.create_plant()
    anonymous.show()
    print("[statistics for Unknown plant]")
    anonymous.display_statistics()


if __name__ == "__main__":
    ft_garden_analytics()
    print("=== End of Program ===")
