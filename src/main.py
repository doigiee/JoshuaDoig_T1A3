import  pixel_art
from storage import fire_blob
#import functions
#import classes

yes_variants = ("Y", "y", "Yes", "YES", "yes")
no_variants = ("N", "n", "No", "NO", "no")
one_variants = ("One", "one", "1", "1.")

class blob():
    def __init__(self, name, species, hp, level, atk, XP):
        self.name = name
        self.species = species
        self.hp = hp
        self.level = level
        self.atk = atk
        self.XP = XP

fire_blob = blob('calcifer', 'fire', 100, level = 1, atk = 25)
water_blob = blob('Rimuru', 'water', 100, level = 25, atk = 1)
grass_blob = blob('Gulpin', 'grass', 250, level = 1, atk = 1)
#print(fire_blob.name)
#print(water_blob.level)

def next(prompt):
    answer = ""
    while True:
        answer = input(f"\n{prompt}\n'yes' or 'no': ")
        print("")
        if answer in (yes_variants):
            return True

def main_program():

#game title
    pixel_art.The_Blob_Game_Title

    pixel_art.The_Blob_Game_Title_2

#indroductiory text, choose blob text, continue prompt
    introduction_text = '\nWelcome to Blobville!\nThe Village needs your help! Evil blobs have invaded the area.\nWe need the a pure heart to bring balance back to our World!\n'
    choose_blob_text = '\nYou are our last chance! Quickly, choose one of these three eggs and raise it to level 100 before the village festival of light in 3 days\n\n\n The fate of our World rests in your hands...\n'
    choose_blob_text = '\n***** Three glistening eggs lay before you, each sublime in their own way *****\n\n A redish burning ember aura radiates from the left-most egg, it calls to those who have no fear in their hearts \n\n The middle-most egg, blue as a clear summer sky, vibrates with rythmic ripples, it calls those who can endure anything\n\n The rightmost egg, green and littered with brownish-yellow vines, shimmers and releases a fragrant aroma, calling those who have no doubt within their heart.\n\n'  
    choose_blob_selection = '1. red egg \n 2. blue egg \n 3. green egg \n'
    
    next_continue = '\nContinue?'

    print(introduction_text)
    #continue prompt
    if next(next_continue):
        print('----------------------------------------------------------------')

    print(choose_blob_text)
    #continue prompt
    if next(next_continue):
        print('----------------------------------------------------------------')

    print(choose_blob_selection)
        if input == one_variants:
            blob = fire_blob
        elif input == one_variants:
            blob = water_blob
        elif input == one_variants:
            blob = grass_blob


main_program()
