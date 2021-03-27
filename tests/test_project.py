from django.conf import settings

from src import __version__


def test_version():
    assert __version__ == '0.1.0'


def test_settings():
    assert settings.IS_TEST
