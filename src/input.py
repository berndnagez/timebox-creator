from src import timebox_types
from src import timebox_creator


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
    print("\nWelcome to the Timebox Creator!")
    print("Please select an option:")
    print("(1) Create a new timebox")
    print("(2) Create a new template")
    print("(3) Load a template")
    print("(4) Exit")
    choice = read_valid_number("Enter your choice (1-4): ", 4)
    return choice


def read_nonempty_string(prompt, max_length=20):
    while True:
        user_input = input(prompt).strip()

        if user_input and len(user_input) <= max_length:
            return user_input

        print(
            f"Empty input or input too long. Please enter a non-empty string with at most {max_length} characters.")


def show_available_types():
    available_timebox_types = timebox_types.get_types()
    print("\nAvailable timebox types:")
    for option_id, timebox_type in enumerate(available_timebox_types, start=1):
        print(f"({option_id}) {timebox_type}")


def read_valid_time(prompt):
    while True:
        user_input = input(prompt).strip()
        try:
            hours, minutes = map(int, user_input.split(":"))
            if 0 <= hours < 24 and 0 <= minutes < 60:
                return f"{hours:02d}:{minutes:02d}"
            else:
                print("Invalid time. Please enter a valid time in HH:MM format.")
        except ValueError:
            print("Invalid format. Please enter time in HH:MM format.")


def get_timezone():
    # NEXT Dynamische Zeitzone basierend auf dem Standort des Benutzers ermitteln
    # evtl. nutzen: from zoneinfo import available_timezones
    return "Europe/Berlin"


def show_create_timebox_menu():
    # NEXT Evaluierung der Eingaben
    title = read_nonempty_string(
        "Enter the title of the timebox: ", max_length=40)
    show_available_types()
    type = read_valid_number("Enter your choice (1-5): ", 5)
    start_time = read_valid_time("Enter the start time (HH:MM): ")
    end_time = read_valid_time("Enter the end time (HH:MM): ")
    description = read_nonempty_string(
        "Enter notes for the timebox: ", max_length=200)
    zone = get_timezone()
    box = timebox_creator.create_box(
        title, start_time, end_time, description, type, zone)
    return box
