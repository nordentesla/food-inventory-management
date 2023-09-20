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
import sys


class ProgramUI:
    def __init__(self):
        self.menu = list[dict]
        self.menu_id = list[int]
        self.prompt = str
        self.option = str

    # OPERATOR OVERLOADING
    def __len__(self):
        return len(self.menu)

    # UI FUNCTIONS
    # Display Menu Options
    def menu_display(self):
        print(
            "|==-- Options --==|",
            tabulate(
                self.menu,
                showindex=list(map(lambda x: x + 1, list(range(len(self.menu))))),
                tablefmt="simple",
            ),
            sep="\n",
        )
        # Option Selection
        self.option = self.option_solver()
        match self.option:
            case "New Inventory":
                return self.new_inventory_menu()
            case "Manage Existing Inventory":
                return self.open_inventory_menu()
            case "Exit Program":
                return sys.exit("\n----------Program Closed----------\n")
            case _:
                return sys.exit("\n!!!---Program Error, Exiting---!!!\n")

    # Display Menu Input Solver
    def option_solver(self, prompt="Select Option Number: "):
        while True:
            menu_input = input(prompt)
            if 0 < int(menu_input) <= (len(self.menu)):
                return self.menu[int(menu_input) - 1][0]
            print("Invalid Input, Please choose a valid option number")
            continue




class MainMenu(ProgramUI):
    def __init__(self):
        super().__init__()
        self.menu = [
            ["New Inventory"],
            ["Manage Existing Inventory"],
            ["Exit Program"],
        ]


def new_inventory(self):
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
    print(
        Figlet().renderText("Food Inventory Management") +
        "\n" +
        ""
        )
    # INITIALIZATION AND MAIN MENU
    fim_main_menu = MainMenu()
    fim_main_menu.menu_display()


def input_solver(prompt):
    while True:
        user_input = input(prompt)
        if user_input == re.search(r"^\w+"):
            return user_input
        print("Invalid input: Alphanumeric and underscore characters only")
        continue


if __name__ == "__main__":
    main()
