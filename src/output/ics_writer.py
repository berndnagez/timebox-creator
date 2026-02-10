
def save_ical(cal, file_path):
    with open(file_path, 'wb') as file:
        file.write(cal.to_ical())
