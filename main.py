from src.template import template
from src.timebox import timebox_creator
from src.output import ics_writer
from src.cli import input, timezone

timezone_conf_path = "./conf/timezone.json"


def main():
    try:
        zone = timezone.get_timezone(timezone_conf_path)
        choice = input.show_main_menu()
        if choice == 1:
            print("Creating a new timebox...")
            box = input.show_create_timebox_menu(zone)
            # Next fragen: Speichern oder als ics exportieren
        elif choice == 2:
            print("Creating a new template...")
            # Implement template creation logic here
        elif choice == 3:
            print("Loading a template...")
            loaded_template = template.read_template(
                'templates/test_template.json')
            cal = timebox_creator.create_events_from_template(loaded_template)
            ics_writer.save_ical(cal, 'results/output.ics')
        elif choice == 4:
            print("Exiting the program. Goodbye!")
            exit()
    except KeyboardInterrupt:
        print("\nKeyboard Interruption: Exiting the program. Goodbye!")
        exit()


if __name__ == "__main__":
    main()
