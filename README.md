# Food Inventory Management

Created by nordentesla

## Video Demo

**!!! UNDER CONSTRUCTION !!!**

## Description

The program is called **Food Inventory Management**.

It is a program that is used to manage food inventory in the household

### Features

* track expiry dates to prevent food wastage
* check food items to plan meals and ingredients for cooking
* export the current list as PDF for printing

### Usage

#### Main Menu Selection

The program has a main menu showing options with the following hierarchy:

1. **New Inventory** - prompts the user for an inventory name. After creating a new inventory, it will go inside the Open Inventory menu.
1. **Manage Existing Inventory** - open and list the existing inventories (accessed through the inventory folder created by the program)
    1. **Displays the existing inventories for selection**
        * Prompts the user for inventory number indicated in the respective inventories
        * Upon creation of a new inventory or selection of an existing inventory, it will open and display the contents of the selected inventory
        * For more details, see Inventory Menu
    1. **Back to Main Menu**
1. **Exit the Program** - exits the program

### Inventory Menu

Upon selection of an inventory, the list of all items inside the selected inventory will display, sorted by date of expiry. (Closest to furthest date) then several options below the list will appear:

1. **Add an Item** - add items, step-by-step, will always have confirmation:
    1. **Name of Item** - *input* - alphanumeric only
    1. **Date of Expiry** - *input* - follows ISO 8601 format: YYYY-MM-DD
1. **Remove an Item** - prompts the user for option number that is displayed in the current inventory
    1. **Item Number** - *input* - option number selection for the item to be edited or removed
        1. **Removal Quantity**  (Usage: 'all' to remove all quantity, 'c' to cancel item removal) - *input* - removes a specified number of quantity, if all quantity is removed, entry removal is shown and established
    1. **Cancel Item Removal** - goes back to current **Inventory Menu**
1. **Export as PDF** - prints the current list into a PDF file
1. **Select Other Inventory** - goes back to **Manage Existing Inventory** menu for inventory selection
1. **Back to Main Menu** - goes back to **Main Menu Selection**
