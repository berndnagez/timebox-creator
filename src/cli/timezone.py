import os
import json
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError, available_timezones

EXCLUDED_REGIONS = {
    "Etc",
    "Factory",
    "Antarctica",   # optional
    "Arctic",       # optional
}


def conf_exists(conf_file_path: str) -> bool:
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


def get_saved_timezone(conf_file_path: str) -> str:
    with open(conf_file_path, 'r') as file:
        timezone = json.load(file)
    return timezone['timezone']


def get_all_timezones():
    return sorted(available_timezones())


def get_regions():
    regions = set()

    for tz in available_timezones():
        if "/" not in tz:
            continue   # removes CET, EST, CST6CDT etc. automatically

        region = tz.split("/", 1)[0]

        if region not in EXCLUDED_REGIONS:
            regions.add(region)

    return sorted(regions)


def get_timezones_for_region(region: str):
    prefix = f"{region}/"

    return [
        tz for tz in get_all_timezones()
        if tz.startswith(prefix)
    ]


def choose_from_list(items):
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item}")

    while True:
        choice = input("Number: ")

        if choice.isdigit() and 1 <= int(choice) <= len(items):
            return items[int(choice) - 1]
        else:
            print(f"Not a valid number. Please try again.")


def get_timezone_input():
    print("Welcome to timebox creator.")
    print("Either you are using the program for the first time or your timezone selection has been lost.")
    print("Please select your timezone.")
    region = choose_from_list(get_regions())
    timezone = choose_from_list(get_timezones_for_region(region))
    return timezone


def save_timezone(timezone: str, conf_file_path: str):
    timezone_dict = {"timezone": timezone}
    json_str = json.dumps(timezone_dict)
    with open(f'{conf_file_path}', "w") as f:
        f.write(json_str)


def get_timezone(conf_file_path: str) -> str:
    if conf_exists(conf_file_path):
        timezone = get_saved_timezone(conf_file_path)
        if not is_validate_timezone(timezone):
            print(f'No valid timezone found.')
            timezone = get_timezone_input()
    else:
        timezone = get_timezone_input()
        save_timezone(timezone, conf_file_path)
    return timezone
