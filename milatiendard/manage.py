#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'milatiendard.settings')
    environment = os.getenv('DJANGO_ENV', 'development')

    if environment == 'production':
        os.environ['DJANGO_SETTINGS_MODULE'] = 'milatiendard.settings_prod'
    elif environment == 'staging':
        os.environ['DJANGO_SETTINGS_MODULE'] = 'milatiendard.settings_local'

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
