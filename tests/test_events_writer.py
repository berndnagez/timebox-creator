from src import events_writer
from src import events_creater
from src import template_reader


def test_write_events_to_file():
    template = template_reader.read_template('templates/test_template.json')
    cal = events_creater.create_events_from_template(template)
    file_path = "tests/test_output.ics"
    test_file_path = "tests/test.ics"

    events_writer.write_events_to_file(cal, file_path)

    with open(test_file_path, 'r') as file:
        expected_content = file.readlines()

    with open(file_path, 'r') as file:
        created_content = file.readlines()

    assert expected_content == created_content
