
from datetime import datetime
from src import input


def test_get_timezone():
    excepted_zone = "Europe/Berlin"
    returned_zone = input.get_timezone()
    assert returned_zone == excepted_zone
