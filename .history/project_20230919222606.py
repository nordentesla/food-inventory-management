'''
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
'''


from pyfiglet import Figlet
import csv
from tabulate import tabulate
import sys

class ProgramMenu:
    def __init__(self):
        self.name = str
        self.menu = list[list]
        self.option = int

    def __len__(self, input_list: list):
        return len(input_list)
    
    def options_table(self):
        print(f"|====---- {self.name.upper()} ----====|")
        print(
            tabulate(self.menu, showindex=list(map(lambda x:x+1, list(range(len(self.menu))))))
            )
        
    def opt
        

class MainMenu(ProgramMenu):
    def __init__(self):
        super().__init__()
        self.name = "Main Menu"
        self.menu = [
            ["New Inventory"],
            ["Manage Existing Inventory"],
            ["Exit Program"],
        ]

def main():
    # Initialization
    main_menu = ProgramMenu()
    # Splash Screen
    print(Figlet().renderText('Food Inventory Management'))
    print('\n----- \"A handy inventory management program for your food\" -----\n')
    main_menu.options_table()



if __name__ == "__main__":
    main()
