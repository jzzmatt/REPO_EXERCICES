class Player():
    total_objects = 2
    current_objects = 0

    def __new__(cls, *args):
        if (cls.current_objects >= cls.total_objects):
            raise ValueError ('More than 2 Objects')

        cls.current_objects += 1
        return super().__new__(cls)



    def __init__(self, name, health):
        self.name = name
        self.health = health


    def get_name(self):
        return self.name


    def get_health(self):
        return self.health




obj1 = Player("Sam", 103)
obj2 = Player("Jonh", 86)

print(Player.current_objects)
print(obj1.get_name())
print(obj1.get_health())
print(obj2.get_name())
print(obj2.get_health())
print(Player.current_objects)

#obj3 = Player("Wolf", 201)