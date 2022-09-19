from xml.dom import InvalidCharacterErr
import clearing
clearing.clear()
import pixel_art as pa
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
#import functions
#import classes

#input potientials
yes_variants = ("Y", "y", "Yes", "YES", "yes")
no_variants = ("N", "n", "No", "NO", "no")
one_variants = ("One", "one", "1")
two_variants = ("Two", "two", "2")
three_variants = ("Three", "three", "3")

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
if input("") == one_variants:
    print(pa.Fire_Blob ())
elif input ("") == two_variants:
    print(pa.Water_Blob ())
elif input ("") == three_variants:
    print(pa.Grass_Blob ())

# set player blob attribute

# ask what activites would like to do
print 
# do the operation and - 1 of 3 from daily activites value

# every 3 activites refresh blob hp and Game Over counter =-1 and ask question relating to blob

# check for instance of GAME OVER counter reaching 0 days or 0 hp after each activity
# e.g if Gamer Over counter == 0 or hp == 0 print GAME OVER and return main_program


#while  blob.hp != 0:
    #if level == 100 you win
   # if blob.level == 100:
      #  print('congrats_text')


   

   # else game_over_text



# def WIN_GAME():
#   Blob_level_100 = True
#return Blob_level_100
# print(WIN GAMW ()) 

#Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Style: DIM, NORMAL, BRIGHT, RESET_ALL

######main_program()

