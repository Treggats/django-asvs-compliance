"""
Django settings for asvs project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import json
import datetime
from pathlib import Path

PROJECT_PACKAGE = Path(__file__).resolve().parent.parent
BASE_DIR = PROJECT_PACKAGE.parent
DATA_DIR = PROJECT_PACKAGE.parent

try:
    with DATA_DIR.joinpath("conf", "secrets.json").open() as handle:
        SECRETS = json.load(handle)
except IOError:
    SECRETS = {
        "secret_key": "a secret",
        "db_type": "postgresql_psycopg2",
        "db_name": "cookie",
        "db_user": "carlos",
        "db_password": "",
        "db_host": "",
        "db_port": ""
    }

# Set the default ASVS version
ASVS_VERSION = 3
ASVS_RELEASE_DATE = datetime.date(2015, 10, 9)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(SECRETS['secret_key'])

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

MARKDOWN_EDITOR_SKIN = 'simple'
MARKDOWN_EXTENSIONS = ['extra']

# Application definition
PREREQ_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

DEPENDENCY_APPS = [
    'hvad',
    'django_markdown',
]

PROJECT_APPS = [
    'asvsrequirement',
    'asvsannotation',
    'reporting',
]
INSTALLED_APPS = PREREQ_APPS + DEPENDENCY_APPS + PROJECT_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'asvs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'asvs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.{}'.format(str(SECRETS['db_type'])),
        'NAME': str(SECRETS['db_name']),
        'USER': str(SECRETS['db_user']),
        'PASSWORD': str(SECRETS['db_password']),
        'HOST': str(SECRETS['db_host']),
        'PORT': str(SECRETS['db_port']),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
# http://django-hvad.readthedocs.org/en/latest/
LANGUAGE_CODE = 'en-us'
LANGUAGES = (('en-us', 'English'),)

TIME_ZONE = 'Europe/Amsterdam'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = str(BASE_DIR.joinpath('static'))