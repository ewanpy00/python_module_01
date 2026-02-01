class Plant:
    def __init__(self, name, height, age):
        self.name = name      # вызывает сеттер
        self.height = height
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
        print(f"Plant created: {self._name}")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age >= 0:
            self._age = age
            print(f"Age updated: {self._age} days [OK]")
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
            print(f"Height updated: {self._height} cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height} cm [REJECTED]")
            print("Security: Negative height rejected")
            exit()


def display_garden(plant):
    print("Current Plant: ", end="")
    print(f"{plant.name} ({plant.height}cm, {plant.age} days)")

def fill_garden(plants_data):
    name, height, age = plants_data[0]
    plant = Plant(name, height, age)
    return plant

def ft_garden_security():
    plants_data = [
        ("Rose", -25, 30)
    ]
    print("=== Garden Security System ===")
    plant = fill_garden(plants_data)
    display_garden(plant)

if __name__ == "__main__":
    ft_garden_security()