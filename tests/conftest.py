import builtins
import pytest


@pytest.fixture(autouse=True)
def mock_gettext():
    builtins._ = lambda x: x
