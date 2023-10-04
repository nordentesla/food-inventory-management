# Food Inventory Management

Created by nordentesla

## Video Demo

**!!! UNDER CONSTRUCTION !!!**

## Description

The program is called **Food Inventory Management**.

It is a program that is used to manage food inventory in the household.

### Features

* track expiry dates to prevent food wastage
* check food items to plan meals and ingredients for cooking
* export the current list as PDF for printing

### Usage

#### Main Menu Selection

The program has a main menu showing options with the following hierarchy:

1. **New Inventory** - prompts the user for an inventory name. After creating a new inventory, it will go inside the Open Inventory menu.
1. **Manage Existing Inventory** - open and list the existing inventories (accessed through the inventory folder created by the program).
    1. **Displays the existing inventories for selection**
        * Prompts the user for inventory number indicated in the respective inventories.
        * Upon creation of a new inventory or selection of an existing inventory, it will open and display the contents of the selected inventory.
        * For more details, see **Inventory Menu**.
    1. **Back to Main Menu**
1. **About this Program** - a short background about this program.
1. **Exit the Program** - exits the program.

### Inventory Menu

Upon selection of an inventory, the list of all items inside the selected inventory will display, sorted by date of expiry. (Closest to furthest date) then several options below the list will appear:

1. **Add an Item** - (a) add items, step-by-step, will always have confirmation:
    1. **Name of Item** - *input* - alphanumeric only
    1. **Date of Expiry** - *input* - follows ISO 8601 format: YYYY-MM-DD
    1. **Quantity** - *input* - asks the user how many items will be added
1. **Remove an Item** - (r) prompts the user for option number that is displayed in the current inventory
    1. **Item Number** - *input* - option number selection for the item to be edited or removed
        1. **Removal Quantity**  (Usage: 'all' to remove all quantity, 'c' to cancel item removal) - *input* - removes a specified number of quantity, if all quantity is removed, entry removal is shown and established
1. **Export as PDF** - (e) - prints the current list into a PDF file
1. **Delete this Inventory** - (d) - deletes the current selected inventory
1. **Select Other Inventory** - (i) - goes back to **Manage Existing Inventory** menu for inventory selection
1. **Back to Main Menu** - (0) - goes back to **Main Menu Selection**

### Appendix

#### Directories Used in this Program

1. inventories - this folder contains the created inventories in this program, files stored here is automatically saved with the proper dataframe headers for future items in the inventories.
1. saved-pdfs - this folder contains the exported PDFs by the program, the program uses "FPDF" library to create an inventory list in PDF format.

#### Python Package Index Libraries Used

1. pyfiglet - for main menu splash screen, purely for aesthetics.
1. csv - for parsing data from a .csv file, which is the format used for inventory lists in the program
1. tabulate - for printing program menu user interface and inventory list interface in the command line
1. sys - for program related methods such as exiting, CLI argparse is considered for future program feature
1. datetime - used to compare expiry dates of items in the inventory list
1. os - used to read directories such as the folders used by the inventory lists
1. re - regex used to validate user inputs such as numbers, dates, etc..
1. time - used to have a pause between program menu transitions for ease of use
1. fpdf2 - for exporting of inventory lists as PDFs
1. pandas - used for advanced manipulation of inventory lists by initializing them into dataframes, useful in adding and removing items and identifying duplicates in the inventory lists.
