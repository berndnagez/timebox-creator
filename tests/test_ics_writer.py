from src.output import ics_writer
from src.timebox import timebox_creator
from src.template import template


def test_write_events_to_file():
    loaded_template = template.read_template('templates/test_template.json')
    cal = timebox_creator.create_events_from_template(
        loaded_template)
    file_path = "tests/test_output.ics"
    test_file_path = "tests/test.ics"

    ics_writer.write_events_to_file(cal, file_path)

    with open(test_file_path, 'r') as file:
        expected_content = file.readlines()

    with open(file_path, 'r') as file:
        created_content = file.readlines()

    assert expected_content == created_content
