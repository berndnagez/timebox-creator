from src import output
from src import templated_timebox_creator
from src import template


def test_write_events_to_file():
    loaded_template = template.read_template('templates/test_template.json')
    cal = templated_timebox_creator.create_events_from_template(
        loaded_template)
    file_path = "tests/test_output.ics"
    test_file_path = "tests/test.ics"

    output.write_events_to_file(cal, file_path)

    with open(test_file_path, 'r') as file:
        expected_content = file.readlines()

    with open(file_path, 'r') as file:
        created_content = file.readlines()

    assert expected_content == created_content
