class Plant:
    def __init__(self, name, height, years):
        self.name = name
        self.height = height
        self.years = years
        self.startingAge = years
    def grow(self):
        self.height += 1
    def age(self):
        self.years += 1
        self.grow()
    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.years} days old")

def ft_plant_growth():
    plant = Plant("Rose", 25, 30)
    days = 7
    print("=== Day 1 ===")
    plant.get_info()
    for i in range(1, days+1):
        if i % 7 == 0:
            print(f"=== Day {i} ===")
            plant.get_info()
            print(f"Growth this week: +{plant.years - plant.startingAge}cm")
        plant.age()

if __name__ == "__main__":
    ft_plant_growth()