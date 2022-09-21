#!/usr/bin/env python3

from simple_term_menu import TerminalMenu

def main():
    options = ["Play Game", "Instructions", "exit"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")

if __name__ == "__main__":
    main()