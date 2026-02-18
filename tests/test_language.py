from src.cli import language


def test_set_language():
    pass


def test_get_saved_language(tmp_path):
    file = tmp_path / "test_conf.json"
    file.write_text('{"timezone": "Europe/Berlin", "language": "de"}')
    language.get_saved_language(file) == "de"


def test_get_input_language():
    pass


def test_save_language():
    pass


def test_get_language():
    pass
