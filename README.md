# Тестовое задание на позицию Back-end developer

## Содержание
- [Тестовое задание на позицию Back-end developer](#тестовое-задание-на-позицию-back-end-developer)
  - [Содержание](#содержание)
  - [Тестовое задание](#тестовое-задание)
  - [Технологии](#технологии)
  - [Установка и использование](#установка-и-использование)
    - [Предупреждение](#предупреждение)
    - [Запуск проекта](#запуск-проекта)
    - [Регистрация](#регистрация)
    - [Авторизация](#авторизация)
  - [Возможности проекта](#возможности-проекта)
  - [Команда проекта](#команда-проекта)

## Тестовое задание
Необходимо реализовать Django приложение для учета оборудование на складах.
* Должны быть реализованный минимум 3 сущности:
  + Stock (Для записи информации о складах для хранения)
  + Category (Для хранения информации о категориях оборудования)
  + Equipment (Для хранения информации о единицах оборудования)
* Требования:
  + Для каждой из модели должны быть реализованы CRUD операции подготовлены API эндпоинты для них. Список операций:
    1. Создание записей.
    2. Получение конкретной записи.
    3. Получение списка всех записей.
    4. Удаление записи.
    5. Изменение записи.
  * Должны быть реализованы сериализаторы для каждой модели.
  * Данные должны храниться в любой базе данных по Вашему усмотрению
  * API должно быть реализовано с помощью Django REST Framework
  * Взаимосвязь между моделями должна быть выстроена следующим образом:
    1. Модель Equipment должна иметь связь по ключу с моделями Category и Stock (При реализации модели User, с ней также должна быть настроена связь)
* Будет существенным плюсом:
  + Добавить сущность User (Для хранения информации о пользователях (можно использовать дефолтную))
  + Настроить permission для пользователей:
    1. Администратор имеет доступ ко всем CRUD операциям
    2. Авторизованный пользователь имеет доступ только к чтению данных
  + Реализовать логику авторизации и аутентификации с использованием любой из библиотек
  + Подключить базу данных PostgreSQL
  + Докеризировать проект, чтобы он запускался через docker compose up
  + Настроить поиск и фильтры в панеле администратора django
  + Написать документацию с использованием библиотеки drf-yasg
  + Соблюдение PEP8


## Технологии
- [django](https://www.djangoproject.com/)
- [DRF]( https://www.django-rest-framework.org/)
- [Docker](https://docs.docker.com)
- [docker-compose](https://docs.docker.com/compose/)
- [PostgreSQL](https://www.postgresql.org/)
- [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/)
- [djoser](https://djoser.readthedocs.io/en/latest/)

## Установка и использование

### Предупреждение
> [!WARNING]
> Использовать API могут только авторизованные пользователи.

### Запуск проекта

В дирекртории с Dockerfile и docker-compose.yml:
```bash
$ docker-compose up --build -d 
```
После запуска Вам следует зарегистрироваться и авторизоваться. 

### Регистрация
[127.0.0.1:8000/api/auth/users/](http://127.0.0.1:8000/api/auth/users/) по POST-запросу
```json
{
    "username": "your username",
    "password": "your password",
    "email": "your email" 
}
```

### Авторизация
[127.0.0.1:8000/api/auth/token/login/](http://127.0.0.1:8000/api/auth/token/login/) по POST-запросу
```json
{
    "username": "your username",
    "password": "your password",
}
```
Вход как администратор:
```json
{
    "username": "admin",
    "password": "123",
}
```

После успешной авторизации Вам в ответе от сервера придет токен, который следует вставить в заголоки запроса, обязательно, написав ключевое слово "Token" перед самим токеном:
```json
{
    "Authorization": "Token 097e6eec52033e7f3ae9ee60a46931f77cc6a159"
}
```

## Возможности проекта
`После авторизации Вам будет доступна возможность использовать эндпоинты с методом GET. Если вы зашли как администратор, то дополнительно еще можете выполнять CRUD операции с конкретными записями.`

Посмотреть все API-эндпоинты можно по адресу:
[127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

## Команда проекта

- [Копылов Денис](https://t.me/TimeToBeShine) — Fullstack-разработчик