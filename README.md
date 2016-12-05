# Django-kickstarter

Django-kickstarter is a kickstarter clone made for fun.

## Prerequisities
* Python 3
* Django 1.10
* pip

## Installation Instructions
1. Clone the repository
2. Navigate into the django-kickstarter directory
3. Rename the file kickstarter/settings_secret.py.template to kickstarter/settings.py and fill the DJANGO_KEY variable
4. pip install -r requirements.txt
5. python manage.py makemigrations
6. python manage.py migrate
7. python manage.py createsuperuser
8. python manage.py runserver

You can access the home page by visiting http://www.localhost:8000
