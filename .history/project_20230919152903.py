# FOOD INVENTORY MANAGEMENT
"""
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
"""


from pyfiglet import Figlet
import re
import csv
from tabulate import tabulate


class ProgramUI:
    def __init__(self):
        self.menu = 

    def menu_display(self):
        print(tabulate(self.menu))

    def menu_option_solver(self, prompt):
        while True:
            self.menu_input = input(prompt)
            try:
                if int(self.menu_input) in self.menu:
                    return self.menu[int(self.menu_input)]
                print("Invalid input: Select a valid menu number")
                continue
            except:
                continue


class MainMenu(ProgramUI):
    def __init__(self):
        super().__init__()
        self.menu = {
            1:"New Inventory",
            2:"Manage Existing Inventory",
            3:"Exit Program",
        }

def new_inventory_menu(self):
    inventory_file = input_solver("Name your new inventory: ")
    # insert csv saving here
    # after creation, open the inventory

def open_inventory_menu(self):
    # will display existing inventories
    # select inventory
    open_inventory_menu_options = ["Back to Main Menu"]

def inventory_menu(self):
    # Displays current inventory
    inventory_menu_options = [
        "Add New Item",
        "Remove Item",
        "Edit Item",
        "Export as PDF",
    ]


def main():
    # SPLASH SCREEN
    print(Figlet().renderText("Food Inventory Management"))
    # INITIALIZATION AND MAIN MENU
    fim_main_menu = MainMenu()
    fim_main_menu.menu_display()
    fim_main_menu.menu_option_solver()


def input_solver(prompt):
    while True:
        user_input = input(prompt)
        if user_input == re.search(r"^\w+"):
            return user_input
        print("Invalid input: Alphanumeric and underscore characters only")
        continue


if __name__ == "__main__":
    main()
