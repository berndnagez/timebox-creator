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


def test_get_saved_timezone(tmp_path):
    file = tmp_path / "test_timezone.json"
    file.write_text('{"timezone": "Europe/Berlin"}')
    assert timezone.get_saved_timezone(file) == "Europe/Berlin"


def test_get_all_timezones():
    pass


def test_get_regions():
    pass


def test_get_timezones_for_region():
    pass


def test_get_timezone_input():
    pass


def test_choose_from_list():
    pass


def test_get_timezone_input():
    pass


def test_save_timezone(tmp_path):
    file = tmp_path / "timezone.json"
    zone = "Europe/Berlin"
    timezone.save_timezone(zone, file)

    returned_timezone = timezone.get_saved_timezone(file)
    assert returned_timezone == zone


def test_get_timezone():
    pass
