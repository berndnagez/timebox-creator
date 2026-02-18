import sys
from src.template import template
from src.timebox import timebox_creator
from src.output import ics_writer
from src.cli import input, timezone, language

conf_path = "./conf/conf.json"


def main():
    language.set_language(conf_path)
    zone = timezone.get_timezone(conf_path)
    print(_("\nWelcome to the Timebox Creator!"))
    while True:
        choice = input.show_main_menu()
        if choice == 1:
            print(_("\nCreating a new timebox..."))
            input.show_create_timebox_menu(zone)
        elif choice == 2:
            print(_("Creating a new template..."))
            # Implement template creation logic here
        elif choice == 3:
            print(_("Loading a template..."))
            loaded_template = template.read_template(
                'templates/default.json')
            cal = timebox_creator.create_events_from_template(loaded_template)
            ics_writer.save_ical(cal, 'results/output.ics')
        elif choice == 4:
            print(_("\nExiting the program. Goodbye!"))
            sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(_("\n\nKeyboard Interruption: Exiting the program. Goodbye!"))
        sys.exit(0)
