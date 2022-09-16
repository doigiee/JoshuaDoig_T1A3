class XP:
    def __init__(self, XP):
        self.XP = XP

class blob():
    def __init__(self, name, species, hp = 100, level = 1, atk = 1, XP = 0):
        self.name = name
        self.species = species
        self.hp = hp
        self.level = level
        self.atk = atk
        self.XP = XP

fire_blob = blob('calcifer', 'fire', 100, level = 1, atk = 1)
water_blob = blob('Rimuru', 'water', 100, level = 1, atk = 1)
grass_blob = blob('Gulpin', 'grass', 100, level = 1, atk = 1)

print(fire_blob.name)
print(water_blob.level)

