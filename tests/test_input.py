
from src.cli import input


def test_read_valid_number():
    pass


def test_read_nonempty_string():
    pass


def test_read_valid_time():
    pass


def test_show_available_types():
    available_types = ["default", "15min-break", "30min-break"]
    excepted_number_of_available_types = 3
    return_number_of_available_types = input.show_available_types(
        available_types)
    assert return_number_of_available_types == excepted_number_of_available_types
