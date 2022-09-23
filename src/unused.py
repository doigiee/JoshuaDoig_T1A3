#all of this file contains is some of the unused code:

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

 
# one_variants = ("1", "one", "One")
# two_variants = ("2", "two", "Two")
# three_variants = ("3", "three", "Three")
# class RangeError(Exception):
#     pass
#error handling for wrong number inputs
#wasn't working with multiple attempts, formattings and iterances so decided to go with a more simple approach
# def get_int():
#     val = int(input('Enter an integer: '))
#     if val not in range(1, 3):
#         raise RangeError(f'{val} is out of range - must be between 1 and 10')

#     return val
    # descision = input("make your choice, type '1', '2' or '3': ")
    # # clearing.clear()
    # def make_a_choice():
    #     if descision == "1":
    #         pa.Fire_Blob()
    #     elif descision == "2":
    #         pa.Water_Blob ()
    #     elif descision == "3":
    #         pa.Grass_Blob ()
    #     # elif descision != ("1" "2" "3"):
    #     #     descision = input("try again '1', '2' or '3': ")
    #     #     make_a_choice()
    #     # else: get_int()
    # make_a_choice()