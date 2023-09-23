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
import datetime
import os

class ProgramMenu:
    def __init__(self, ui_name, ui_menu):
        self.ui_name: str = ui_name
        self.ui_menu: list[list] = ui_menu
        self.option = int

    def __len__(self, input_list: list):
        return len(input_list)
    
    def options_table(self):
        print(f"|=====----- {self.ui_name.upper()} -----=====|")
        print(
            tabulate(self.ui_menu, showindex=list(map(lambda x:x+1, list(range(len(self.ui_menu))))),
                     tablefmt='simple_grid')
            )
        
    def input_option(self):
        while True:
            try:
                user_input = input(f'===> {self.ui_name.upper()} - Input Option Number: ')
                if 0 < int(user_input) <= len(self.ui_menu):
                    return self.ui_menu[int(user_input) - 1][0]
                print("Invalid option, select a valid option number")
                continue
            except ValueError:
                print("Invalid option, select a valid option number")
                continue

class Inventory:
    def __init__(self, inv_name: str, storage: list[list]):
        self.inv_name = inv_name
        self.storage = storage

    def __len__(self, input_list: list):
        return len(input_list)

    def inventory_table(self):
        print(f"|=====----- {self.inv_name.upper()} -----=====|")
        print(
            tabulate(self.storage, showindex=list(map(lambda x:x+1, list(range(len(self.storage))))),
                     tablefmt='simple_grid')
            )
        
    def item_option(self):
        while True:
            try:
                user_input = input(f'===> {self.inv_name.upper()} - Input Item Number: ')
                if 0 < int(user_input) <= len(self.storage):
                    print("hi")
                print("Invalid item, select a valid item number")
                continue
            except ValueError:
                print("Invalid item, select a valid item number")
                continue
        
    


def main():
    # Initialization
    main_menu = ProgramMenu("Main Menu", [
        ['New Inventory'],
        ['Manage Existing Inventory'],
        ['Exit Program']
    ])
    # saved_inventories_menu = ProgramMenu("My Inventories")
    selected_option = str
    # Splash Screen
    print(Figlet().renderText('Food Inventory Management'))
    print('----- \"A handy inventory management program for your food\" -----\n')
    main_menu.options_table()
    selected_option = main_menu.input_option()
    # Options
    match selected_option:
        case "Back to Main Menu":
            main_menu.options_table()
            selected_option = main_menu.input_option()
        case "New Inventory":
            print("hi!")
        case "Manage Existing Inventory":
            directory = filter(lambda x:, list(os.listdir()))
        case "Exit Program":
            sys.exit("\n|----- Program Closed -----|\n")
        case _:
            sys.exit("\n|----- PROGRAM ERROR, EXITING -----|\n")


if __name__ == "__main__":
    main()
