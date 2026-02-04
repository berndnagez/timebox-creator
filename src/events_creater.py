import icalendar
import zoneinfo
from datetime import datetime, timedelta


def parse_time_to_datetime_next_day(time_str, zone):
    time_obj = datetime.strptime(time_str, "%H:%M").time()
    now = datetime.now(zoneinfo.ZoneInfo(zone))
    combined_datetime = datetime.combine(
        now.date(), time_obj).replace(tzinfo=zoneinfo.ZoneInfo(zone))
    if combined_datetime <= now:
        combined_datetime += timedelta(days=1)
    return combined_datetime


def create_event(title, start, end, description, zone):
    start_datetime = parse_time_to_datetime_next_day(start, zone)
    end_datetime = parse_time_to_datetime_next_day(end, zone)
    event = icalendar.Event()
    event.add('SUMMARY', title)
    event.add('DTSTART', start_datetime)
    event.add('DTEND', end_datetime)
    event.add('DESCRIPTION', description)
    return event


def create_events_from_template(template):
    cal = icalendar.Calendar()
    for box in template.get('box_list', []):
        event = create_event(title=box['title'], start=box['start'],
                             end=box['end'], description=box['description'], zone=box['zone'])
        cal.add_component(event)
    return cal
