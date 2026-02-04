"""
This module demonstrates a plant security and validation system.

It shows how setters can be used to validate plant attributes
such as name, height, and age, and how invalid data is handled.
"""


class Plant:
    """
    Represents a plant with validated attributes.

    Attribute values are set using setter methods that enforce
    basic validation rules.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initializes a Plant instance using validated setters.

        Args:
            name (str): The name of the plant.
            height (int): The height of the plant in centimeters.
            age (int): The age of the plant in days.
        """
        self.set_name(name)
        self.set_height(height)
        self.set_age(age)

    def get_name(self) -> str:
        """
        Returns the plant's name.

        Returns:
            str: The name of the plant.
        """
        return self._name

    def set_name(self, name: str) -> None:
        """
        Sets the plant's name.

        Args:
            name (str): The name to assign to the plant.
        """
        self._name = name
        print(f"Plant created: {self._name}")

    def get_age(self) -> int:
        """
        Returns the plant's age.

        Returns:
            int: The age of the plant in days.
        """
        return self._age

    def set_age(self, age: int) -> None:
        """
        Sets the plant's age with validation.

        Raises:
            ValueError: If the age is negative.
        """
        if age < 0:
            print("\n Ivalid operation attempted ", end="")
            print(f"age {age} [REJECTED]")
            print("Security: Negative height rejected")
            self._age = 0
        else:
            self._age = age
            print(f"Age updated: {self.get_age()} days [OK]")

    def get_height(self) -> int:
        """
        Returns the plant's height.

        Returns:
            int: The height of the plant in centimeters.
        """
        return self._height

    def set_height(self, height: int) -> None:
        """
        Sets the plant's height with validation.

        If a negative height is provided, the value is rejected
        and the height is set to 0.

        Args:
            height (int): The height of the plant in centimeters.
        """
        if height < 0:
            print("\nInvalid operation attempted ", end="")
            print(f"height {height} [REJECTED]")
            print("Security: Negative height rejected")
            self._height = 0
        else:
            self._height = height
            print(f"Height updated: {self.get_height()}cm [OK]")


def display_garden(plant: Plant) -> None:
    """
    Displays formatted information about a plant.

    Args:
        plant (Plant): The plant to display.
    """
    print("\nCurrent Plant: ", end="")
    print(f"{plant.get_name()} ({plant.get_height()}cm,", end="")
    print(f" {plant.get_age()} days)")


def fill_garden(plants_data: list[tuple[str, int, int]]) -> Plant:
    """
    Creates a Plant object from provided plant data.

    Args:
        plants_data (list[tuple]): A list containing plant data tuples.

    Returns:
        Plant: A Plant instance created from the first data entry.
    """
    name, height, age = plants_data[0]
    plant = Plant(name, height, age)
    return plant


def ft_garden_security() -> None:
    """
    Runs a garden security validation scenario.

    Attempts to create a plant with invalid data and demonstrates
    how the system handles and corrects it.
    """
    plants_data = [
        ("Rose", -5, 30)
    ]
    print("=== Garden Security System ===")
    plant = fill_garden(plants_data)
    display_garden(plant)


if __name__ == "__main__":
    ft_garden_security()
