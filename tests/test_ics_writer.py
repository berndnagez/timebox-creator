from icalendar import Calendar
from src.output import ics_writer
from src.timebox import timebox_creator
from src.template import template


def test_write_events_to_file(tmp_path):
    file = tmp_path / "test.ics"
    loaded_template = template.read_template('templates/test_template.json')
    cal = timebox_creator.create_events_from_template(
        loaded_template)

    ics_writer.write_events_to_file(cal, file)

    returned_cal = Calendar.from_ical(file.read_bytes())
    events = returned_cal.walk("VEVENT")
    first = events[0]

    assert len(events) == 6
    assert first["SUMMARY"].to_ical().decode() == "VN JAT"
