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
import csv
from tabulate import tabulate
import sys


class ProgramUI:
    def __init__(self):
        self.menu_name = str
        self.menu = list[list]
        self.menu_id = list[int]
        self.prompt = str
        self.option = str

    # OPERATOR OVERLOADING
    def __len__(self):
        return len(self.menu)

    # UI FUNCTIONS
    # Display Menu Options
    def start_ui(self):
        self.menu_id = list(range(len(self.menu)))
        print(
            f"|====---- {self.menu_name.upper()} ----====|",
            tabulate(
                self.menu,
                showindex=list(map(lambda x: x + 1, self.menu_id)),
                tablefmt="simple_grid",
            ),
            sep="\n",
        )
        # Option Selection
        _ = self.option_solver
        global ui_transfer 
        ui_transfer = _


    # INPUT SOLVERS
    # Option Input Solver
    def option_solver(self, prompt="Select Option Number: "):
        while True:
            menu_input = input(prompt)
            if 0 < int(menu_input) <= (len(self.menu)):
                return self.menu[int(menu_input) - 1][0])
            print("Invalid Input, Please choose a valid option number")
            continue
    
    # File Name Input Solver
    ...

class MainMenu(ProgramUI):
    def __init__(self):
        super().__init__()
        self.menu_name = "Main Menu"
        self.menu = [
            ["New Inventory"],
            ["Manage Existing Inventory"],
            ["Exit Program"],
        ]


class NewInventoryMenu(ProgramUI):
    def __init__(self):
        super().__init__()
        self.menu_name = "New Inventory"
        self.menu = [
            ["Create a New Inventory"],
            ["Back to Main Menu"],
        ]

    def new_inventory(self):
        self.inventory_filename = input("Name your new inventory: ")
        with open(f"{self.inventory_filename}.csv") as file:
            file.save()

        # insert csv saving here
        # after creation, open the inventory


class OpenInventoryMenu(ProgramUI):
    ...


class InventoryMenu(ProgramUI):
    ...





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
        Figlet().renderText('Food Inventory Management') +
        "\n" +
        "----- \"A handy inventory management for your food\" -----" + "\n"
        )
    # INITIALIZATION AND MAIN MENU
    ui_transfer = str
    fim_mainmenu = MainMenu()
    fim_newinvmenu = NewInventoryMenu()
    fim_openinvmenu = OpenInventoryMenu()
    fim_invmenu = InventoryMenu()
    fim_mainmenu.start_ui()

    match ui_transfer:
            # Main Menu
            case "New Inventory":
                fim_newinvmenu.start_ui()
            case "Manage Existing Inventory":
                fim_openinvmenu.start_ui()
            case "Exit Program":
                return sys.exit("\n----------Program Closed----------\n")
            # New Inventory Menu
            case "Create a New Inventory":
                fim_newinvmenu.new_inventory()
            case _:
                return sys.exit("\n!!!---Program Error, Exiting---!!!\n")


if __name__ == "__main__":
    main()
