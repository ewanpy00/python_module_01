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

def ft_plant_factory():
    