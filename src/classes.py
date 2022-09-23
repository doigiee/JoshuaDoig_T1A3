class Blob:
    def __init__(self, name, species, hp, atk, level):
        self.name = name
        self.species = species
        self.hp = hp
        self.atk = atk
        self.level = level


#not used currently

# class enemy:
#     def __init__(self, level):
#         self.level = level
#         self.xp = level

#     #transfer level of this loot to Blob
#     def defeat(self, level):
#         #Blob.xp.add(self.level)
#         self.level = 0
        

# class days:
#     def __init__(self, days):
#         self.days = days

# class level:
#     def set_level(self, level):
#         self.level = level

#     def add_level(self, level):
#         self.level += level




#was initially intending there to be three blob classes though for now 1 is fine
#class Fire_blob(Blob):
#    def __init__(self, name, species, hp=10, atk=20
#    super().__init__(name, species, hp, atk)
#    self.level = level


#@classmethod
#(blob.__str__())
#print(blob.__repr__())