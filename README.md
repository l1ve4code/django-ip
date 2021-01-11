# Инженерный Проект: «Продажа недвижимости»

1. Проектирование и создание реляционной базы данных для веб-сервиса или приложения по предметной области, которая предложена вам по варианту.
2. Создать и настроить административную панель для управления базой данных с помощью фреймворка Django.
3. Изучить формат Json и реализовать RESTfull API, разобраться с инструментом Postman

# Ссылки на проект

[Лэндинг проекта](http://landing.std-926.ist.mospolytech.ru)

[Ссылка на рабочую версию](ip-2021.std-926.ist.mospolytech.ru)

[Ссылка на документацию/ видео](https://drive.google.com/drive/folders/1BpbDnRJ9BwmLiVbUdePnTdIxlnX8WmKi?usp=sharing)

# Ссылки на REST-API

### Районы

[Таблица районы (Создание)](ip-2021.std-926.ist.mospolytech.ru/api/vl/data/rayoni/create/)

[Таблица районы (Все)](ip-2021.std-926.ist.mospolytech.ru/api/vl/data/rayoni/all/)

[Таблица районы (Детально)](ip-2021.std-926.ist.mospolytech.ru/api/vl/data/rayoni/detail/1/)

### Города

[Таблица города (Создание)](ip-2021.std-926.ist.mospolytech.ru/api/vl/data/gorod/create/)

[Таблица города (Все)](ip-2021.std-926.ist.mospolytech.ru/api/vl/data/gorod/all/)

[Таблица города (Детально)](ip-2021.std-926.ist.mospolytech.ru/api/vl/data/gorod/detail/1/)

### Операции

[Таблица операции (Создание)](ip-2021.std-926.ist.mospolytech.ru/api/vl/data/operahii/create/)

[Таблица операции (Все)](ip-2021.std-926.ist.mospolytech.ru/api/vl/data/operahii/all/)

[Таблица операции (Детально)](ip-2021.std-926.ist.mospolytech.ru/api/vl/data/operahii/detail/1/)

### Роли

[Таблица роли (Создание)](ip-2021.std-926.ist.mospolytech.ru/api/vl/data/role/create/)

[Таблица роли (Все)](ip-2021.std-926.ist.mospolytech.ru/api/vl/data/role/all/)

[Таблица роли (Детально)](ip-2021.std-926.ist.mospolytech.ru/api/vl/data/role/detail/1/)

### Пользователи

[Таблица пользователи (Создание)](ip-2021.std-926.ist.mospolytech.ru/api/vl/data/polzovateli/create/)

[Таблица пользователи (Все)](ip-2021.std-926.ist.mospolytech.ru/api/vl/data/polzovateli/all/)

[Таблица пользователи (Детально)](ip-2021.std-926.ist.mospolytech.ru/api/vl/data/polzovateli/detail/1/)

### Предложения

[Таблица предложения (Создание)](ip-2021.std-926.ist.mospolytech.ru/api/vl/data/predlozheniya/create/)

[Таблица предложения (Все)](ip-2021.std-926.ist.mospolytech.ru/api/vl/data/predlozheniya/all/)

[Таблица предложения (Детально)](ip-2021.std-926.ist.mospolytech.ru/api/vl/data/predlozheniya/detail/1/)

### Тарифы

[Таблица тарифы (Создание)](ip-2021.std-926.ist.mospolytech.ru/api/vl/data/tariphy/create/)

[Таблица тарифы (Все)](ip-2021.std-926.ist.mospolytech.ru/api/vl/data/tariphy/all/)

[Таблица тарифы (Детально)](ip-2021.std-926.ist.mospolytech.ru/api/vl/data/tariphy/detail/1/)

### Спрос

[Таблица спрос (Создание)](ip-2021.std-926.ist.mospolytech.ru/api/vl/data/spros/create/)

[Таблица спрос (Все)](ip-2021.std-926.ist.mospolytech.ru/api/vl/data/spros/all/)

[Таблица спрос (Детально)](ip-2021.std-926.ist.mospolytech.ru/api/vl/data/spros/detail/1/)

### Страховой

[Таблица страховой (Создание)](ip-2021.std-926.ist.mospolytech.ru/api/vl/data/straxovoi/create/)

[Таблица страховой (Все)](ip-2021.std-926.ist.mospolytech.ru/api/vl/data/straxovoi/all/)

[Таблица страховой (Детально)](ip-2021.std-926.ist.mospolytech.ru/api/vl/data/straxovoi/detail/1/)

### Сделки

[Таблица сделки (Создание)](ip-2021.std-926.ist.mospolytech.ru/api/vl/data/sdelki/create/)

[Таблица сделки (Все)](ip-2021.std-926.ist.mospolytech.ru/api/vl/data/sdelki/all/)

[Таблица сделки (Детально)](ip-2021.std-926.ist.mospolytech.ru/api/vl/data/sdelki/detail/1/)

# Задачи

| №1  | Этап                                                                                                                                 | Ориентировочное время (часов) |
| --- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------- |
| 1   | Анализ аналогов (поиск отечественных и зарубежных сайтов, анализ структуры сайта, функциональности)                                  | 2                             |
| 2   | Проектирование инфологической модели предметной области (Модель "Сущность-Связь"), концептуальное проектирование                     | 3                             |
| 3   | Проектирование физической структуры (конкретные таблицы, столбцы и связи между ними).                                                | 2                             |
| 4   | Создание django-приложения, сохранение проекта в GIT, запуск проекта на сервере fit.mospolytech.ru, изучение документации фреймворка | 3                             |
| 5   | Настройка административного интерфейса Django                                                                                        | 3                             |
| 6   | Наполнение базы данных. Продумывание кейсов использования административной панели, донастройка интерфейса.                           | 2                             |
| 7   | Реализация REST API (минимум два примера url). Разобраться с тестированием API через сервис Postman                                  | 2                             |
| 8   | Реализация импорта и экспорта данных в базу данных, например, с помощью django-import-export или аналогов                            | 3                             |
| 9   | Написание минимум 5 типовых запросов к базе данных                                                                                   | 3                             |
| 10  | Документирование (подробное описание этапов работы над проектом, в том числе структура базы данных, типовые запросы к БД, и т.д.)    | 3                             |
| 11  | Заполнение оценочного листа по проекту (см. шаблон), подготовка к защите.                                                            | 1                             |

# Разработчик

| Учебная группа | Имя пользователя | ФИО           |
| -------------- | ---------------- | ------------- |
| 191-322        | @l1ve4code       | Веденин И. С. |

# Пользователи

| Логин | Пароль |
| ----- | ------ |
| admin | admin  |
| user  | user   |
