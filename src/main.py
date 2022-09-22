import colorama
import clearing
import pixel_art as pa
from colorama import Fore, Back
colorama.init(autoreset=True)
from xml.dom import InvalidCharacterErr
#import functions
from classes import Blob

#input potientials
yes_variants = ("Y", "y", "Yes", "YES", "yes")
no_variants = ("N", "n", "No", "NO", "no")
one_variants = ("1", "one", "One")
two_variants = ("2", "two", "Two")
three_variants = ("3", "three", "Three")

#error handling for wrong number inputs
def Wrong_number():
    val = (input("Enter an number either '1', '2', or '3': "))
    if not val in range(1, 3):
        raise NameError(f'{val} is out of range - must be between 1 and 3')

    return val

#letting user set the pace
def next(prompt):
    answer = ""
    while True:
        answer = input(f"{prompt}\n'yes' or 'no':")
        print("")
        if answer in (yes_variants):
            return True
        elif answer not in (no_variants):
            InvalidCharacterErr
            print("InvalidCharacterErr- Please enter either: 'yes', 'no', 'y', 'n'")


#text for Story game
introduction_text = '\nWelcome to Blobville!\nThe Village needs your help! Evil blobs have invaded the area.\nWe need a pure heart to bring balance back to our World!\n'
help_us_text = '\nYou are our last chance! Quickly, choose one of these three eggs and raise it to level 100 before the village festival of light in 3 days\n\n\n The fate of our World rests in your hands...\n'
choose_blob_text = f'\n{Back.MAGENTA}***** Three glistening eggs lay before you, each sublime in their own way *****{Back.RESET}\n\n{Fore.RED}A redish burning ember aura radiates from the left-most egg, it calls to those who have no fear in their hearts \n\n{Fore.BLUE}The middle egg, blue as a clear summer sky, vibrates with rythmic ripples, it calls those who can endure anything\n\n{Fore.GREEN}The right egg, green and littered with brownish-yellow vines and leaves, shimmers and releases a fragrant aroma, calling those who have no doubt within their heart.\n\n'
choose_blob_selection = f'\n1.{Fore.RED} Red Egg\n{Fore.RESET}2. {Fore.BLUE}Blue Egg{Fore.RESET}\n3. {Fore.GREEN}Green Egg{Back.RESET}\n\n'
congrats_text = 'YAY! Your Blob reached level 100 before the town festial.\n !!!CONGRATULATIONS!!!'
game_over_text = '\n Sorry but your blob didn\'t reach level 100 in 3 days.\nGAME OVER'
#reused continue segway
next_continue = '\nContinue?'
what_activity = "\n What activity would you like to do next? \n1. walk\n2. eat\n3. play \n\nif wanting to walk type 'walk', or 'play', or 'eat'\n"
######def main_program():

#main menu import


#main program
def main_program():
    #game title
    pa.The_Blob_Game_Title ()

    #indroductiory text, choose blob text, continue prompt
    next(next_continue)
    print('----------------------------------------------------------------')
    clearing.clear()

    print(introduction_text)
    print(help_us_text)
    #continue prompt
    next(next_continue)
    print('----------------------------------------------------------------')
    clearing.clear()

    print(choose_blob_text)
    #continue prompt
    next(next_continue)
    print('----------------------------------------------------------------')
    clearing.clear()

    print(choose_blob_selection)

    descision = input("make your choice, type '1', '2' or '3': ")

    def make_a_choice():
        if descision == "1":
            pa.Fire_Blob()
        elif descision == "2":
            print(pa.Water_Blob ())
        elif descision == "3":
            print(pa.Grass_Blob ())
        else: Wrong_number()
        return

    make_a_choice()
    if descision == "1":
        blob_thingy = Blob('calcifer', 'fire', 70, atk = 50, level = 0)
    elif descision == "2":
        blob_thingy = Blob('\nrimuru', 'water', 150, atk = 50, level = 0)
    elif descision == "3":
        blob_thingy = Blob('\ngulpin', 'grass', 100, atk = 50, level = 0)

    print(blob_thingy.__dict__)


    #main game loop.
    days_left = 3
    days = 0
    # level= 1


    while days < 3 : #or blob_thingy.level < 100#:

        print (f'you have {days_left} days until the town festival and have used {days} day(s) with you blob and your blob\'s level is {blob_thingy.level}')
        # offer activity and add to level. 
        print(what_activity)
        choice = input()
        if choice == "walk":
            clearing.clear()
            blob_thingy.level += 40
            days += 1
            days_left -= 1
            print(f'your blob went up 35 levels congrats your new level is {blob_thingy.level} you have {days_left} days left')
        elif choice == "eat":
            clearing.clear()
            blob_thingy.level += 20
            days += 1
            days_left -= 1
            print(f'your blob went up 25 levels congrats your new level is {blob_thingy.level} you have {days_left} days left')
        elif choice == "play":
            clearing.clear()
            blob_thingy.level += 101
            days += 1
            days_left -= 1
            print(f'you and your blob had a great afternoon together playing , your blob went up 35 levels congrats your new level is {blob_thingy.level} you have days {days_left}')
        else:
            print("Please make a correct choice for an activiy")
        
        if days_left > 1 and blob_thingy.level >= 100:
            clearing.clear()
            print(congrats_text)
            break
        if days_left < 1 and blob_thingy.level < 100:
            clearing.clear()
            print(game_over_text)
            break



# every 3 activites refresh blob hp and Game Over counter =-1 and ask question relating to blob

# check for instance of GAME OVER counter reaching 0 days or 0 hp after each activity
# e.g if Gamer Over counter == 0 or hp == 0 print GAME OVER and return main_program


##other ways to use colorama - reference
#Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Style: DIM, NORMAL, BRIGHT, RESET_ALL

######main_program()