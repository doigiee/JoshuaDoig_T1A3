class level:
    def __init__(self, XP):
        self.XP = XP

class days:
    def __init__(self, days_left):
        self.days_left = days_left

class Character:
    __available_species = ['Fire-blob', 'water_blob', 'grass_blob']

    def __init__(self, name, species, hp, level, atk):
        self.name = name
        self.species = species
        self.hp = hp
        self.level = level
        self.atk = atk

print(blob.__str__())
print(blob.__repr__())

fire_blob = blob('calcifer', 'fire', 70, level = 1, atk = 50)
water_blob = blob('Rimuru', 'water', 150, level = 1, atk = 50)
grass_blob = blob('Gulpin', 'grass', 100, level = 10, atk = 50)


#print(fire_blob.name)
#print(water_blob.level)

