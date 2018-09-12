from .base import *


SECRET_KEY = 'p_1ec5pj&8-#)nq)c14gl66_+sreo+caphx4xs*=cm5+n$&%su'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = ['nzaniela.com']


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'polls',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': ''
    }
}