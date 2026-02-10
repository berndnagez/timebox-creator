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
                    f"Invalid choice. Please enter a number between 1 and {max_value}.")
        except ValueError:
            print(
                f"Invalid input. Please enter a number between 1 and {max_value}.")


def show_main_menu():
    print(f"\nWelcome to the Timebox Creator!\n")
    print(f"Please select an option:")
    print(f"(1) Create a new timebox")
    print(f"(2) Create a new template")
    print(f"(3) Load a template")
    print(f"(4) Exit")
    choice = read_valid_number("Enter your choice (1-4): ", 4)
    return choice


def read_nonempty_string(prompt, max_length=20):
    while True:
        user_input = input(prompt).strip()

        if user_input and len(user_input) <= max_length:
            return user_input

        print(
            f"Empty input or input too long. Please enter a non-empty string with at most {max_length} characters.")


def show_available_types(available_timebox_types):
    print(f"\nAvailable timebox types:")
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
                print(f"Invalid time. Please enter a valid time in HH:MM format.")
        except ValueError:
            print(f"Invalid format. Please enter time in HH:MM format.")


def show_create_timebox_menu(timezone: str):
    title = read_nonempty_string(
        f"Enter the title of the timebox: ", max_length=40)
    number_of_available_types = show_available_types(timebox_types.get_types())
    type = read_valid_number(
        f"Enter your choice (1-{number_of_available_types}): ", number_of_available_types)
    start_time = read_valid_time(f"Enter the start time (HH:MM): ")
    end_time = read_valid_time(f"Enter the end time (HH:MM): ")
    description = read_nonempty_string(
        f"Enter notes for the timebox: ", max_length=200)
    zone = timezone
    box = timebox_creator.create_box(
        title, start_time, end_time, description, type, zone)
    return box
