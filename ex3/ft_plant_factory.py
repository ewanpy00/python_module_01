class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def display(self):
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def ft_plant_factory():
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
