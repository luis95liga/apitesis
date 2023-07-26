from .base import *
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default':  dj_database_url.config(
        default='',
        conn_max_age=600
    )
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
