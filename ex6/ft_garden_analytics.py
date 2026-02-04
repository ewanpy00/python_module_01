"""
Garden management system with analytics and plant hierarchy.
"""


class GardenManager:
    """Manages a garden and its plants."""

    total_managers = 0

    def __init__(self, name):
        """Create a garden manager."""
        self.set_name(name)
        self.score = 0
        self.plants = []
        self.total_growth = 0
        self.height_valid = True
        GardenManager.total_managers += 1

    def set_name(self, name):
        """Set manager name."""
        self._name = name

    def get_name(self):
        """Return manager name."""
        return self._name

    class GardenStats:
        """Utility class for garden statistics."""

        @staticmethod
        def count_plant_types(plants):
            """Count regular, flowering, and prize plants."""
            regular = flowering = prize = 0
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize

        @staticmethod
        def count_plants(plants):
            """Return number of plants."""
            return len(plants)

        @staticmethod
        def validate_heights(plants):
            """Check that all plant heights are valid."""
            for plant in plants:
                if plant.get_height() < 0:
                    return False
            return True

    @classmethod
    def create_garden_network(cls, name, garden_data):
        """Create a manager and assign plants."""
        manager = cls(name)
        for plant in garden_data:
            manager.plants.append(plant)
            print(f"Added {plant.get_name()} to {manager.get_name()}'s garden")
        manager.height_valid = cls.GardenStats.validate_heights(manager.plants)
        return manager

    def grow_plants(self):
        """Grow all plants and update score."""
        print(f"\n{self.get_name()} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1
            self.score += plant.get_height()

    def statistics(self):
        """Print garden statistics."""
        r, f, p = self.GardenStats.count_plant_types(self.plants)
        print(f"\n=== {self.get_name()}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            plant.display()
        print("\nPlants added: ", end="")
        print(f"{self.GardenStats.count_plants(self.plants)}, ", end="")
        print(f"Total growth: {self.total_growth}cm")
        print(f"Plant types: {r} regular, {f} flowering, {p} prize flowers")


class Plant:
    """Base class for all plants."""

    def __init__(self, name, height, age):
        """Create a plant."""
        self.set_name(name)
        self.set_height(height)
        self.set_age(age)

    def grow(self):
        """Increase height by 1 cm."""
        self._height += 1
        print(f"{self.get_name()} grew 1cm")

    def get_name(self):
        """Return plant name."""
        return self._name

    def set_name(self, name):
        """Set plant name."""
        self._name = name

    def get_height(self):
        """Return plant height."""
        return self._height

    def set_height(self, height):
        """Set plant height with validation."""
        if height < 0:
            raise ValueError("Height cannot be negative")
        self._height = height

    def get_age(self):
        """Return plant age."""
        return self._age

    def set_age(self, age):
        """Set plant age with validation."""
        if age < 0:
            raise ValueError("Age cannot be negative")
        self._age = age

    def display(self):
        """Display plant information."""
        print(f"- {self.get_name()}: ", end="")
        print(f"{self.get_height()}cm, {self.get_age()} days")


class FloweringPlant(Plant):
    """Plant with flowers."""

    def __init__(self, name, height, age, color):
        """Create a flowering plant."""
        super().__init__(name, height, age)
        self.set_color(color)

    def set_color(self, color):
        """Set flower color."""
        self._color = color

    def get_color(self):
        """Return flower color."""
        return self._color

    def bloom(self):
        """Display blooming status."""
        print("(blooming)", end="")

    def display(self):
        """Display flowering plant information."""
        print(f"- {self.get_name()}: ", end="")
        print(f"{self.get_height()}cm, {self.get_color()} flowers ", end="")
        self.bloom()
        print()


class PrizeFlower(FloweringPlant):
    """Flower with prize value."""

    def __init__(self, name, height, age, color, prize_level):
        """Create a prize flower."""
        super().__init__(name, height, age, color)
        self.set_prize_level(prize_level)

    def set_prize_level(self, prize_level):
        """Set prize level."""
        self._prize_level = prize_level

    def get_prize_level(self):
        """Return prize level."""
        return self._prize_level

    def display(self):
        """Display prize flower information."""
        print(f"- {self.get_name()}: ", end="")
        print(f"{self.get_height()}cm, {self.get_color()} flowers ", end="")
        self.bloom()
        print(f", Prize points: {self.get_prize_level()}")


class Tree(Plant):
    """Tree plant type."""

    def __init__(self, name, height, age, trunk_diameter):
        """Create a tree."""
        super().__init__(name, height, age)
        self.set_trunk_diameter(trunk_diameter)

    def set_trunk_diameter(self, trunk_diameter):
        """Set trunk diameter with validation."""
        if trunk_diameter < 0:
            raise ValueError("Trunk diameter cannot be negative")
        self._trunk_diameter = trunk_diameter

    def get_trunk_diameter(self):
        """Return trunk diameter."""
        return self._trunk_diameter

    def grow(self):
        """Increase tree height by 1 cm."""
        self._height += 1
        print(f"{self.get_name()} Tree grew 1cm")

    def display(self):
        """Display tree information."""
        print(f"- {self.get_name()} Tree: {self.get_height()}cm")


def valid_height(manager1, manager2):
    """Check if both gardens have valid plant heights."""
    return manager1.height_valid and manager2.height_valid


def ft_garden_analytics():
    """Run garden management demo."""
    garden_data = [
        [
            Tree("Oak", 100, 50, 50),
            FloweringPlant("Rose", 26, 30, "red"),
            PrizeFlower("Sunflower", 51, 30, "yellow", 10)
        ],
        [
            Tree("Pine", 100, 50, 20),
            FloweringPlant("Tulip", 15, 45, "pink")
        ]
    ]

    print("=== Garden Management System Demo ===")
    manager1 = GardenManager.create_garden_network("Alice", garden_data[0])
    print("")
    manager2 = GardenManager.create_garden_network("Bob", garden_data[1])

    manager1.grow_plants()
    manager1.statistics()

    print(f"\nHeight validation test: {valid_height(manager1, manager2)}")
    print(f"Garden scores - Alice: {manager1.score}, Bob: {manager2.score}")
    print(f"Total gardens managed: {GardenManager.total_managers}")


if __name__ == "__main__":
    ft_garden_analytics()
