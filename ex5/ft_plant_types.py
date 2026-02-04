"""
Garden plant type demonstration using inheritance.
"""


class Plant:
    """Base class for all plants."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Create a plant with name, height, and age."""
        self.set_name(name)
        self.set_height(height)
        self.set_age(age)

    def get_name(self) -> str:
        """Return the plant name."""
        return self._name

    def set_name(self, name: str) -> None:
        """Set the plant name."""
        self._name = name

    def get_height(self) -> int:
        """Return the plant height."""
        return self._height

    def set_height(self, height: int) -> None:
        """Set the plant height with validation."""
        if height < 0:
            raise ValueError(f"Height {height} cm [REJECTED]")
        self._height = height

    def get_age(self) -> int:
        """Return the plant age."""
        return self._age

    def set_age(self, age: int) -> None:
        """Set the plant age with validation."""
        if age < 0:
            raise ValueError(f"Age {age} days [REJECTED]")
        self._age = age

    def display(self) -> None:
        """Print basic plant information."""
        print(f"- {self.get_name()}: {self.get_height()}cm,", end="")
        print(f" {self.get_age()} days")


class Vegetable(Plant):
    """Plant subclass representing a vegetable."""

    def __init__(
        self, name: str, height: int, age: int,
        harvest_season: str, nutrition_value: str
    ) -> None:
        """Create a vegetable with harvest season and nutrition."""
        super().__init__(name, height, age)
        self.set_harvest_season(harvest_season)
        self.set_nutrition_value(nutrition_value)

        print(f"\n{self.get_name()} (Vegetable): ", end="")
        print(f"{self.get_height()}cm, {self.get_age()} days, ", end="")
        print(f"{self.get_harvest_season()} season")
        print(f"{self.get_name()} is rich in vitamin", end="")
        print(f" {self.get_nutrition_value()}")

    def get_harvest_season(self) -> str:
        """Return the harvest season."""
        return self._harvest_season

    def set_harvest_season(self, season: str) -> None:
        """Set the harvest season."""
        self._harvest_season = season

    def get_nutrition_value(self) -> str:
        """Return the nutrition value."""
        return self._nutrition_value

    def set_nutrition_value(self, value: str) -> None:
        """Set the nutrition value."""
        self._nutrition_value = value


class Flower(Plant):
    """Plant subclass representing a flower."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Create a flower with a color."""
        super().__init__(name, height, age)
        self.set_color(color)

        print(f"\n{self.get_name()} (Flower): {self.get_height()}cm, "
              f"{self.get_age()} days, {self.get_color()} color")

    def get_color(self) -> str:
        """Return the flower color."""
        return self._color

    def set_color(self, color: str) -> None:
        """Set the flower color."""
        self._color = color

    def bloom(self) -> None:
        """Print a blooming message."""
        print(f"{self.get_name()} is blooming beautifully!")

    def display(self) -> None:
        """Display flower info and bloom."""
        print(f"- {self.get_name()}: {self.get_height()}", end="")
        print(f"cm, {self.get_color()} flowers")
        self.bloom()


class Tree(Plant):
    """Plant subclass representing a tree."""

    def __init__(
            self, name: str, height: int,
            age: int, trunk_diameter: int
    ) -> None:
        """Create a tree with trunk diameter."""
        super().__init__(name, height, age)
        self.set_trunk_diameter(trunk_diameter)

        print(f"\n{self.get_name()} (Tree): {self.get_height()}cm, "
              f"{self.get_age()} days, {self.get_trunk_diameter()}cm diameter")

    def get_trunk_diameter(self) -> int:
        """Return trunk diameter."""
        return self._trunk_diameter

    def set_trunk_diameter(self, diameter: int) -> None:
        """Set trunk diameter with validation."""
        if diameter < 0:
            raise ValueError(f"Trunk diameter {diameter} cm [REJECTED]")
        self._trunk_diameter = diameter

    def produce_shade(self) -> None:
        """Print shade information."""
        print(f"{self.get_name()} provides 78 square meters of shade")


def ft_plant_types() -> None:
    """Create and display different plant types."""
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 25, 30, "red")
    rose.bloom()
    sunflower = Flower("Sunflower", 40, 180, "yellow")
    sunflower.bloom()
    oak = Tree("Oak", 500, 1825, 50)
    oak.produce_shade()
    pine = Tree("Pine", 300, 1000, 30)
    pine.produce_shade()
    tomato = Vegetable("Tomato", 80, 90, "summer", "C")
    cucumber = Vegetable("Cucumber", 60, 75, "autumn", "D")
    tomato, cucumber


if __name__ == "__main__":
    ft_plant_types()
