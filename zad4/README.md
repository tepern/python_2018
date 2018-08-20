# Веб-приложение для заказа пиццы

## Технологии

* [Flask](http://flask.pocoo.org/)
* [Bootstrap](https://getbootstrap.com)

## Инструкция

* Установка зависимостей
```
pip install -r requirements.txt
```

* Инициализация базы данных (создание схемы БД)
```
python init_db.py
```

* Загрузка фейковых данных для тестирования
```
python load_fixtures.py
```

* Включение DEBUG-режима (опционально)
```
export FLASK_ENV=development
```

* Запуск веб-сервиса
```
flask run
```
#Для просмотра списка заказов и изменения статуса заказа необходимо перейти на страницу \admin