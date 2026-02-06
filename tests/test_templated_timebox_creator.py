from src import templated_timebox_creator
from src import timebox_creator


def test_parse_time_to_datetime_next_day():
    time_str = "23:59"
    zone = "Europe/Berlin"
    dt = templated_timebox_creator.parse_time_to_datetime_next_day(
        time_str, zone)
    assert dt.hour == 23
    assert dt.minute == 59
    assert dt.tzinfo.key == zone


def test_create_events_from_template():
    template = {
        "box_list": [
            {
                "title": "Event 1",
                "start": "09:00",
                "end": "10:00",
                "description": "First event",
                "zone": "Europe/Berlin"
            },
            {
                "title": "Event 2",
                "start": "11:00",
                "end": "12:00",
                "description": "Second event",
                "zone": "Europe/Berlin"
            }
        ]
    }
    cal = templated_timebox_creator.create_events_from_template(template)
    events = [comp for comp in cal.walk() if comp.name == 'VEVENT']
    assert len(events) == 2
    assert events[0].get('SUMMARY') == "Event 1"
    assert events[1].get('SUMMARY') == "Event 2"
