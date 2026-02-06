from src import event_creater
from src import events_from_template_creater


def test_create_event():
    title = "Test Event"
    start = "10:00"
    end = "11:00"
    description = "This is a test event."
    zone = "Europe/Berlin"
    start_datetime = events_from_template_creater.parse_time_to_datetime_next_day(
        start, zone)
    end_datetime = events_from_template_creater.parse_time_to_datetime_next_day(
        end, zone)
    event = event_creater.create_event(
        title, start_datetime, end_datetime, description)
    assert event.get('SUMMARY') == title
    assert event.get('DESCRIPTION') == description
    assert event.get('DTSTART').dt.hour == 10
    assert event.get('DTEND').dt.hour == 11
    assert event.get('DTSTART').dt.tzinfo.key == zone
