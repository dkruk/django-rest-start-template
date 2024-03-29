FROM python:3.11
ENV PYTHONUNBUFFERED 1 \
    PYTHONFAULTHANDLER=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

RUN pip install "poetry==1.6.1"

RUN mkdir /project
WORKDIR /project
COPY poetry.* pyproject.* /project/
RUN poetry config virtualenvs.create false && poetry install
ADD . /project
