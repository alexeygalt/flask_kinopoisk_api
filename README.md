

## Описание проекта

- Установка зависимостей

```shell
pip install -r requirements.txt

pip install -r requirements.dev.txt
```

## Запуск тестов

```shell
pytest .
```

## Запуск проекта

- run script

```shell
python run.py
```

- Open [http://127.0.0.1:25000/]()

## Методы

| Url|Methods|
|----|----|
|`/movies/`|`GET` params: status, page.|
|`/movies/<id>`|`GET`|
|`/genres/`|`GET` param: page|
|`/genres/<id>`|`GET`|
|`/directors/`|`GET` param: page|
|`/directors/<id>`|`GET`|
|`/auth/register`|`POST`|
|`/auth/login`|`POST`, `PUT`|
|`/user/`|`GET`, `PATCH`|
|`/user/password`|`PUT`|
