
available_blobs = ['Fire blob', 'Water blob', 'Grass blob']
class fire_blob :
    def super(blob):

class water_blob :
    def super(blob):

class grass_blob :
    def super(blob):

class Pokemon():
    def __init__(self, name, type, pokedexNumber):
        self.name = name
        self.pokedexNumber = pokedexNumber
        self.type = type

pikachu = Pokemon("Pikachu", 25, "Electric")
print(pikachu.name)
print(pikachu.pokedexNumber)
print(pikachu.type)





calcifer = classes.Blob('calcifer', 'fire', 70, atk = 50)
calcifer.set_level = (10)
rimuru = classes.Blob('rimuru', 'water', 150, atk = 50)
gulpin = classes.Blob('gulpin', 'grass', 100, atk = 50)
enemy = classes.enemy(level = 10)

print(enemy.__dict__)
print(calcifer.__dict__)
enemy.defeat(calcifer)

print(rimuru.__dict__)
print(gulpin.__dict__)
