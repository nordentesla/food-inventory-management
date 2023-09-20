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


class ProgramUI:
    def splash_screen():
        print(Figlet().renderText("Food Inventory Management"))

    def main_menu():
        main_menu_options = [
            "New Inventory", "Manage Existing Inventory",
            "Export Inventory as PDF"
        ]
        # insert 

    def new_inventory_menu():
        inventory_file = input_solver("Create ")
        # insert csv saving here


def main():
    program_start = ProgramUI()
    program_start.main_menu()

def main_menu():
    """
    Options Menu:
    x. New Inventory
    x. Check my Inventory
    x. Add New Item
    x. Remove Item
    x. Edit Item
    x. Export as PDF
    """

def input_solver(prompt):
    while True:
        user_input = input(prompt)
        if user_input == re.search(r"^\w+")





if __name__ == "__main__":
    main()