# Django REST start template
Simple Django project template for REST API with my preferred setup.
The template is just for a quick start and covers only the base things.

## Stack
* Python 3.12;
* Postgres 15 as database;
* Redis 7 as cache and message broker.

## Features
* [Django](https://www.djangoproject.com/) - python web framework;
* [Django REST Framework](https://www.django-rest-framework.org/) - for serializing and deserializing data;
* [drf-spectacular](https://github.com/tfranzel/drf-spectacular) - for REST api documentation;
* [django-cors-headers](https://github.com/adamchainz/django-cors-headers) - adds Cross-Origin Resource Sharing headers to responses;
* [django-environ](https://github.com/joke2k/django-environ) - read `.env` file;


### Dev features
* [pytest](https://github.com/pytest-dev/pytest) - for unit and integration tests;
* [flake8](https://github.com/PyCQA/flake8) - check code style;
* [mypy](https://github.com/python/mypy) - check types;
* [autopep8](https://github.com/hhatto/autopep8) - automatically update code style;
* [isort](https://github.com/PyCQA/isort) - keeps imports in the correct way;
* [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar) - to find weak points in the project.

### Docker

Docker settings is for development only.
