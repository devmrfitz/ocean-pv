# I have used a .env file and python-decouple in place of environment variables.
# You can use that or just use development_settings.py

import os

from decouple import config, Csv

from .settings import *

DEBUG = config('DEBUG', cast=bool)
DEBUG = True

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

SECRET_KEY = config('SECRET_KEY')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = config('EMAIL_HOST')

EMAIL_PORT = config('EMAIL_PORT', cast=int)

EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)

EMAIL_HOST_USER = config('EMAIL_HOST_USER')

EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

GOOGLE_RECAPTCHA_SECRET_KEY = config('GOOGLE_RECAPTCHA_SECRET_KEY')

GOOGLE_RECAPTCHA_SITE_KEY = config('GOOGLE_RECAPTCHA_SITE_KEY')
