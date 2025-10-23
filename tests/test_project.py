from django.conf import settings

from src import __version__


def test_version() -> None:
    assert __version__ == "0.1.0"


def test_settings() -> None:
    assert settings.IS_TEST
