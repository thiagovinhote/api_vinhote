"""
Django settings for api_vinhote project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os
import dj_database_url
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g4bl00u&7e!zek7q_(0z0$*y329m9g=@n&%85=x7d!)(7wgl0z'

# SECURITY WARNING: don't run with debug turned on in production!
# Loading data for development enviroment
try:
  ret = os.environ['DEBUG']
  print('DSV')
  DEBUG = True
except KeyError:
  print('PRD')
  DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

DEFAULT_APPS = [
  'django.contrib.sites',
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
  'rest_framework',
  'rest_framework.authtoken',
  'allauth',
  'allauth.account',
  'allauth.socialaccount',
  'rest_auth',
  'rest_auth.registration',
  'storages',
  'django_filters',
  'whitenoise.runserver_nostatic',
  'corsheaders',
]

LOCAL_APPS = [
  'api',
]

INSTALLED_APPS = LOCAL_APPS + THIRD_PARTY_APPS + DEFAULT_APPS

SITE_ID = 1

MIDDLEWARE = [
  'corsheaders.middleware.CorsMiddleware',
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'whitenoise.middleware.WhiteNoiseMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'api_vinhote.urls'

REST_USE_JWT = True

JWT_AUTH = {
  'JWT_ALLOW_REFRESH': True,
  'JWT_AUTH_HEADER_PREFIX': 'Bearer',
  'JWT_EXPIRATION_DELTA': timedelta(hours=1),
  'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=7),
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_PERMISSION_CLASSES': (
      'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
      'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
      'rest_framework.authentication.SessionAuthentication',
    ),
    'PAGE_SIZE': 100,
}

REST_AUTH_SERIALIZERS = {
  'USER_DETAILS_SERIALIZER': 'api.serializers.UserSerializerAuth',
}

AUTHENTICATION_BACKENDS = (
  'django.contrib.auth.backends.ModelBackend',
  'allauth.account.auth_backends.AuthenticationBackend',
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {
      'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
      ],
      'debug': DEBUG
    },
  },
]

WSGI_APPLICATION = 'api_vinhote.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
  }
}

DATABASES['default'] =  dj_database_url.config()
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Storage
DEFAULT_FILE_STORAGE = 'storages.backends.gs.GSBotoStorage'
GS_ACCESS_KEY_ID = 'GOOGNWLB4ZEJTDA32YJA'
GS_SECRET_ACCESS_KEY = 'TOl0h3OwIj1wrz1D6bgnqvl6XylyQXnT5g72vPnw'
GS_BUCKET_NAME = 'vinhotestorage'

# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
  {
    'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
  },
  {
    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
  },
  {
    'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
  },
  {
    'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
  },
]


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'Brazil/East'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
  os.path.join(PROJECT_ROOT, 'static'),
]

AUTH_USER_MODEL = 'api.User'
# ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
# ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username'
