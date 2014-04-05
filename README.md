Начало работы с Джанго
======================

Содержание этого репозитория:
- [guestbook](guestbook) - старая и кривая версия гостевой книги
- [new_guestbook](new_guestbook) - новая версия на шаблоне от Джанго 1.6

Что читать
----------

- [Документация на русском](http://djbook.ru/rel1.6/) - там есть раздел "Первые шаги"
- [Мои лекции на Зимней пущинской школе](http://www.zpsh.ru/files/Slon2013/%D0%9A%D1%83%D1%80%D1%81%D1%8B/Python/Django/) - в разделе `teacher_resources/handouts` можно найти пошаговые инструкции

Устанавливаем Джанго на Виндоуз
-------------------------------

1. Устанавливаем [setuptools](http://www.lfd.uci.edu/~gohlke/pythonlibs/#setuptools)
и [pip](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip)

2. Открываем консоль: Пуск → Выполнить, набираем `cmd`, нажимаем Enter. Доходим до директории
с установленными pip-ом и запускаем установку Джанго.
        
        cd C:\Python33\Scripts
        pip.exe install django

Для удобства использования скриптов Питона можно добавить директорию `C:\Python33\Scripts`
в переменную `PATH`. Гуглите "установка переменной окружения path windows".


Устанавливаем Джанго на Убунту
------------------------------

        sudo apt-get install python3-setuptools
        sudo easy_install3 pip
        sudo pip-3.3 install django

Создаём проект на Виндоуз
-------------------------

Открываем консоль. Внутри командами `cd` и `dir`, используя клавишу Tab, доходим до директории, в которой хотим создать проект. Дальше говорим

        C:\Python33\Scripts\django-admin.py startproject guestbook
        cd guestbook
        manage.py runserver

В браузере заходим на [http://127.0.0.1:8000/](http://127.0.0.1:8000/) и убеждаемся в том, что сервер разработчика успешно запустился.


Создаём проект на Убунту
------------------------

Открываем терминал. Внутри командами `cd` и `ls`, используя клавишу Tab, доходим до директории, в которой хотим создать проект. Дальше говорим

        which django-admin.py
        django-admin.py startproject guestbook
        cd guestbook
        python3 manage.py runserver

В браузере заходим на [http://127.0.0.1:8000/](http://127.0.0.1:8000/) и убеждаемся в том, что сервер разработчика успешно запустился.


Раскладка файлов в new_guestbook
--------------------------------

Для создания своих таблиц в базе данных нам надо создать приложение (application):

        python3 manage.py startapp messages

В нашем проекте имеем следующую раскладку файлов:

        new_guestbook/
        |-- manage.py   (скрипт для работы с проектом. нам нужны его параметры syncdb, runserver)
        |-- db.sqlite3   (файл базы данных sqlite3, будет создан командой syncdb)
        |-- new_cdguestbook/   (директория глобальных настроек проекта)
        |    |-- __init__.py   (его наличие превращает папку в питоновский модуль)
        |    |-- settings.py   (файл с настройками языка, расширений, базы данных и прочего)
        |    |-- urls.py   (файл со связями между url-адресами и функциями-обработчиками)
        |    |-- wsgi.py   (файл, нужный для связи проекта с продакшн-серверами. нам не понадобится)
        |-- messages/   (директория глобальных настроек проекта)
        |    |-- __init__.py   (его наличие превращает папку в питоновский модуль)
        |    |-- admin.py   (настройки интерфейса администратора сайта)
        |    |-- tests.py   (тесты на проверку правильности кода приложения)
        |    |-- models.py   (файл с описанием таблиц в базе данных)
        |    |-- views.py   (файл с функциями-обработчиками запросов)
        |    |-- templates/*   (директория шаблонов html-страничек)

* - эти файлы и директории нужно создать самому.

Задание
=======

Реализовать вики-движок (как на Википедии). Пользователь приходит по адресам типа `Сова/` и `Сова/edit`.
В первом случае он просматривает содержимое страницы. Во втором случае - редактирует её.

Feature list:
- можно заходить по обоим типам ссылок и делать описанные операции (30 баллов)
- на главной странице отображается список всех имеющихся статей (10 баллов)
- вики-движок хранит версии каждой статьи, можно просмотреть каждую старую версию и откатить статью до неё (10 баллов)
- версии можно сравнивать между собой (10 баллов)
- прикручена авторизация, анонимное редактирование недоступно (10 баллов)
- сайт выложен на хостинг - например, на [pythonanywhere](http://pythonanywhere.com/) (10 баллов)
