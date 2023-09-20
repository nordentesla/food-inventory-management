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


def main():
    main_menu()

def main_menu():
    """
    Options Menu:
    1. Check my Inventory
    2. Add New Item
    3. Remove Item
    4. Edit Item
    5. Export as PDF
    """
    print(Figlet().renderText("Food Inventory Management"))
    




if __name__ == "__main__":
    main()