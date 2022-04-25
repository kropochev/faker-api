# Faker API
Генератор случайных личностей.

## Установка
Клонировать этот репозиторий. `git clone https://github.com/kropochev/faker-api.git`

## Запуск с помощью Docker-Compose
1. Проверить, что `Docker` работает локально.
2. Создать образ `docker-compose build`.
3. Запустить `docker-compose up`.

## Создание личности
```
curl -X 'POST' \
  'http://0.0.0.0:8000/person?sex=Male&age=20' \
  -H 'accept: application/json' \
  -d ''
```

## Создание нескольких личностей
```
curl -X 'POST' \
  'http://0.0.0.0:8000/persons?sex=Female&age=25&count=3' \
  -H 'accept: application/json' \
  -d ''
```
Результат
```
[
  {
    "first_name": "Раиса",
    "last_name": "Сорокина",
    "birthday": "14-03-1997",
    "login": "Raisa25",
    "password": "VggTqs&J"
  },
  {
    "first_name": "Анжелика",
    "last_name": "Шестакова",
    "birthday": "07-11-1996",
    "login": "Anzhelika25",
    "password": "5u-6gttb"
  },
  {
    "first_name": "Надежда",
    "last_name": "Костина",
    "birthday": "17-09-1996",
    "login": "Kostina1996",
    "password": "=P&BH69b"
  }
]
```