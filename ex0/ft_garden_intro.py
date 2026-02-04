"""
This module demonstrates a simple example of printing information
about a plant in a garden.
"""


def ft_garden_intro() -> None:
    """
    Prints information about a plant in the garden.

    Plant attributes:
    - name (str): The name of the plant.
    - height (int): The height of the plant in centimeters.
    - age (int): The age of the plant in days.

    The function prints a welcome message, the plant's details,
    and an end-of-program message.
    """
    name = "Rose"
    height = 100
    age = 100
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}")
    print(f"Age: {age}")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
