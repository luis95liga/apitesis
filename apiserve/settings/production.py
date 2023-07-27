from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = False
ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default':  {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'trasrouter',
        'USER': 'postgres',
        'PASSWORD': 'luis1234',
        'HOST': '44.216.248.16',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
