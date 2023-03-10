#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


# Написать API Restful CRUD (Create, Read, Update, Delete).
# Создать таблицу Student с полями (ID,name,e-mail,# phoneNumbers, и тд).
# Нужно сделать API с обращением в базу данных(Postgresql) , и контроллер для всех crud операций.

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'praktika1.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
