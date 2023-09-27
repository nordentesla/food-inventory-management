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
from re import search
from time import sleep


class ProgramMenu:
    def __init__(self, ui_name, ui_menu):
        self.ui_name: str = ui_name
        self.ui_menu: list[list] = ui_menu
        self.option = int

    def __len__(self, input_list: list):
        return len(input_list)

    def display_options(self):
        print("-------------------------------------------------\n")
        print(f"|=====----- {self.ui_name.upper()} -----=====|")
        print(
            tabulate(
                self.ui_menu,
                showindex=list(map(lambda x: x + 1, list(range(len(self.ui_menu))))),
                tablefmt="simple_grid",
            )
        )

    def input_option(self):
        while True:
            try:
                user_input = input(
                    f"===> {self.ui_name.upper()} - Input Option Number: "
                )
                if user_input == "0":
                    return "Main Menu"
                elif 0 < int(user_input) <= len(self.ui_menu):
                    print("")
                    return self.ui_menu[int(user_input) - 1][0]
                print("!!! Invalid option, select a valid option number !!!")
                continue
            except ValueError:
                print("!!! Invalid option, select a valid option number !!!")
                continue


class Inventory:
    def __init__(self, inv_name: str, storage: list[list] = [[]]):
        self.inv_name = inv_name
        self.storage = storage
        self.filename_with_extension = str
        self.match = str

    def __str__(self):
        return f"\n\nINVENTORY: {self.inv_name}, CONTAINING {self.storage[0]}\n\n"

    def __len__(self, input_list: list):
        return len(input_list)

    def display_inventory(self):
        self.storage = []
        with open(f"./inventories/{self.inv_name}.csv") as file:
            my_csv = csv.reader(file)
            for row in my_csv:
                self.storage.append(row)
        print("-------------------------------------------------\n")
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

    def special_option(self):
        print("")
        print(f"{self.inv_name.upper()} OPTIONS:\n")
        print(
            f"Type 'a' => Add an Item to {self.inv_name.upper()}",
            f"Type 'r' => Remove an Item from {self.inv_name.upper()}",
            f"Type 'e' => Export {self.inv_name.upper()} list as PDF",
            "Type 'i' => Back to Other Inventories",
            "Type '0' => Back to Main Menu",
            sep="\n", end="\n\n\n"
            )
        while True:
            try:
                user_input = input(
                    f"===> {self.inv_name.upper()} - Type the Option: "
                    )
                print("")
                match user_input:
                    case "a":
                        ...
                    case "r":
                        ...
                    case "e":
                        ...
                    case "i":
                        return "Manage Existing Inventory"
                    case "0":
                        return "Main Menu"
                    case _:
                        print("!!! Invalid option, select a valid option number !!!\n")
                        continue
            except KeyboardInterrupt:
                return "Exit Program"
            
    def save_new_inventory(self):
        WIP()

    def item_option(self):
        while True:
            try:
                user_input = input(
                    f"===> {self.inv_name.upper()} - Select Item Number: "
                )
                if 0 < int(user_input) <= len(self.storage):
                    return self.storage[0][int(user_input)]
                print("Invalid item, select a valid item number")
                continue
            except ValueError:
                print("Invalid item, select a valid item number")
                continue

    @property
    def inv_name(self):
        return self._inv_name
    
    @inv_name.setter
    def inv_name(self, inv_name):
        if not search(r"^(\w)+$", inv_name):
            raise ValueError("!!! Invalid inventory name !!!".upper())
        self._inv_name = inv_name
        

def main():
    # Initial selection
    main_menu = ProgramMenu(
        "Main Menu",
        [["New Inventory"], ["Manage Existing Inventory"], ["Exit Program"]],
    )
    splash_screen()
    selected_option: str = "Main Menu"
    # Program Main Loop
    while True:
        try:
            match selected_option:
                case "Main Menu":
                    main_menu.display_options()
                    selected_option = main_menu.input_option()

                case "New Inventory":
                    while True:
                        try:
                            current_inventory = Inventory(
                                input("Enter new inventory name: ".upper())
                                    )
                            with open(
                                f"./inventories/{current_inventory.inv_name}.csv", "x"
                                ) as new_inv_file:
                                csv_writer = csv.writer(new_inv_file)
                                csv_writer.writerow(["Item", "Expiry Date", "Quantity"])
                            break
                        except (ValueError, NameError):
                            print("\n!!! Alphanumeric characters and underscore only !!!\n")
                            continue
                        except FileExistsError:
                            print("\n\n!!! Inventory already exists, please enter a different name !!!\n\n")
                            continue
                    print("\n\n", current_inventory.inv_name.upper(), " inventory created!", sep="")
                    sleep(1)
                    print("Loading new inventory, Please wait...\n".upper())
                    sleep(2.5)
                    selected_option = "Inventory Menu"
                    selected_inventory_file = current_inventory.inv_name

                case "Manage Existing Inventory":
                    # Read local directory for .csv files, and
                    csv_files = list_saved_csvs(
                        "./inventories", remove_extension_from_file
                    )

                    # Create a ProgramMenu object for display of all .csv files in the directory
                    my_inventories = ProgramMenu("My Inventories", csv_files)
                    my_inventories.display_options()
                    print("** Other Options: Type '0' to go back to Main Menu **\n")

                    # Initializes selected inventory file and directs to inventory menu
                    selected_inventory_file = my_inventories.input_option()
                    if selected_inventory_file == "Main Menu":
                        print("")
                        selected_option = "Main Menu"
                    else:
                        selected_option = "Inventory Menu"

                case "Inventory Menu":
                    current_inventory = Inventory(selected_inventory_file)
                    current_inventory.display_inventory()
                    if option := current_inventory.special_option():
                        selected_option = option

                case "Exit Program":
                    sys.exit("\n\n|----- Program Closed -----|\n")

                case _:
                    sys.exit("\n|----- PROGRAM ERROR: OPTION MISMATCH -----|\n")
        except KeyboardInterrupt:
            sys.exit("\n\n|----- Program Force Closed -----|\n")


def splash_screen():
    """
    Prints the program splash screen
    """
    print(Figlet().renderText("Food Inventory Management"))
    print('----- "A handy inventory management program for your food" -----\n')
    print("** by ~nordentesla~ **\n")


def list_saved_csvs(my_path: str, map_function=None):
    """
    List all the saved CSV in the current directory
    map_function is optional, uses map to apply function to list items
    Makes a list of files a list within itself i.e.: [[item1], [item2]] for tabulate library
    """
    file_list = list(
        filter(
            lambda x: x.endswith(".csv") and (["Item","Expiry Date","Quantity"] in csv.reader(f"{x}")), 
               list(os.listdir(path=my_path)),)
    )
    if map_function != None:
        modified_file_list = []
        for item in file_list:
            modified_file_list.append([map_function(item)])
        return modified_file_list
    return file_list


def remove_extension_from_file(filename: str):
    """
    Function to remove extension from the filename of a file
    """
    if matches := re.search(r"^(.+)(\.\w+)$", f"{filename}", flags=re.IGNORECASE):
        return matches.group(1)


def WIP():
    sys.exit("\n--- !!! WORK IN PROGRESS !!! ---\n")


if __name__ == "__main__":
    main()
