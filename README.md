# Приклад Веб-сайту на Django4 присвячений "Prozzoro"
prozzoro for ZODA


[![Python Version](https://img.shields.io/badge/python-3.11-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-4.0-brightgreen.svg)](https://djangoproject.com)
Звичайний сайт, реалізований на веб-фреймворку Django 4

Як веб-інтерфейс використано фреймворк Bootstrap https://getbootstrap.com/

![ToDo на Django](/zoda_img.png)

## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/ajax3101/prozzoro.git
```

```bash
    python3 -m venv venv
    . venv/bin/activate
 ```

Install the requirements:

```bash
 pip install -r requirements.txt
```

Run

```bash

 python manage.py makemigrations 
 python manage.py migrate
 python manage.py createsuperuser --email admin@example.com --username admin
 python manage.py runserver 
```
