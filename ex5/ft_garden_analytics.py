class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

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
        print(f"\n{self._name} (Vegetable): {self._height}cm, {self._age} days, {self._harvest_season} season")
        print(f"{self._name} is rich in vitamin {self._nutrition_value}")

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

class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self._color = color
        print(f"\n{self._name} (Flower): {self._height}cm, {self._age} days, {self._color} color")

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color
    
    def bloom(self):
        print(f"{self._name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        print(f"\n{self._name} (Tree): {self._height}cm, {self._age} days, {self._trunk_diameter}cm diameter")

    @property
    def trunk_diameter(self):
        return self._trunk_diameter
    
    @trunk_diameter.setter
    def trunk_diameter(self, trunk_diameter):
        self._trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"{self._name} provides 78 square metersof shade")

def ft_plant_types():
    print("=== Garden Plant Types ===")
    flower = Flower("Rose", 25, 30, "red")
    flower.bloom()
    flower = Flower("Sunflower", 40, 180, "yellow")
    flower.bloom()
    oak = Tree("Oak", 500, 1825, 50)
    oak.produce_shade()
    pine = Tree("Pine", 300, 1000, 30)
    pine.produce_shade()
    tomato = Vegetable("Tomato", 80, 90, "summer", 'C')
    cucumber = Vegetable("Cucumber", 60, 75, "autumn", "D")


if __name__ == "__main__":
    ft_plant_types()

#add checker in setter function