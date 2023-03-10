# Practical task 1 week
### Write a Restful CRUD API (Create, Read, Update, Delete).
### Create Student table with fields (ID,name,e-mail, phoneNumbers, etc.). 
### Need to make API with database access (Postgresql) , and controller for all crud operations.

# Manual
### 1 install Postgresql
### 2 install Django framework
#### pip instal django
### 3 install database adapter
#### pip install psycopg2
### 4 install database adapter
#### pip install djangorestframework 
### 5 change database settings in settings.py
     'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_user'(default is 'postgres'),
        'PASSWORD': 'your_password',
        'HOST': 'your_host'(default is 'localhost'),
        'PORT': 'your_port'(default is '5432'),
    }
### 6 migrate data model to database
#### python manage.py makemigrations
#### python manage.py migrate
### 7 run
#### python manage.py runserver
