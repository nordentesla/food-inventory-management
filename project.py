"""
FOOD INVENTORY MANAGEMENT
by Jose Nichole C. Galenzoga
A.K.A.: nordentesla (Northwind Creative)

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
from time import sleep
from fpdf import FPDF
import pandas as pd
import numpy as np


class ProgramMenu:
    """
    ProgramMenu class, blueprint for the different menus
    that provides a simple GUI in the terminal
    """

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
            ),
            "\n",
        )

    def input_option(self):
        while True:
            try:
                user_input = input(
                    f"===> {self.ui_name.upper()} - Input Option Number: "
                )
                if user_input == "0":
                    print("")
                    sleep(0.5)
                    return "Main Menu"
                elif 0 < int(user_input) <= len(self.ui_menu):
                    print("")
                    sleep(0.5)
                    return self.ui_menu[int(user_input) - 1][0]
                print("!!! Invalid option, select a valid option number !!!")
                continue
            except ValueError:
                print("!!! Invalid option, select a valid option number !!!")
                continue


class Inventory:
    """
    Class to initialize an inventory object for data manipulation
    """

    def __init__(self, inv_name: str, storage: list[list] = [[]]):
        self.inv_name = inv_name
        self.storage = storage
        self.filename_with_extension = str
        self.match = str
        self.item: list = [str, datetime, int]

    def __str__(self):
        return f"\n\nINVENTORY: {self.inv_name}, CONTAINING {self.storage[0]}\n\n"

    def __len__(self, input_list: list):
        return len(input_list)

    def display_inventory(self):
        self.storage = []
        with open(f"./inventories/{self.inv_name}.csv") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                self.storage.append(row)
        # Prints the following:
        # Title, inventory table, table description, and inventory menu options
        print(
            "-------------------------------------------------\n",
            f"|=====----- {self.inv_name.upper()} -----=====|",
            tabulate(
                self.storage,
                tablefmt="simple_grid",
                headers="firstrow",
                showindex=list(
                    map(lambda x: x + 1, list(range(len(self.storage) - 1)))
                ),
            ),
            f"!--- {self.inv_name} has {len(self.storage)-1} item(s) ---!".upper(),
            "",
            f"{self.inv_name.upper()} OPTIONS:",
            f"Type 'a' => Add an Item to {self.inv_name.upper()}",
            f"Type 'r' => Remove an Item from {self.inv_name.upper()}",
            f"Type 'e' => Export \"{self.inv_name.upper()}\" inventory list as PDF",
            f"Type 'd' => Delete \"{self.inv_name.upper()}\" Inventory",
            "Type 'i' => Back to My Inventories",
            "Type '0' => Back to Main Menu",
            sep="\n",
            end="\n\n\n",
        )


    def special_option(self):
        while True:
            try:
                user_input = input(
                    f"===> Inventory Menu: {self.inv_name.upper()} - Type the Option: "
                )
                print("")
                match user_input:
                    case "a":
                        return self.add_item()
                    case "r":
                        return self.remove_item()
                    case "e":
                        return self.export_pdf()
                    case "d":
                        return self.delete_inventory()
                    case "i":
                        return "Manage Existing Inventory"
                    case "0":
                        return "Main Menu"
                    case _:
                        print("!!! Invalid option, type a valid option !!!\n")
                        continue
            except KeyboardInterrupt:
                return "Exit Program"

    def add_item(self):
        # item name input processing
        while True:
            item_name = input("What is the name of the item? ").strip().title()
            if re.search(r"^[A-Za-z]\w{2}[\w ]*$", item_name):
                confirm_item_name = input(
                    f"Confirm Item Name: '{item_name}'?\n\n[Y/N]:"
                ).lower()
                match confirm_item_name:
                    case "y":
                        break
                    case "n":
                        continue
                    case _:
                        print("Invalid input, Y or N only")
                        continue
            else:
                print(
                    "Item name must be 3 characters or more and starts with 2 letters".upper()
                )
        # item expiry date input processing
        while True:
            try:
                item_expiry_date = input(
                    "What is the expiry date of the item?\n\nInput Date YYYY-MM-DD or YYYY-MM: "
                ).strip()
                # regex for validating dates to be later than year 2023, capturing year, month, and day data
                if matches := re.search(
                    r"^(2[0-1](2[3-9]|[3-9]\d))-(0\d|1[0-2])(-([0-2]\d|3[0-1]))*$",
                    item_expiry_date,
                ):
                    expiry_year = int(matches.group(1))
                    expiry_month = int(matches.group(3))
                    # if no "day" is indicated, day will be set to "01"
                    if matches.group(5) == None:
                        expiry_day = 1
                    else:
                        expiry_day = int(matches.group(5))
                    # validation if the input expiry date is in the future
                    # invalid date will prompt the user input again
                    if (
                        item_expiry_date := datetime.date(
                            expiry_year, expiry_month, expiry_day
                        )
                    ) > datetime.date.today():
                        item_expiry_date = str(item_expiry_date)
                    else:
                        raise ValueError(
                            "Invalid expiry date: date should be later than today"
                        )
                    confirm_expiry_date = input(
                        f"Confirm Expiry Date: '{item_expiry_date}'?\n\n[Y/N]:"
                    ).lower()
                    match confirm_expiry_date:
                        case "y":
                            break
                        case "n":
                            continue
                        case _:
                            print("Invalid input, Y or N only")
                            continue
                else:
                    print("Invalid expiry date, Check your format")
            except ValueError:
                continue
        # item name quantity processing
        while True:
            item_count = input(
                f"How many '{item_name}' item do you want to add to {self.inv_name}? "
            ).strip()
            # max item should be 999
            if re.search(r"^\d{0,2}[1-9]$", item_count):
                item_count = int(item_count)
                confirm_item_count = input(
                    f'Confirm Item to be Added "{item_expiry_date}"?\n\n[Y/N]:'
                ).lower()
                match confirm_item_count:
                    case "y":
                        break
                    case "n":
                        continue
                    case _:
                        print("Invalid input, Y or N only")
                        continue
            else:
                print("Invalid quantity, input a number more than 0")
                continue

        current_item_list = pd.read_csv(f"./inventories/{self.inv_name}.csv")
        item_to_add = pd.DataFrame([{"Item": item_name, "Expiry Date": item_expiry_date, "Quantity": item_count}])
        print(current_item_list)
        print("", item_to_add, sep="\n")

        # join inputs into an item list
        # append inputed list into the file
        # print a notice that the file is saved
        # print the item list of the inventory
        WIP()
        # addition of item done, returns to current inventory menu
        return "Inventory Menu"

    def remove_item(self):
        # open the csv file
        # parse the csv file
        # select item number from the inventory
        # ask user for input for quantity to be removed
        # verify if the input is a valid integer, and less than the item quantity
        # prompt the user if they wish to proceed with the inputted quantity to be removed
        # subtract the quantity from the item
        # if the item yields to 0, remove the item from the .csv file
        WIP()
        return "Inventory Menu"

    def export_pdf(self):
        while True:
            confirm_create_pdf: str = (
                input(f"Do you want to export {self.inv_name.upper()} as PDF? [Y/N]: ")
                .lower()
                .strip()
            )
            match confirm_create_pdf:
                case "y":
                    pdf_maker(self.inv_name, self.storage)
                    loading_notices(
                        f"{self.inv_name} inventory exported as pdf",
                        'pdf file saved at "saved-pdfs" folder',
                        "returning to inventory menu...",
                    )
                    return "Inventory Menu"
                case "n":
                    loading_notices(
                        "export as pdf cancelled",
                        "returning to inventory menu...",
                    )
                    return "Inventory Menu"
                case _:
                    print('\nInvalid option "y" for Yes and "n" for No only\n'.upper())
                    continue

    def delete_inventory(self):
        while True:
            confirm_delete: str = (
                input(
                    f"Are you sure you want to delete {self.inv_name.upper()}? [Y/N]: "
                )
                .lower()
                .strip()
            )
            match confirm_delete:
                case "y":
                    delete_csv_file(self.inv_name)
                    loading_notices(
                        f"{self.inv_name} deleted!",
                        "returning to my manage existing inventories menu",
                    )
                    return "Manage Existing Inventory"
                case "n":
                    loading_notices(
                        f"deletion cancelled",
                        f"returning to {self.inv_name} options menu",
                    )
                    return "Inventory Menu"
                case _:
                    print('\nInvalid option "y" for Yes and "n" for No only\n'.upper())
                    continue

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
        if not re.search(r"^(\w)+$", inv_name):
            raise ValueError("!!! Invalid inventory name !!!".upper())
        self._inv_name = inv_name


def main():
    # Initial selection
    main_menu = ProgramMenu(
        "Main Menu",
        [
            ["New Inventory"],
            ["Manage Existing Inventory"],
            ["About this Program"],
            ["Exit Program"],
        ],
    )
    splash_screen()
    # selected_
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
                            # Prompt for inventory name
                            current_inventory = Inventory(
                                input("Enter new inventory name: ".upper())
                            )
                            confirm_create = (
                                input(
                                    f"Do you want to create {current_inventory.inv_name}? [Y/N]: "
                                )
                                .lower()
                                .strip()
                            )
                            if confirm_create == "y":
                                # inventory creation
                                create_csv_file(current_inventory.inv_name)
                                loading_notices(
                                    f'"{current_inventory.inv_name}" inventory created',
                                    f"opening {current_inventory.inv_name} inventory...",
                                )
                                selected_option = "Inventory Menu"
                                selected_inventory_file = current_inventory.inv_name
                                break
                            elif confirm_create == "n":
                                # cancellation of creation, returns to main menu
                                loading_notices(
                                    f"inventory creation cancelled",
                                    f"returning to main menu...",
                                )
                                selected_option = "Main Menu"
                                break
                            else:
                                # invalid confirmation (y/n) for inventory creation
                                print(
                                    '\nInvalid option "y" for Yes and "n" for No only\n'.upper()
                                )
                                continue
                        except (ValueError, NameError):
                            print(
                                "\n!!! Alphanumeric characters and underscore only !!!\n"
                            )
                            continue
                        except FileExistsError:
                            print(
                                "\n\n!!! Inventory already exists, please enter a different name !!!\n\n"
                            )
                            continue

                case "Manage Existing Inventory":
                    # Read local directory for .csv files
                    csv_files = list_saved_inventory_csvs(
                        "./inventories", remove_extension_from_file
                    )
                    # if no inventories are saved to "./inventories"
                    if csv_files == None:
                        selected_option = "Main Menu"
                        continue

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

                case "About this Program":

                    def about():
                        """
                        The program is called Food Inventory
                        Management. It is a program that is
                        used to manage food inventory in the
                        household. This was created to fulfill
                        the requirements of Harvard University's
                        CS50P final project.

                        See ReadMe for more information:
                        https://github.com/nordentesla/food-inventory-management
                        """

                    try:
                        print(about.__doc__)
                        loading_notices(
                            "Press Ctrl + C to go back to main menu",
                            "(Will automatically go to main menu after 10 seconds)",
                        )
                        sleep(9)
                        selected_option = "Main Menu"
                    except KeyboardInterrupt:
                        selected_option = "Main Menu"

                case "Exit Program":
                    sys.exit(
                        "\n\n|----- Program Closed, Thank you for using the Program! -----|\n\n"
                    )

                case _:
                    sys.exit("\n|----- PROGRAM ERROR: OPTION MISMATCH -----|\n")
        except KeyboardInterrupt:
            sys.exit("\n\n|----- Program Force Closed -----|\n")


def splash_screen():
    """
    Prints the program splash screen
    """
    print(
        Figlet().renderText("Food Inventory Management"),
        '----- "A handy inventory management program for your food" -----\n',
        sep="\n",
    )


def create_csv_file(filename):
    with open(f"./inventories/{filename}.csv", "x") as new_inv_file:
        csv_writer = csv.writer(new_inv_file)
        csv_writer.writerow(["Item", "Expiry Date", "Quantity"])


def delete_csv_file(filename):
    """
    created to prevent carrying over the selected_option = 'd'
    when declining the delete prompt for the current inventory
    """
    os.remove(f"./inventories/{filename}.csv")
    return "Manage Existing Inventory"


def list_saved_inventory_csvs(my_path: str, map_function=None):
    """
    List all the saved CSV in the current directory
    map_function is optional, uses map to apply function to list items
    Makes a list of files a list within itself i.e.: [[item1], [item2]] for tabulate library
    """
    try:
        # first filter: all .csv file in the directory
        file_list = list(
            filter(lambda file: file.endswith(".csv"), list(os.listdir(path=my_path)))
        )
        # second filter: all .csv file should have a valid header:
        file_list = list(
            filter(
                lambda file: re.search(
                    r"^Item,\"?Expiry Date\"?,Quantity\n?$",
                    list(open(f"./inventories/{file}", "r"))[0],
                ),
                file_list,
            )
        )
        # file list modifier
        if map_function != None:
            modified_file_list = []
            for item in file_list:
                modified_file_list.append([map_function(item)])
            return sorted(modified_file_list)
        return sorted(file_list)
    except IndexError:
        loading_notices("no inventories saved", "returning to main menu...")
        return None


def pdf_maker(pdf_filename: str, inventory_list: list):
    """
    main function for pdf creation of inventories when
    export as PDF option is selected
    """
    # PDF initialization
    my_pdf = FPDF()
    my_pdf.set_author("Northwind Creative")
    my_pdf.set_font(family="helvetica", size=30)
    # creating PDF page and content
    my_pdf.add_page()
    my_pdf.cell(txt=f"{pdf_filename} items".title(), center=True)
    my_pdf.ln(15)
    # creates table from data, taken from FPDF2 documentation, for further study
    my_pdf.set_font(family="helvetica", size=15)
    if len(inventory_list) == 1:
        # for inventory with no items
        my_pdf.ln(10)
        my_pdf.set_font(family="helvetica", size=20, style="B")
        my_pdf.cell(
            txt="! no items in this inventory !".upper(),
            center=True,
        )
        my_pdf.ln(30)
    else:
        # for inventory with valid items
        with my_pdf.table() as pdf_table:
            for data_row in inventory_list:
                row = pdf_table.row()
                for datum in data_row:
                    row.cell(datum)
        my_pdf.ln(4)
        my_pdf.set_font(family="helvetica", size=15)
        my_pdf.cell(txt="!-- end of the list --!".upper(), center=True)
        my_pdf.ln(4)
    # program signature
    my_pdf.ln(4)
    my_pdf.set_font(family="helvetica", size=10)
    my_pdf.cell(
        txt="Created with Food Inventory Management by nordentesla / Northwind Creative",
        center=True,
    )
    # saving PDF file
    my_pdf.output(name=f"./saved-pdfs/{pdf_filename}.pdf")


def remove_extension_from_file(filename: str):
    """
    Function to remove extension from the filename of a file
    """
    if matches := re.search(r"^(.+)(\.\w+)$", f"{filename}", flags=re.IGNORECASE):
        return matches.group(1)


# UI TEXT NOTICES
def loading_notices(*notices: str):
    """
    iterable notices with time intervals in between
    """
    for notice in notices:
        sleep(0.5)
        print(f"\n{notice.upper()}\n")
        sleep(1.2)


def WIP():
    """
    placeholder for work in progress functions/objects
    """
    print("\n--- !!! WORK IN PROGRESS !!! ---\n")


if __name__ == "__main__":
    main()
