
from src.cli import input


def test_show_option_menu(monkeypatch, capsys):
    intro = _("\nAvailable timebox types:")
    types = ["Pomodoro", "Short Break", "Long Break"]

    inputs = iter(["abc", "10", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = input.show_option_menu(intro, types)

    captured = capsys.readouterr()
    output = captured.out

    assert intro in output

    for i, t in enumerate(types, start=1):
        assert f"({i}) {t}" in output

    assert result == 2
