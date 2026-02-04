class GardenManager:
    total_managers = 0

    def __init__(self, name):
        self.set_name(name)
        self.score = 0
        self.plants = []
        self.total_growth = 0
        self.height_valid = True
        GardenManager.total_managers += 1

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    class GardenStats:
        @staticmethod
        def count_plant_types(plants):
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
            return len(plants)

        @staticmethod
        def validate_heights(plants):
            for plant in plants:
                if plant.get_height() < 0:
                    return False
            return True

    @classmethod
    def create_garden_network(cls, name, garden_data):
        manager = cls(name)
        for plant in garden_data:
            manager.plants.append(plant)
            print(f"Added {plant.get_name()} to {manager.get_name()}'s garden")
        manager.height_valid = cls.GardenStats.validate_heights(manager.plants)
        return manager

    def grow_plants(self):
        print(f"\n{self.get_name()} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1
            self.score += plant.get_height()

    def statistics(self):
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
    def __init__(self, name, height, age):
        self.set_name(name)
        self.set_height(height)
        self.set_age(age)

    def grow(self):
        self._height += 1
        print(f"{self.get_name()} grew 1cm")

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_height(self):
        return self._height

    def set_height(self, height):
        if height < 0:
            raise ValueError("Height cannot be negative")
        self._height = height

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self._age = age

    def display(self):
        print(f"- {self.get_name()}: ", end="")
        print(f"{self.get_height()}cm, {self.get_age()} days")


class FloweringPlant(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.set_color(color)

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def bloom(self):
        print("(blooming)", end="")

    def display(self):
        print(f"- {self.get_name()}: ", end="")
        print(f"{self.get_height()}cm, {self.get_color()} flowers ", end="")
        self.bloom()
        print()


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, prize_level):
        super().__init__(name, height, age, color)
        self.set_prize_level(prize_level)

    def set_prize_level(self, prize_level):
        self._prize_level = prize_level

    def get_prize_level(self):
        return self._prize_level

    def display(self):
        print(f"- {self.get_name()}: ", end="")
        print(f"{self.get_height()}cm, {self.get_color()} flowers ", end="")
        self.bloom()
        print(f", Prize points: {self.get_prize_level()}")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.set_trunk_diameter(trunk_diameter)

    def set_trunk_diameter(self, trunk_diameter):
        if trunk_diameter < 0:
            raise ValueError("Trunk diameter cannot be negative")
        self._trunk_diameter = trunk_diameter

    def get_trunk_diameter(self):
        return self._trunk_diameter

    def grow(self):
        self._height += 1
        print(f"{self.get_name()} Tree grew 1cm")

    def display(self):
        print(f"- {self.get_name()} Tree: {self.get_height()}cm")


def valid_height(manager1, manager2):
    return manager1.height_valid and manager2.height_valid


def ft_garden_analytics():
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
