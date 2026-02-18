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


def read_nonempty_string(prompt, max_length=20):
    while True:
        user_input = input(prompt).strip()

        if user_input and len(user_input) <= max_length:
            return user_input

        print(
            _("Empty input or input too long. Please enter a non-empty string with at most %(num)s characters.") % {"num": max_length})


def read_string(prompt, max_length=20):
    while True:
        user_input = input(prompt).strip()

        if len(user_input) <= max_length:
            return user_input

        print(
            _("Input too long. Please enter a string with at most %(num)s characters.") % {"num": max_length})


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
