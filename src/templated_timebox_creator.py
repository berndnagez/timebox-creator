import icalendar
import zoneinfo
from datetime import datetime, timedelta
from src import timebox_creator


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
        event = timebox_creator.create_event(title=box['title'], start_datetime=start_datetime,
                                             end_datetime=end_datetime, description=box['description'])
        cal.add_component(event)
    return cal
