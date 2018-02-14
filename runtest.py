#!/usr/bin/env python
import os
import sys
import django
from django.conf import settings
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

installed_apps = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'calfile'
]


DEFAULT_SETTINGS = dict(
    ALLOWED_HOSTS=['localhost'],
    ROOT_URLCONF='calfile.urls',
    STATIC_URL='/static/',
    INSTALLED_APPS=installed_apps,
    CALFILE_DF = '%d-%m-%Y %H:%M',
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        }
    },
    MIDDLEWARE_CLASSES=[
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    ],
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
            ]
        },
    }],
)


def main():

    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)
    if hasattr(django, 'setup'):
        django.setup()
    try:
        from django.test.runner import DiscoverRunner
    except ImportError:
        from django.test.simple import DjangoTestSuiteRunner
        failures = DjangoTestSuiteRunner(failfast=False).run_tests(['tests'])
    else:
        failures = DiscoverRunner(failfast=False).run_tests(['calfile.tests'])
    sys.exit(failures)


if __name__ == "__main__":
    # logging.basicConfig()
    main()
