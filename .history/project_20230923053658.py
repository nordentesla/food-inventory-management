'''
FOOD INVENTORY MANAGEMENT
by Jose Nichole C. Galenzoga

Final Python project for Harvard University's CS50P course
    Requirements:
        1. main function must be in a file called project.py
        2. at least 3 custom functions other than main with the same
            indentation as main (not nested in any class or other functions)
        3. must have test functions called test_project.py with "test_" in
            front of the custom_function to be tested in the main file
            Ex.: test_custom_function()
        4. welcome to implement classes and functions aside from the
            mentioned requirements
        5. implementing the project should entail more time and effort
            compared to each problem sets in the course
        6. any pip-installable libraries should be listed, one per line
            in a file called 'requirements.txt'
'''


from pyfiglet import Figlet
import csv
from tabulate import tabulate
import sys

class ProgramMenu:
    def __init__(self, name, menu):
        self.name: str = name
        self.menu: list[list] = menu
        self.option = int

    def __len__(self, input_list: list):
        return len(input_list)
    
    def options_table(self):
        print(f"|====---- {self.name.upper()} ----====|")
        print(
            tabulate(self.menu, showindex=list(map(lambda x:x+1, list(range(len(self.menu))))),
                     tablefmt='simple_grid')
            )
        
    def input_option(self):
        user_input = input('Select Option Number: ')
        while True:
            if 0 < int(user_input) <= len(self.menu):
                global selected_option
                selected_option = self.menu[int(user_input) - 1][0]
                break
            print("Invalid option, select a valid option number")
            continue
        

def main():
    # Initialization
    main_menu = ProgramMenu("Main Menu", [
        ['New Inventory'],
        ['Manage Existing Inventory'],
        ['Exit Program']
    ])
    selected_option = str
    # Splash Screen
    print(Figlet().renderText('Food Inventory Management'))
    print('\n----- \"A handy inventory management program for your food\" -----\n')
    main_menu.options_table()
    main_menu.input_option()
    # Options
    match selected_option:
        # Common Options
        case "Back to Main Menu":
            main_menu.options_table()
            main_menu.input_option()
        # Main Menu Options
        case "New Inventory":
            ...
        case "Manage Existing Inventory":
            ...
        case "Exit Program":
            sys.exit("\n|----- Program Closed -----|\n")
        case _:
            sys.exit("\n|----- PROGRAM ERROR: EXITING -----|\n")


if __name__ == "__main__":
    main()
