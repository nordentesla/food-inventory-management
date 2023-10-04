import pytest
from project import list_saved_inventory_csvs
from project import remove_extension_from_file
from project import create_csv_file


# Testing of valid CSV's with proper headers for
# the food inventory management program
def test_list_saved_inventory_csvs():
    assert list_saved_inventory_csvs("./inventories") == sorted(
        ["freezer.csv", "pantry.csv", "refrigerator.csv"]
        )
    assert list_saved_inventory_csvs(".") == []


def test_remove_extension_from_file():
    assert remove_extension_from_file("my_csv.csv") == "my_csv"
    assert remove_extension_from_file("hello_world.txt") == "hello_world"
    assert remove_extension_from_file("pic.jpg") == "pic"


def test_create_csv_file():
    with pytest.raises(FileExistsError):
        create_csv_file("pantry")
        create_csv_file("refrigerator")
        create_csv_file("freezer")
