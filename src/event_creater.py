import icalendar


def create_event(title, start_datetime, end_datetime, description):
    event = icalendar.Event()
    event.add('SUMMARY', title)
    event.add('DTSTART', start_datetime)
    event.add('DTEND', end_datetime)
    event.add('DESCRIPTION', description)
    return event
