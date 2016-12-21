# -*- coding: utf-8 -*-
"""
Django settings for manualDoBixo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, sys
from imp import reload
from .social import *
from handbook.info import *


reload(sys)
sys.setdefaultencoding('utf-8')


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.dirname(__file__)



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#!ld1!qzpp=*)ryiujhwi(7t3f-3k($7ubd#2ps433_7t78haq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['www.manualdobixo.quixada.ufc.br']
#ALLOWED_HOSTS = ['*']

# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.syndication',
)
THIRD_PARTY_APPS = (
    'rosetta',
    'rest_framework',
    'social.apps.django_app.default', 
    'versatileimagefield',
)

LOCAL_APPS = (
    'handbook',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

from django.core.urlresolvers import reverse_lazy

AUTH_USER_MODEL = 'handbook.Person'
LOGIN_URL = reverse_lazy('handbook:login')
LOGOUT_URL = reverse_lazy('handbook:logout')




TEMPLATE_DIRS = (
    'handbook/templates',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)



MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'



TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',

    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

VERSATILEIMAGEFIELD_SETTINGS = {
     # The amount of time, in seconds, that references to created images
     # should be stored in the cache. Defaults to `2592000` (30 days)
    'cache_length': 2592000,
    # The name of the cache you'd like `django-versatileimagefield` to use.
    # Defaults to 'versatileimagefield_cache'. If no cache exists with the name
    # provided, the 'default' cache will be used instead.
    'cache_name': 'versatileimagefield_cache',
    # The save quality of modified JPEG images. More info here:
    # http://pillow.readthedocs.org/en/latest/handbook/image-file-formats.html#jpeg
    # Defaults to 70
    'jpeg_resize_quality': 70,
    # The name of the top-level folder within storage classes to save all
    # sized images. Defaults to '__sized__'
    'sized_directory_name': '__sized__',
    # The name of the directory to save all filtered images within.
    # Defaults to '__filtered__':
    'filtered_directory_name': '__filtered__',
    # The name of the directory to save placeholder images within.
    # Defaults to '__placeholder__':
    'placeholder_directory_name': '__placeholder__',
    # Whether or not to create new images on-the-fly. Set this to `False` for
    # speedy performance but don't forget to 'pre-warm' to ensure they're
    # created and available at the appropriate URL.
    'create_images_on_demand': True
}

ROOT_URLCONF = 'manualDoBixo.urls'


#Admin
ADMINS = ( (u'Ciano Saraiva',u'saraiva.ufc@gmail.com'), )


#EMAIL
EMAIL_ADMINS = [u'saraiva.ufc@gmail.com',]
DEFAULT_FROM_EMAIL= u'saraiva.ufc@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = u'saraiva.ufc@gmail.com'
EMAIL_HOST_PASSWORD = u'******************'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


#Social Auth
SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_USER_MODEL = 'handbook.Person'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = reverse_lazy('handbook:index')
SOCIAL_AUTH_LOGIN_URL = '/'
SOCIAL_AUTH_FORCE_POST_DISCONNECT = True
SOCIAL_AUTH_FORCE_EMAIL_VALIDATION = True
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['first_name', 'last_name', 'email']
SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.mail.mail_validation',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
)


# ST_RATELIMIT_ENABLE = True
# ST_RATELIMIT_CACHE_PREFIX = 'srl'
# ST_RATELIMIT_CACHE = 'default'


# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'handbook_cache',
#     },
# }

# CACHES.update({
#     'djconfig': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#     },
# })
WSGI_APPLICATION = 'manualDoBixo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'default' : {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'manualdobixo',                      
       'USER': 'postgres',
       'PASSWORD': '****************',
       'HOST': '******************',
       'PORT': '****',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/


LOCALE_PATHS = (
        os.path.join(PROJECT_DIR, '../handbook/locale'),
        '/var/local/translations/locale',
)
LANGUAGES = (
        ('pt_BR', ('Brazilian Portuguese')),
        ('en', ('English')),
        ('es', ('Spanish')),
)

LANGUAGE_CODE = 'pt_BR'


TIME_ZONE = 'America/Fortaleza'



USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATICFILES_DIRS = (os.path.join(PROJECT_DIR, '../handbook/static'),)


MEDIA_ROOT= os.path.join(PROJECT_DIR, '../media')
MEDIA_URL='/media/'

STATIC_ROOT = os.path.join(PROJECT_DIR, '.')

STATIC_URL = '/static/'
