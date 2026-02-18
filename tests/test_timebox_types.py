from src.timebox import timebox_types


def test_get_types():
    expected_types = ["default", "5min-break", "15min-break",
                      "30min-break", "60min-break", "deep-work", "10min-rule", "pomodoro-classic"]
    returned_types = timebox_types.get_types()
    assert returned_types == expected_types
