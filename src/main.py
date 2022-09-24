import colorama
import clearing
import pixel_art as pa
import functions
from classes import Blob
from simple_term_menu import TerminalMenu
from colorama import Fore, Back
colorama.init(autoreset=True)

#text for Story game
introduction_text = '\nWelcome to Blobville!\nThe Village needs your help! Evil blobs have invaded the area.\nWe need a pure heart to bring balance back to our World!\n'
help_us_text = '\nYou are our last chance! Quickly, choose one of these three eggs and raise it to level 100 before the village festival of light in 3 days\n\n\n The fate of our World rests in your hands...\n'
choose_blob_text = f'\n{Back.MAGENTA}***** Three glistening eggs lay before you, each sublime in their own way *****{Back.RESET}\n\n{Fore.RED}A redish burning ember aura radiates from the left-most egg, it calls to those who have no fear in their hearts \n\n{Fore.BLUE}The middle egg, blue as a clear summer sky, vibrates with rythmic ripples, it calls those who can endure anything\n\n{Fore.GREEN}The right egg, green and littered with brownish-yellow vines and leaves, shimmers and releases a fragrant aroma, calling those who have no doubt within their heart.\n\n'
choose_blob_selection = f'\n1.{Fore.RED} Red Egg\n{Fore.RESET}2. {Fore.BLUE}Blue Egg{Fore.RESET}\n3. {Fore.GREEN}Green Egg{Back.RESET}\n\n'
congrats_text = 'YAY! Together with your Blob you were able to reach level 100 before the town festival and save the world from the evil blobs.\n !!!CONGRATULATIONS!!!'
game_over_text = '\nSorry but your blob didn\'t reach level 100 in 3 days.\nGAME OVER'
#reused continue segway
next_continue = '\nContinue?'
what_activity = "\n What activity would you like to do next? \n1. fight\n2. eat\n3. play \n\nif wanting to walk type 'fight', or 'eat', or 'play'\n"
#input potientials


def main_program():
    #game title
    clearing.clear()
    pa.The_Blob_Game_Title ()

    #indroductiory text, choose blob text, continue prompt
    functions.next(next_continue)
    print('----------------------------------------------------------------')
    clearing.clear()

    print(introduction_text)
    print(help_us_text)
    #continue prompt
    functions.next(next_continue)
    print('----------------------------------------------------------------')
    clearing.clear()

    print(choose_blob_text)
    #continue prompt
    functions.next(next_continue)
    print('----------------------------------------------------------------')
    clearing.clear()

    print(choose_blob_selection)

    while True:
        descision = input("make your choice, type '1', '2' or '3': ")
        if descision == "1":
            pa.Fire_Blob()
            break
        if descision == "2":
            pa.Water_Blob ()
            break
        if descision == "3":
            pa.Grass_Blob ()
            break
        else:
            print("\nInvalid Character - Please enter either: '1', '2', '3'")

    print("As you touch the egg a warm glow explodes from within, What is this?...")

    if descision == "1":
        blob_thingy = Blob('calcifer', 'fire', 70, atk = 50, level = 0)
    elif descision == "2":
        blob_thingy = Blob('rimuru', 'water', 150, atk = 50, level = 0)
    elif descision == "3":
        blob_thingy = Blob('gulpin', 'grass', 100, atk = 50, level = 0)

    print(blob_thingy.__dict__)
    
    functions.next(next_continue)
    print('----------------------------------------------------------------')
    clearing.clear()

    print("Remember, you must now level your blob upto level 100 before the town festival")
    
    #main game loop.
    days_left = 3
    days = 0


    while blob_thingy.level < 300 and days < 4:
        # print(f'you have {days_left} days until the town festival and have used {days} day(s) with you blob and your blob\'s level is {blob_thingy.level}')
        # offer activity
        print(what_activity)
        choice = input()
        if choice == "fight":
            clearing.clear()
            blob_thingy.level += 20
            days += 1
            days_left -= 1
            print(f'your blob went up 20 levels congrats your new level is {blob_thingy.level} you have {days_left} days left')
        elif choice == "eat":
            clearing.clear()
            blob_thingy.level += 30
            days += 1
            days_left -= 1
            print(f'your blob went up 30 levels congrats your new level is {blob_thingy.level} you have {days_left} days left')
        elif choice == "play":
            clearing.clear()
            blob_thingy.level += 40
            days += 1
            days_left -= 1
            print(f'you and your blob had a great afternoon together playing, your blob went up 40 levels congrats your new level is {blob_thingy.level} you have  {days_left} days')
        else:
            clearing.clear()
            print("Please choose a proper activity")
        if days == 3 and blob_thingy.level < 101:
            clearing.clear()
            print(game_over_text)
            break
        if days == 3 and blob_thingy.level >= 101:
            clearing.clear()
            print(congrats_text)
            break
    functions.next(next_continue)
    print('----------------------------------------------------------------')
    clearing.clear()

#main menu - wasn't working from importing from another .py file but was working when placed here
def menu_log ():
    clearing.clear()
    main_menu = ["[p] Play Game", "[i] Instructions", "[q] Quit"]
    sub_menu = ["[r] return to main menu"]

    loop = True

    while loop:
        descision_for_menu = main_menu[TerminalMenu(main_menu, title = "Main menu", menu_cursor_style = ("fg_red", "bold"), menu_highlight_style = ("fg_black", "bg_red"), menu_cursor = "->").show()]

        if descision_for_menu == "[p] Play Game":
            main_program()

        elif descision_for_menu == "[i] Instructions":
            sub_loop = True
            while sub_loop:
                print("This game is quite simple, go through the game by reading and enjoying the story.\nPress 'y' followed by the 'enter key' once finished reading text. \nPick a blob '1' , '2' or '3' + 'enter key' then manually type 'fight', 'eat' or 'play' to do activites with your blob.")
                descision_for_menu = sub_menu[TerminalMenu(sub_menu, title = "Instructions Menu").show()]

                if descision_for_menu == "[r] return to main menu":
                    sub_loop = False

        elif descision_for_menu == "[q] Quit":
            loop = False

menu_log()
