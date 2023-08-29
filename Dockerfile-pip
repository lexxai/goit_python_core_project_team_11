# Docker-команда FROM вказує базовий образ контейнера
# Наш базовий образ - це Linux з попередньо встановленим python-3.11
FROM python:3.11-slim

# Встановимо змінну середовища
ENV APP_HOME /app

# Встановимо робочу директорію всередині контейнера
WORKDIR $APP_HOME

# Скопіюємо інші файли в робочу директорію контейнера
COPY . .

# Встановимо залежності всередині контейнера

ENV VIRTUAL_ENV=/app/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install .
RUN mkdir $APP_HOME/user_data
RUN cd $APP_HOME/user_data

WORKDIR $APP_HOME/user_data


# Запустимо наш застосунок всередині контейнера
# ENTRYPOINT [ "python", "assistant_bot/main.py" ]

ENTRYPOINT [ "assistant_bot" ]