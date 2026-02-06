from src import timebox_types


def show_main_menu():
    print("\nWelcome to the Timebox Creator!")
    print("Please select an option:")
    print("(1) Create a new timebox")
    print("(2) Create a new template")
    print("(3) Load a template")
    print("(4) Exit")
    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if 1 <= choice <= 4:
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
    return choice


def show_available_types():
    available_timebox_types = timebox_types.get_types()
    print("\nAvailable timebox types:")
    for option_id, timebox_type in enumerate(available_timebox_types, start=1):
        print(f"({option_id}) {timebox_type}")


def show_create_timebox_menu():
    # NEXT Evaluierung der Eingaben
    title = input("Enter the title of the timebox: ")
    show_available_types()
    type = input("Enter your choice (1-5): ")
    start_time = input("Enter the start time (HH:MM): ")
    end_time = input("Enter the end time (HH:MM): ")
    description = input("Enter notes for the timebox: ")
    return title, start_time, end_time, description, type
