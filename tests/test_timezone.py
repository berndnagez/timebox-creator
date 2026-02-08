from src.cli import timezone


def test_timezone_conf_exists():
    excepted_boolean = True
    returned_boolean = timezone.timezone_conf_exists("./conf/timezone.json")
    assert returned_boolean == excepted_boolean

    excepted_boolean = False
    returned_boolean = timezone.timezone_conf_exists("./conf/mist.json")
    assert returned_boolean == excepted_boolean


def test_is_validate_timezone():
    excepted_boolean = True
    returned_boolean = timezone.is_validate_timezone("Europe/Berlin")
    assert returned_boolean == excepted_boolean

    excepted_boolean = False
    returned_boolean = timezone.is_validate_timezone("Bla/Blubb")
    assert returned_boolean == excepted_boolean


def test_get_timezone_conf():
    excepted_timezone = "Europe/Berlin"
    returned_timezone = timezone.get_timezone_conf("./conf/timezone.json")
    assert returned_timezone == excepted_timezone


def test_get_timezone_input():
    pass


def test_write_timezone():
    pass


def test_get_timezone():
    pass
