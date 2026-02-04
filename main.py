from src import template_reader
from src import events_creater
from src import events_writer


def main():
    template = template_reader.read_template('templates/test_template.json')
    cal = events_creater.create_events_from_template(template)
    events_writer.write_events_to_file(cal, 'results/output.ics')


if __name__ == "__main__":
    main()
