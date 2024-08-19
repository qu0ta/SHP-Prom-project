# Документация по проекту Final Prom Project

Проект представляет собой новостной сайт с функцией авторизации.

## Начало работы

 1. Склонируйте репозиторий: 
 
	`git clone https://gitlab.informatics.ru/stanislaw/final-prom-project.git`

2. Установить версию Python>=3.9
3. Создать и активировать виртуальное окружение:
`python -m venv venv`
`venv/Scripts/activate`
4. Установить зависимости:
`pip install -r final_prom_project/requirement.txt`
5. Начать работу!
`cd final_prom_project`
`python manage.py runserver`

    

## В проекте присутствует автодокументация

Для ее работы необходимо зайти в папку **docs**, затем в терминале прописать команду:
`make.bat html`

Далее в **docs/build/html** появится файл **index.html** со всей имеющейся документацией.

## Тестирование

Для тестов был выбран фреймворк Django Testing Framework. Для запуска тестов необходимо в корневой папке проекта прописать команду:
` coverage run --source=. --omit='*/migrations/*,*/tests/*' manage.py test`
А затем, чтобы увидеть покрытие кода:
`covarage report`