from src.timebox import timebox_types
from src.timebox import timebox_creator
from src.cli import input_validation
from src.cli import prompts


def show_option_menu(intro: str, options: list) -> int:
    print(_(intro))
    for option_id, option in enumerate(options, start=1):
        print(f"{option_id}. {_(option)}")
    choice = input_validation.read_valid_number(
        _("Enter your choice (1-%(num)s): ") % {"num": len(options)}, len(options))
    return choice


def show_main_menu():
    choice = show_option_menu(prompts.MAIN_MENU_INTRO,
                              prompts.MAIN_MENU_OPTIONS)
    return choice


def collect_timebox_data():
    title = input_validation.read_nonempty_string(
        _("Enter the title of the timebox: "), max_length=40)
    type = show_option_menu(
        _("\nAvailable timebox types:"), timebox_types.get_types())
    # TODO: Allow HH-input for HH:00
    start_time = input_validation.read_valid_time(
        _("Enter the start time (HH:MM): "))
    end_time = input_validation.read_valid_time(
        _("Enter the end time (HH:MM): "))
    # TODO: Implement logic to handle day delta
    day_delta = 0
    description = input_validation.read_string(
        _("Enter notes for the timebox: "), max_length=200)
    return title, type, start_time, end_time, day_delta, description


def read_save_choice(box):
    save_choice = show_option_menu(
        prompts.SAVE_CHOICE_INTRO, prompts.SAVE_OPTIONS)
    if save_choice == 1:
        timebox_creator.save_timebox_as(ical=True, template=False, box=box)
    elif save_choice == 2:
        timebox_creator.save_timebox_as(ical=False, template=True, box=box)
    elif save_choice == 3:
        timebox_creator.save_timebox_as(ical=True, template=True, box=box)


def show_create_timebox_menu(zone: str):
    while True:
        title, type, start_time, end_time, day_delta, description = collect_timebox_data()
        box = timebox_creator.create_box(
            title, start_time, end_time, day_delta, description, type, zone)
        read_save_choice(box)

        next_action = show_option_menu(
            prompts.NEXT_ACTION_INTRO, prompts.NEXT_ACTIONS_OPTIONS)
        if next_action == 2:
            break
