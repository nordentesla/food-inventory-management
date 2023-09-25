"""
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
"""


from pyfiglet import Figlet
import csv
from tabulate import tabulate
import sys
import datetime
import os
import re


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
            tabulate(
                self.ui_menu,
                showindex=list(map(lambda x: x + 1, list(range(len(self.ui_menu))))),
                tablefmt="simple_grid",
            )
        )
        print("")

    def input_option(self):
        while True:
            try:
                user_input = input(
                    f"===> {self.ui_name.upper()} - Input Option Number: "
                )
                if int(user_input) == 0:
                    return "Back to Main Menu"
                elif 0 < int(user_input) <= len(self.ui_menu):
                    print("")
                    return self.ui_menu[int(user_input) - 1][0]
                print("!!! Invalid option, select a valid option number !!!")
                continue
            except ValueError:
                print("!!! Invalid option, select a valid option number !!!")
                continue

    def inventory_option(self):
        ...

    def item_option(self):
        ...


class Inventory:
    def __init__(self, inv_name: str, storage: list[list] = [[]]):
        self.inv_name = inv_name
        self.storage = storage
        self.filename_with_extension = str
        self.match = str

    def __len__(self, input_list: list):
        return len(input_list)

    def inventory_table(self):
        self.storage = []
        with open(f"./inventories/{self.inv_name}.csv") as file:
            my_csv = csv.reader(file)
            for row in my_csv:
                self.storage.append(row)
        print(f"|=====----- {self.inv_name.upper()} -----=====|")
        print(
            tabulate(
                self.storage,
                tablefmt="simple_grid",
                headers="firstrow",
                showindex=list(
                    map(lambda x: x + 1, list(range(len(self.storage) - 1)))
                ),
            )
        )
        print("")

    def item_option(self):
        while True:
            try:
                user_input = input(
                    f"===> {self.inv_name.upper()} - Select Item Number: "
                )
                if 0 < int(user_input) <= len(self.storage):
                    print("WIP")
                print("Invalid item, select a valid item number")
                continue
            except ValueError:
                print("Invalid item, select a valid item number")
                continue


def main():
    # Initialization
    main_menu = ProgramMenu(
        "Main Menu",
        [["New Inventory"], ["Manage Existing Inventory"], ["Exit Program"]],
    )

    # saved_inventories_menu = ProgramMenu("My Inventories")
    selected_option: str = "Main Menu"

    # Program Main Loop
    while True:
        match selected_option:
            case "Main Menu":
                splash_screen()
                main_menu.options_table()
                selected_option = main_menu.input_option()
            case "Back to Main Menu":
                selected_option = "Main Menu"
            case "New Inventory":
                # WIP
                sys.exit("\nWORK IN PROGRESS\n")
            case "Manage Existing Inventory":
                # Read local directory for .csv files
                csv_files = list_saved_csvs("./inventories", remove_extension_from_file)

                # Create a ProgramMenu object for display of all .csv files in the directory
                inventory_menu = ProgramMenu("My Inventories", [csv_files])
                inventory_menu.options_table()

                # Prompts the user for a specific inventory and then reads the .csv inventory file
                inventory_file = inventory_menu.input_option()
                current_inventory = Inventory(inventory_file)
                current_inventory.inventory_table()

                # Creates an inventory object for the opened .csv file for modification/viewing
                current_inventory = Inventory(inventory_file)
                selected_option = "Inventory Menu"
            case "Inventory Menu":
                # WIP
                sys.exit("\n!!! WORK IN PROGRESS !!!\n")
            case "Exit Program":
                sys.exit("\n|----- Program Closed -----|\n")
            case _:
                sys.exit("\n|----- PROGRAM ERROR: OPTION MISMATCH -----|\n")


def splash_screen():
    """
    Prints the program splash screen
    """
    print(Figlet().renderText("Food Inventory Management"))
    print('----- "A handy inventory management program for your food" -----\n')


def list_saved_csvs(my_path: str, map_function=None):
    """
    List all the saved CSV in the current directory
    map_function is optional, uses map to apply function to list items
    """
    file_list = list(
        filter(lambda x: x.endswith(".csv"), list(os.listdir(path=my_path)))
    )
    if map_function != None:
        file_list = list(map(map_function, file_list))
        return file_list
    return file_list


def remove_extension_from_file(filename: str):
    """
    Function to remove extension from the filename of a file
    """
    if matches := re.search(r"^(.+)(\.\w+)$", f"{filename}", flags=re.IGNORECASE):
        return matches.group(1)


if __name__ == "__main__":
    main()
