# Docker-команда FROM вказує базовий образ контейнера
# Наш базовий образ - це Linux з попередньо встановленим python-3.11
FROM python:3.11-slim

# Встановимо змінну середовища
# ENV APP_HOME /app

ENV APP_HOME /app 
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Встановимо робочу директорію всередині контейнера
WORKDIR $APP_HOME

# Скопіюємо інші файли в робочу директорію контейнера
COPY . .

# Встановимо залежності всередині контейнера



RUN pip install --upgrade pip 

ENV VIRTUAL_ENV=/app/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install poetry 
# Project initialization:
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi
RUN poetry build

# RUN poetry install
# RUN poetry build
RUN mkdir $APP_HOME/user_data
RUN cd $APP_HOME/user_data

WORKDIR $APP_HOME/user_data


# Запустимо наш застосунок всередині контейнера
# ENTRYPOINT [ "python", "assistant_bot/main.py" ]

ENTRYPOINT [ "assistant_bot" ]