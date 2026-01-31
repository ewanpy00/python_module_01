class Plant:
    def __init__(self, name, hight, age):
        self.name = name
        self.hight = hight
        self.age = age
    def print_plant(self):
        print(f"{self.name}: {self.hight}cm, {self.age} days old")

def ft_garden_data():
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 26, 30)
    rose.print_plant()
    sunflower = Plant("Sunflower", 80, 45)
    sunflower.print_plant()
    cactus = Plant("Cactus", 15, 120)
    cactus.print_plant()

if __name__ == "__main__":
    ft_garden_data()