
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(self.get_printable_name() + ": " + self.get_printable_height() +
              ", " + self.get_printable_age())

    def get_printable_name(self) -> str:
        return self.name.capitalize()

    def get_printable_height(self) -> str:
        return str(self.height) + "cm"

    def get_printable_age(self) -> str:
        return str(self.age) + " days old"


def ft_garden_data() -> None:
    plant1: Plant = Plant("Rose", 25, 30)
    plant2: Plant = Plant("Sunflower", 80, 45)
    plant3: Plant = Plant("Cactus", 15, 120)

    print("=== Welcome to My Garden ===")
    plant1.show()
    plant2.show()
    plant3.show()


if __name__ == "__main__":
    ft_garden_data()
    print("=== End of Program ===")
