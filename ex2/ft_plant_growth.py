"""
This module simulates the growth of a plant over time.

It demonstrates how a plant's height and age change
day by day and prints weekly growth information.
"""


class Plant:
    """
    Represents a plant that grows over time.

    Attributes:
        name (str): The name of the plant.
        height (int): The height of the plant in centimeters.
        years (int): The age of the plant in days.
        startingAge (int): The initial age used to track growth.
    """

    def __init__(self, name: str, height: int, years: int) -> None:
        """
        Initializes a Plant instance.

        Args:
            name (str): The name of the plant.
            height (int): The initial height in centimeters.
            years (int): The initial age of the plant in days.
        """
        self.name = name
        self.height = height
        self.years = years
        self.startingHeight = height

    def grow(self) -> None:
        """
        Increases the plant's height by 1 centimeter.
        """
        self.height += 1

    def age(self) -> None:
        """
        Increases the plant's age by one day and triggers growth.
        """
        self.years += 1
        self.grow()

    def get_info(self) -> None:
        """
        Prints the current state of the plant.

        Output format:
            <name>: <height>cm, <age> days old
        """
        print(f"{self.name}: {self.height}cm, {self.years} days old")


def ft_plant_growth() -> None:
    """
    Simulates plant growth over a fixed number of days.

    Creates a Plant instance, advances its age day by day,
    and prints information at the beginning and every 7 days.
    """
    plant = Plant("Rose", 25, 30)
    days = 7
    print("=== Day 1 ===")
    plant.get_info()
    for i in range(1, days + 1):
        if i % 7 == 0:
            print(f"=== Day {i} ===")
            plant.get_info()
            print("Growth this week: +", end="")
            print(f"{plant.height - plant.startingHeight}cm")
        plant.age()


if __name__ == "__main__":
    ft_plant_growth()
