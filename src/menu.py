from simple_term_menu import TerminalMenu
import main
main_menu = ["[p] Play Game", "[i] Instructions", "[q] Quit"]
sub_menu = ["[r] return to main menu"]

loop = True

while loop:
    descision_for_menu = main_menu[TerminalMenu(main_menu, title = "Main menu", menu_cursor_style = ("fg_red", "bold"), menu_highlight_style = ("fg_black", "bg_red"), menu_cursor = "->").show()]

    if descision_for_menu == "[p] Play Game":
        main.main_program()

    elif descision_for_menu == "[i] Instructions":
        sub_loop = True
        while sub_loop:
            print("This game is quite simple, go through the game by reading and enjoying the story.\nPress 'y' followed by the 'enter key' once finished reading text. \nPick a blob '1' , '2' or '3' + 'enter key' then manually type 'battle', 'eat' or 'play' to do activites with your blob.")
            descision_for_menu = sub_menu[TerminalMenu(sub_menu, title = "Instructions Menu").show()]

            if descision_for_menu == "[r] return to main menu":
                sub_loop = False

    elif descision_for_menu == "[q] Quit":
        loop = False

        