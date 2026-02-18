import icalendar
import zoneinfo
from datetime import datetime, timedelta


def create_timebox_event(title, start_datetime, end_datetime, description):
    event = icalendar.Event()
    event.add('SUMMARY', title)
    event.add('DTSTART', start_datetime)
    event.add('DTEND', end_datetime)
    event.add('DESCRIPTION', description)
    return event


def parse_time_to_datetime_next_day(time_str, zone):
    time_obj = datetime.strptime(time_str, "%H:%M").time()
    now = datetime.now(zoneinfo.ZoneInfo(zone))
    combined_datetime = datetime.combine(
        now.date(), time_obj).replace(tzinfo=zoneinfo.ZoneInfo(zone))
    if combined_datetime <= now:
        combined_datetime += timedelta(days=1)
    return combined_datetime


def create_events_from_template(template):
    cal = icalendar.Calendar()
    for box in template.get('box_list', []):
        start_datetime = parse_time_to_datetime_next_day(
            box['start'], box['zone'])
        end_datetime = parse_time_to_datetime_next_day(box['end'], box['zone'])
        event = create_timebox_event(title=box['title'], start_datetime=start_datetime,
                                     end_datetime=end_datetime, description=box['description'])
        cal.add_component(event)
    return cal


def create_box(title, start_time, end_time, day_delta, description, type, zone):
    box = {
        "title": title,
        "start": start_time,
        "end": end_time,
        "day_delta": day_delta,
        "description": description,
        "type": type,
        "zone": zone
    }
    return box


def save_as_ical(box):
    pass


def save_as_template(box):
    pass


def save_as_ical_and_template(box):
    pass


def save_timebox_as(ical: bool, template: bool, box: dict):
    if ical and not template:
        save_as_ical(box)
    elif not ical and template:
        save_as_template(box)
    elif ical and template:
        save_as_ical_and_template(box)
