
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
