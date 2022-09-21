import clearing
clearing.clear()
import simple_term_menu
import pixel_art as pa
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)
from xml.dom import InvalidCharacterErr
#import functions
import classes

#input potientials
yes_variants = ("Y", "y", "Yes", "YES", "yes")
no_variants = ("N", "n", "No", "NO", "no")
one_variants = ("1", "one", "One")
two_variants = ("2", "two", "Two")
three_variants = ("3", "three", "Three")

def Wrong_number():
    val = int(input('Enter an integer: '))
    if not val in range(1, 3):
        raise NameError(f'{val} is out of range - must be between 1 and 10')

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
game_over_text = '\n Sorry but your blob lost all it\'s health.\nGAME OVER'
#reused continue segway
next_continue = '\nContinue?'
what_activity = '\n What activity would you like to do next?\n'
######def main_program():

#game title
pa.The_Blob_Game_Title ()

#indroductiory text, choose blob text, continue prompt
next(next_continue)
print('----------------------------------------------------------------')


print(introduction_text)
print(help_us_text)
#continue prompt
next(next_continue)
print('----------------------------------------------------------------')

print(choose_blob_text)
#continue prompt
next(next_continue)
print('----------------------------------------------------------------')

print(choose_blob_selection)

descision = input("make your choice 1, 2 or 3: ")

def make_a_choice():
    if descision == int(1):
        pa.Fire_Blob ()
    elif descision == int(2):
        print(pa.Water_Blob ())
    elif descision == int(3):
        print(pa.Grass_Blob ())
    else: Wrong_number()
    return
make_a_choice()

print("hello")

day_left = 3
days = 0
level= 1

while days < 3 or level < 100:
    print ('you have {days_left} until the town festival and have used {days} with you blob and your blobs level is {level}')
    # offer activity 
    # print (what_activity)
    if input() == str(walk):
        level += 35
        day_left -= 1 
        print(f'your blob went up 35 levels congrats your new level is {level} you have days {day_left}')
    
    elif input() == str(eat):
        level += 25
        print(f'your blob went up 25 levels congrats your new level is {level} you have days {day_left}')
    
    elif input() == str(play):
        level += 40
        print(f'you and your blob had a great afternoon together playing ,your blob went up 35 levels congrats your new level is {level} you have days {day_left}') 
    

# main game area and loop 
#days_left = 0

#while days_left < 3 or classes.Blob.xp < 0:
    ### ask what activites would like to do
 #   print("would you like to do?")

 #   days_left += 1
     
  #  if days_left > 3:
  #      pass




# every 3 activites refresh blob hp and Game Over counter =-1 and ask question relating to blob

# check for instance of GAME OVER counter reaching 0 days or 0 hp after each activity
# e.g if Gamer Over counter == 0 or hp == 0 print GAME OVER and return main_program



#Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Style: DIM, NORMAL, BRIGHT, RESET_ALL

######main_program()