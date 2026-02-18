from src.cli import input_validation


def test_read_valid_number(monkeypatch, capsys):

    inputs = iter(["abc", "10", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = input_validation.read_valid_number(">", 5)

    assert result == 2

    captured = capsys.readouterr()
    assert "Invalid" in captured.out


def test_read_nonempty_string(monkeypatch, capsys):

    inputs = iter(
        ["", "This is a very long string that exceeds the limit", "Valid String"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = input_validation.read_nonempty_string(">", max_length=20)

    assert result == "Valid String"

    captured = capsys.readouterr()
    assert "Empty" in captured.out
    assert "too long" in captured.out


def test_read_string_accepts_empty(monkeypatch):
    inputs = iter([""])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = input_validation.read_string(">", max_length=20)

    assert result == ""


def test_read_string_retries_until_valid(monkeypatch, capsys):
    inputs = iter([
        "This is a very long string that exceeds the limit",
        "Valid String",
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = input_validation.read_string(">", max_length=20)

    assert result == "Valid String"

    captured = capsys.readouterr()
    assert "too long" in captured.out


def test_read_valid_time(monkeypatch, capsys):

    inputs = iter(["25:00", "12:60", "abc", "14:30"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = input_validation.read_valid_time(">")

    assert result == "14:30"

    captured = capsys.readouterr()
    assert "Invalid" in captured.out
