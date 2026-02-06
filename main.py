from src import template_reader
from src import events_from_template_creater
from src import events_writer
from src import user_input_reader


def main():
    choice = user_input_reader.show_main_menu()
    if choice == 1:
        print("Creating a new timebox...")
        # Implement timebox creation logic here
    elif choice == 2:
        print("Creating a new template...")
        # Implement template creation logic here
    elif choice == 3:
        print("Loading a template...")
        # Implement template loading logic here
        # template = template_reader.read_template('templates/test_template.json')
        # cal = events_from_template_creater.create_events_from_template(template)
        # events_writer.write_events_to_file(cal, 'results/output.ics')
    elif choice == 4:
        print("Exiting the program. Goodbye!")
        exit()


if __name__ == "__main__":
    main()
