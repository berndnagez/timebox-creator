
from datetime import datetime
from src.cli import input


def test_get_timezone():
    excepted_zone = "Europe/Berlin"
    returned_zone = input.get_timezone()
    assert returned_zone == excepted_zone


def test_show_available_types():
    available_types = ["default", "15min-break", "30min-break"]
    excepted_number_of_available_types = 3
    return_number_of_available_types = input.show_available_types(
        available_types)
    assert return_number_of_available_types == excepted_number_of_available_types
