# flake8: noqa
from pathlib import Path

import environ

from src.global_constants import LOCAL_ENV

env = environ.Env()
environ.Env.read_env(f'{Path(__file__).resolve().parent.parent.parent}/.env')

if env('ENVIRONMENT') == LOCAL_ENV:
    from .local import *
else:
    from .base import *
