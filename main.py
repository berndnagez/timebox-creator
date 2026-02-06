from src import template
from src import templated_timebox_creator
from src import output
from src import input


def main():
    choice = input.show_main_menu()
    if choice == 1:
        print("Creating a new timebox...")
        input.show_create_timebox_menu()
    elif choice == 2:
        print("Creating a new template...")
        # Implement template creation logic here
    elif choice == 3:
        print("Loading a template...")
        # template = template_reader.read_template('templates/test_template.json')
        # cal = events_from_template_creater.create_events_from_template(template)
        # events_writer.write_events_to_file(cal, 'results/output.ics')
    elif choice == 4:
        print("Exiting the program. Goodbye!")
        exit()


if __name__ == "__main__":
    main()
