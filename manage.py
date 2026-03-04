#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""

    # Set the default settings module for the Django project
    # This tells Django which configuration file to use.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatbot_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Execute the management command passed in the terminal
    # Example: python manage.py runserver
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
