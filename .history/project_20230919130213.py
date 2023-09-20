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
import sys


class ProgramUI:
    def splash_screen(self):
        print(Figlet().renderText("Food Inventory Management"))

    def main_menu(self):
        main_menu_options = [
            "New Inventory", "Manage Existing Inventory",
            "Export Inventory as PDF"
        ]
        # insert 

    def new_inventory_menu(self):
        inventory_file = input_solver("Name your new inventory: ")
        # insert csv saving here

    def open_inventory_menu(self):
        # will display existing inventories
        


def main():
    fim_program = ProgramUI()
    fim_program.splash_screen()
    fim_program.main_menu()

def main_menu():
    """
    Options Menu:
    x. Add New Item
    x. Remove Item
    x. Edit Item
    x. Export as PDF
    """

def input_solver(prompt):
    while True:
        user_input = input(prompt)
        if user_input == re.search(r"^\w+"):
            return user_input
        print("Invalid input: Alphanumeric and underscore characters only")
        continue

def menu_option_solver(prompt):
    while True:
        menu_input = input(prompt)
        if menu_input == re.search(r"^\d$"):
            return menu_input
        print("Invalid input: Select a valid menu number")
        continue
        


if __name__ == "__main__":
    main()