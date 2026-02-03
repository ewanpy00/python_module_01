#Include a method create_garden_network() that works on the manager type itself????

class GardenManager:
    def __init__(self, name):
        self._name = name
        self.score = 0
        self.gardens = []

    @classmethod
    def create_garden_network(cls, name, garden_data):
        manager = cls(name)
        for data in garden_data:
            manager.gardens.append(data)
            print{f"Added {data.name} to {manager._name}'s garden"}
        return manager
        
    def statistics(self):
        print(f"=== {self._name}'s Garden Report ===")
        print("Plants in garden:")
        for garden in self.gardens:
            garden.display()
    #add display method to Plants
    def statistics(self):
        
# class Garden:
#     def __init__(self):
#         self._plant = []
#     def addToGarden(self, plant):
#         self._plant.append(plant)


class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        print(f"\nAdded {self._name} to Alice's garden")

    def grow(self):
        self._height += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age >= 0:
            self._age = age
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
            exit()
    
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height >= 0:
            self._height = height
        else:
            print(f"Invalid operation attempted: height {height} cm [REJECTED]")
            print("Security: Negative height rejected")
            exit()

class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutrition_value):
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutrition_value = nutrition_value
        # print(f"\nAdded {self._name} to Alice's garden")

    @property
    def nutrition_value(self):
        return self._nutrition_value
    
    @nutrition_value.setter
    def nutrition_value(self, nutrition_value):
        self._nutrition_value = nutrition_value

    @property
    def harvest_season(self):
        return self._harvest_season
    
    @harvest_season.setter
    def harvest_season(self, harvest_season):
        self._harvest_season = harvest_season

class FloweringPlant(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self._color = color
        # print(f"\nAdded {self._name} to Alice's garden")

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color
    
    def bloom(self):
        print(f"{self._name} is blooming beautifully!")

class PrizeFlower(FloweringPlant):
    def __init__(self, name, color, prize_level):
        super().__init__(name, color)
        self.prize_level = prize_level

class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        # print(f"\nAdded {self._name} to Alice's garden")

    @property
    def trunk_diameter(self):
        return self._trunk_diameter
    
    @trunk_diameter.setter
    def trunk_diameter(self, trunk_diameter):
        self._trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"{self._name} provides 78 square metersof shade")

def ft_garden_analytics():
    garden_data = [
        Tree("Oak", 100, 50, 50)
    ]
    manager = GardenManager.create_garden_network("Alice", garden_data)
    print("=== Garden Management System Demo ===")

if __name__ == "__main__":
    ft_garden_analytics()

#Переопределение методов