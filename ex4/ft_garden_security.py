class Plant:
    def __init__(self, name, height, age):
        self.set_name(name)
        self.set_height(height)
        self.set_age(age)

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
        print(f"Plant created: {self._name}")

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age < 0:
            raise ValueError(f"Age {age} days [REJECTED]")
        self._age = age
        print(f"Age updated: {self.get_age()} days [OK]")

    def get_height(self):
        return self._height

    def set_height(self, height):
        if height < 0:
            print("\nInvalid operation attempted ", end="")
            print(f"height {height} [REJECTED]")
            print("Security: Negative height rejected")
            self._height = 0
            return
        self._height = height
        print(f"Height updated: {self.get_height()}cm [OK]")


def display_garden(plant):
    print("\nCurrent Plant: ", end="")
    print(f"{plant.get_name()} ({plant.get_height()}cm,", end="")
    print(f" {plant.get_age()} days)")


def fill_garden(plants_data):
    name, height, age = plants_data[0]
    plant = Plant(name, height, age)
    return plant


def ft_garden_security():
    plants_data = [
        ("Rose", -5, 30)
    ]
    print("=== Garden Security System ===")
    plant = fill_garden(plants_data)
    display_garden(plant)


if __name__ == "__main__":
    ft_garden_security()
