from src.timebox import timebox_creator
from src.timebox import timebox_creator


def test_create_event():
    title = "Test Event"
    start = "10:00"
    end = "11:00"
    description = "This is a test event."
    zone = "Europe/Berlin"
    start_datetime = timebox_creator.parse_time_to_datetime_next_day(
        start, zone)
    end_datetime = timebox_creator.parse_time_to_datetime_next_day(
        end, zone)
    event = timebox_creator.create_timebox_event(
        title, start_datetime, end_datetime, description)
    assert event.get('SUMMARY') == title
    assert event.get('DESCRIPTION') == description
    assert event.get('DTSTART').dt.hour == 10
    assert event.get('DTEND').dt.hour == 11
    assert event.get('DTSTART').dt.tzinfo.key == zone


def test_parse_time_to_datetime_next_day():
    time_str = "23:59"
    zone = "Europe/Berlin"
    dt = timebox_creator.parse_time_to_datetime_next_day(
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
    cal = timebox_creator.create_events_from_template(template)
    events = [comp for comp in cal.walk() if comp.name == 'VEVENT']
    assert len(events) == 2
    assert events[0].get('SUMMARY') == "Event 1"
    assert events[1].get('SUMMARY') == "Event 2"


def test_create_box():
    title = "Test Box"
    start_time = "10:00"
    end_time = "11:00"
    day_delta = 0
    description = "This is a test box."
    type = 1
    zone = "Europe/Berlin"
    box = timebox_creator.create_box(
        title, start_time, end_time, day_delta, description, type, zone)
    assert box["title"] == title
    assert box["start"] == start_time
    assert box["end"] == end_time
    assert box["day_delta"] == day_delta
    assert box["description"] == description
    assert box["type"] == type
    assert box["zone"] == zone
