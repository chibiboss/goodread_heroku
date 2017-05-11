from .base import *
import os

SECRET_KEY = 'uoa93enc3zui8hx&pqyzxikncagrvmrrbs62xk'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_goodreads',
        'USER': 'admin_goodreads',
        'PASSWORD':'goodreads2017',
        'HOST':'localhost',
        'PORT':'5432'
    }
}