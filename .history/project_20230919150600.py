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


class ProgramUserInterface:
    def __init__(self, menu: list[str]):
        self.menu = menu

    def menu_option_solver(prompt):
        while True:
            menu_input = input(prompt)
            try:
                if menu_input == re.search(r"^\d$"):
                    return menu_input
                print("Invalid input: Select a valid menu number")
                continue
            except:
                continue

class MainMenu(ProgramUserInterface):
    def main_menu(self):
        main_menu_options = [
            "New Inventory",
            "Manage Existing Inventory",
            "Exit Program",
        ]

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
    # PROGRAM INITIALIZATION
    fim_program = ProgramUI()
    # SPLASH SCREEN
    print(Figlet().renderText("Food Inventory Management"))
    fim_program.main_menu()


def input_solver(prompt):
    while True:
        user_input = input(prompt)
        if user_input == re.search(r"^\w+"):
            return user_input
        print("Invalid input: Alphanumeric and underscore characters only")
        continue





if __name__ == "__main__":
    main()
