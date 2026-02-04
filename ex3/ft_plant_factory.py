"""
This module demonstrates a simple plant factory.

It creates multiple Plant objects from predefined data,
displays their information, and reports the total number
of plants created.
"""


class Plant:
    """
    Represents a plant with basic properties.

    Attributes:
        name (str): The name of the plant.
        height (int): The height of the plant in centimeters.
        age (int): The age of the plant in days.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initializes a Plant instance.

        Args:
            name (str): The name of the plant.
            height (int): The height of the plant in centimeters.
            age (int): The age of the plant in days.
        """
        self.name = name
        self.height = height
        self.age = age

    def display(self) -> None:
        """
        Prints information about the plant.

        Output format:
            Created: <name> (<height>cm, <age> days)
        """
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def ft_plant_factory() -> None:
    """
    Creates multiple Plant objects and displays their details.

    Uses predefined plant data to instantiate Plant objects,
    prints their information, and outputs the total number
    of plants created.
    """
    plant_data = [
        ["Rose", 25, 30],
        ["Oak", 200, 365],
        ["Cactus", 5, 90],
        ["Sunflower", 80, 45],
        ["Fern", 15, 120]
    ]

    plants = [Plant(name, height, age) for name, height, age in plant_data]

    print("=== Plant Factory Output ===")
    count = 0
    for plant in plants:
        plant.display()
        count += 1
    print(f"\nTotal plants created: {count}")


if __name__ == "__main__":
    ft_plant_factory()
