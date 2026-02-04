"""
This module defines a simple garden plant registry.

It demonstrates the use of a Plant class and prints
information about several plants when executed directly.
"""


class Plant:
    """
    Represents a plant with basic attributes.

    Attributes:
        name (str): The name of the plant.
        hight (int): The height of the plant in centimeters.
        age (int): The age of the plant in days.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initializes a Plant instance.

        Args:
            name (str): The name of the plant.
            hight (int): The height of the plant in centimeters.
            age (int): The age of the plant in days.
        """
        self.name = name
        self.hight = height
        self.age = age

    def print_plant(self) -> None:
        """
        Prints formatted information about the plant.

        Output format:
            <name>: <height>cm, <age> days old
        """
        print(f"{self.name}: {self.hight}cm, {self.age} days old")


def ft_garden_data() -> None:
    """
    Prints a registry of plants in the garden.

    Creates several Plant objects and prints their
    information to the terminal.
    """
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 26, 30)
    rose.print_plant()
    sunflower = Plant("Sunflower", 80, 45)
    sunflower.print_plant()
    cactus = Plant("Cactus", 15, 120)
    cactus.print_plant()


if __name__ == "__main__":
    ft_garden_data()
