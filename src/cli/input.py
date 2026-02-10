from src.timebox import timebox_types
from src.timebox import timebox_creator


def read_valid_number(prompt, max_value):
    while True:
        try:
            user_input = int(input(prompt))
            if 1 <= user_input <= max_value:
                return user_input
            else:
                print(
                    _("Invalid choice. Please enter a number between 1 and %(num)s.") % {"num": max_value})
        except ValueError:
            print(
                _("Invalid input. Please enter a number between 1 and %(num)s.") % {"num": max_value})


def show_main_menu():
    print(_("\nWelcome to the Timebox Creator!\n"))
    print(_("Please select an option:"))
    print(_("(%(num)s) Create a new timebox") % {"num": "1"})
    print(_("(%(num)s) Create a new template") % {"num": "2"})
    print(_("(%(num)s) Load a template") % {"num": "3"})
    print(_("(%(num)s) Exit") % {"num": "4"})
    choice = read_valid_number(
        _("Enter your choice (1-%(num)s): ") % {"num": "4"}, 4)
    return choice


def read_nonempty_string(prompt, max_length=20):
    while True:
        user_input = input(prompt).strip()

        if user_input and len(user_input) <= max_length:
            return user_input

        print(
            _("Empty input or input too long. Please enter a non-empty string with at most %(num)s characters.") % {"num": max_length})


def show_available_types(available_timebox_types):
    for option_id, timebox_type in enumerate(available_timebox_types, start=1):
        print(f"({option_id}) {timebox_type}")
    return len(available_timebox_types)


def read_valid_time(prompt):
    while True:
        user_input = input(prompt).strip()
        try:
            hours, minutes = map(int, user_input.split(":"))
            if 0 <= hours < 24 and 0 <= minutes < 60:
                return f"{hours:02d}:{minutes:02d}"
            else:
                print(_("Invalid time. Please enter a valid time in HH:MM format."))
        except ValueError:
            print(_("Invalid format. Please enter time in HH:MM format."))


def show_create_timebox_menu(timezone: str):
    title = read_nonempty_string(
        _("Enter the title of the timebox: "), max_length=40)
    print(_("\nAvailable timebox types:"))
    number_of_available_types = show_available_types(timebox_types.get_types())
    type = read_valid_number(
        _("Enter your choice (1-%(num)s): ") % {"num": number_of_available_types}, number_of_available_types)
    start_time = read_valid_time(_("Enter the start time (HH:MM): "))
    end_time = read_valid_time(_("Enter the end time (HH:MM): "))
    description = read_nonempty_string(
        _("Enter notes for the timebox: "), max_length=200)
    zone = timezone
    box = timebox_creator.create_box(
        title, start_time, end_time, description, type, zone)
    return box
