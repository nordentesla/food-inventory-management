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
        print(f"!--- {self.inv_name} has {len(self.storage)-1} item(s) ---!".upper())

    def special_option(self):
        print("")
        print(f"{self.inv_name.upper()} OPTIONS:\n")
        print(
            f"Type 'a' => Add an Item to {self.inv_name.upper()}",
            f"Type 'r' => Remove an Item from {self.inv_name.upper()}",
            f"Type 'e' => Export \"{self.inv_name.upper()}\" inventory list as PDF",
            f"Type 'd' => Delete \"{self.inv_name.upper()}\" Inventory",
            "Type 'i' => Back to My Inventories",
            "Type '0' => Back to Main Menu",
            sep="\n",
            end="\n\n\n",
        )
        while True:
            try:
                user_input = input(f"===> {self.inv_name.upper()} - Type the Option: ")
                print("")
                match user_input:
                    case "a":
                        # item name input processing
                        while True:
                            item_name = input(
                                "What is the name of the item? "
                                ).strip()
                            if re.search(r"^[A-Za-z]\w{2}\w*$", item_name):
                                confirm_item_name = input(
                                    f"Confirm Item Name: \"{item_name}\"?\n\n[Y/N]:"
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
                                print("Item name must be 3 characters or more and starts with 2 letters".upper())
                        # item expiry date input processing
                        while True:
                            try:
                                item_expiry_date = input(
                                    "What is the expiry date of the item?\n\nInput Date YYYY-MM-DD or YYYY-MM: "
                                    ).strip()
                                if matches := re.search(
                                    r"^(2[0-1](2[3-9]|[3-9]\d)\d)-(0\d|1[0-2])(-([0-2]\d|3[0-1]))*$", 
                                    item_name,
                                    ):
                                    expiry_year = int(matches.group(1))
                                    expiry_month = int(matches.group(3))
                                    if matches.group(5) == None:
                                        expiry_day = 1
                                    else:
                                        expiry_day = int(matches.group(5))

                                    if (item_expiry_date := datetime.date(expiry_year, expiry_month, expiry_day)) > datetime.datetime.now:
                                        item_expiry_date = str(item_expiry_date)
                                    else:
                                        raise ValueError("Invalid expiry date: date should be later than today")
                                    confirm_expiry_date = input(
                                        f"Confirm Expiry Date: \"{item_expiry_date}\"?\n\n[Y/N]:"
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
                                    print("Invalid expiry date, Check your format",
                                        "Valid expiry dates are 2023-10-01 and beyond",
                                        )
                            except ValueError:
                                continue
                        # item name quantity processing
                        while True:
                            item_count = input(
                                f"How many \"{item_name}\" item do you want to add to {self.inv_name}? "
                                ).strip()
                            if re.search(r"^\d{0,2}[1-9]$", item_count):
                                item_count = int(item_count)
                                confirm_item_count = input(
                                    f"Confirm Item to be Added \"{item_expiry_date}\"?\n\n[Y/N]:"
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
                        
                        item_for_appending = [item_name, item_expiry_date, item_count]

                        with open(f"./inventories/{self.inv_name}.csv", "a") as my_csv:
                            csv_writer = csv.DictWriter(
                                my_csv, fieldnames=["Item","Expiry Date","Quantity"]
                                )
                            # existing item
                            if f"{item_name},{item_expiry_date}" in my_csv:
                                # find a way to move the cursor to the existing item
                                # find a way to add the input count to the existing count
                                # max item (999) should return an error if it exceeded the max item count after addition
                                WIP()
                            else:
                                csv_writer.writerow({"Item": item_name, 
                                                    "Expiry Date": item_expiry_date,
                                                    "Quantity": item_count
                                                    })
                        # join inputs into an item list
                        # append inputed list into the file
                        # print a notice that the file is saved
                        # print the item list of the inventory
                        WIP()
                    case "r":
                        # open the csv file
                        # parse the csv file
                        # select item number from the inventory
                        # ask user for input for quantity to be removed
                        # verify if the input is a valid integer, and less than the item quantity
                        # prompt the user if they wish to proceed with the inputted quantity to be removed
                        # subtract the quantity from the item
                        # if the item yields to 0, remove the item from the .csv file
                        WIP()
                    case "e":
                        while True:
                            confirm_create_pdf: str = (
                                input(
                                    f"Do you want to export {self.inv_name.upper()} as PDF? [Y/N]: "
                                )
                                .lower()
                                .strip()
                            )
                            if confirm_create_pdf == "y":
                                pdf_maker(self.inv_name, self.storage)
                                loading_notices(
                                    f"{self.inv_name} inventory exported as pdf",
                                    'pdf file saved at "saved-pdf" folder',
                                    "returning to inventory menu...",
                                )
                                return "Inventory Menu"
                            elif confirm_create_pdf == "n":
                                loading_notices(
                                    "export as pdf cancelled",
                                    "returning to inventory menu...",
                                )
                                return "Inventory Menu"
                            else:
                                print(
                                    '\nInvalid option "y" for Yes and "n" for No only\n'.upper()
                                )
                                continue
                    case "d":
                        while True:
                            confirm_delete: str = (
                                input(
                                    f"Are you sure you want to delete {self.inv_name.upper()}? [Y/N]: "
                                )
                                .lower()
                                .strip()
                            )
                            if confirm_delete == "y":
                                delete_csv_file(self.inv_name)
                                loading_notices(
                                    f"{self.inv_name} deleted!",
                                    "returning to my inventories menu",
                                )
                                return "Manage Existing Inventory"
                            elif confirm_delete == "n":
                                loading_notices(
                                    f"deletion cancelled",
                                    f"returning to {self.inv_name} options menu",
                                )
                                return "Inventory Menu"
                            else:
                                print(
                                    '\nInvalid option "y" for Yes and "n" for No only\n'.upper()
                                )
                                continue
                    case "i":
                        return "Manage Existing Inventory"
                    case "0":
                        return "Main Menu"
                    case _:
                        print("!!! Invalid option, type a valid option !!!\n")
                        continue
            except KeyboardInterrupt:
                return "Exit Program"

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
        [["New Inventory"], ["Manage Existing Inventory"], ["About this Program"], ["Exit Program"]],
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
                    # Read local directory for .csv files, and
                    csv_files = list_saved_inventory_csvs(
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

                case "About this Program":
                    WIP()

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
    print(Figlet().renderText("Food Inventory Management"))
    print('----- "A handy inventory management program for your food" -----\n')
    print("** by ~nordentesla~ **\n")


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
    # first filter: all .csv file in the directory
    file_list = list(
        filter(lambda file: file.endswith(".csv"), list(os.listdir(path=my_path)))
    )
    # second filter: all .csv file should have a valid header:
    file_list = list(
        filter(lambda file: re.search(
            r"^Item,\"?Expiry Date\"?,Quantity\n?$",
            list(open(f"./inventories/{file}", "r"))[0],
            ), file_list)
    )
    # file list modifier
    if map_function != None:
        modified_file_list = []
        for item in file_list:
            modified_file_list.append([map_function(item)])
        return sorted(modified_file_list)
    return sorted(file_list)


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
        my_pdf.cell(txt="! no items in this inventory !".upper(),
                    center=True,)
        my_pdf.ln(30)
    else:
        # for inventory with valid items
        with my_pdf.table() as pdf_table:
            for data_row in inventory_list:
                row = pdf_table.row()
                for datum in data_row:
                    row.cell(datum)
    # program signature
    my_pdf.ln(4)
    my_pdf.set_font(family="helvetica", size=10)
    my_pdf.cell(
        txt="Created with Food Inventory Management by nordentesla / Northwind Creative", 
        center=True,
    )
    # saving PDF file
    my_pdf.output(name=f"./saved-pdf/{pdf_filename}.pdf")


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
        print(f"\n\n{notice.upper()}\n")
        sleep(1.2)


def WIP():
    """
    placeholder for work in progress functions/objects
    """
    sys.exit("\n--- !!! WORK IN PROGRESS !!! ---\n")


if __name__ == "__main__":
    main()
