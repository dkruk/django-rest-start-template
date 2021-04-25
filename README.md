# Django REST start template
Simple Django project template for REST API with my preferred setup. The template is just for a quick start and covers only the base things. If you looking for more complex templates, please look at projects like [django-project-template](https://github.com/jpadilla/django-project-template) or [wemake-django-template](https://github.com/wemake-services/wemake-django-template).

## Stack
* Python 3.9;
* Postgres 13 as database;
* Redis 6 as cache and message broker.

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

### Why is there no setting for background tasks?

Background tasks is needed on almost all projects, but various approaches can be used to implement it. The most common solution is [Celery](https://docs.celeryproject.org/en/stable/index.html), but [Dramatiq](https://dramatiq.io/) and other solutions are also commonly used. At the moment, I cannot choose one thing.

### Why is there no setting for deploy?

The number of options here is much larger than in background tasks, so choosing one thing is also very difficult.