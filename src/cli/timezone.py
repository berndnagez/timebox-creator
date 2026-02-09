import os
import json
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


def timezone_conf_exists(conf_file_path: str) -> bool:
    if os.path.exists(conf_file_path):
        return True
    else:
        return False


def is_validate_timezone(timezone) -> bool:
    try:
        ZoneInfo(timezone)
        return True
    except ZoneInfoNotFoundError:
        return False


def get_timezone_conf(conf_file_path: str) -> str:
    with open(conf_file_path, 'r') as file:
        timezone = json.load(file)
    return timezone['timezone']


def get_timezone_input():
    pass
    # siehe ChatGPT "Eingabevalidierung in Python"
    # evtl. nutzen: from zoneinfo import available_timezones (siehe ChatGPT-Chat "Eingabevalidierung in Python")
    # return timezone


def write_timezone(timezone: str):
    pass


def get_timezone(conf_file_path: str) -> str:
    if timezone_conf_exists:
        timezone = get_timezone_conf(conf_file_path)
        if not is_validate_timezone(timezone):
            print(f'No valid timezone found.')
            timezone = get_timezone_input()
    else:
        timezone = get_timezone_input
        write_timezone(timezone)
    return timezone
