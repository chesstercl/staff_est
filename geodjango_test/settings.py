"""
Django settings for geodjango_test project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hs*0gc=u()ty8s1&nayv0&ux8@ny0q2n8l@5omz@4ai1c5t%@_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'gps',
    'est',
    'djgeojson',
    'leaflet',
    'django_extensions',
    'qrcode',
    'corsheaders',
]

MIDDLEWARE_CLASSES = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'geodjango_test.urls'

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
        },
    },
]

WSGI_APPLICATION = 'geodjango_test.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
#    'default': {
#        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    },
#    'default':{
#        'ENGINE': 'django.contrib.gis.db.backends.postgis',
#        'NAME': 'test',
#        'HOST': '104.196.13.123',
#        'USER': 'postgres',
#        'PASSWORD': 'est.postgres',
#        'PORT': '5432',
#    },
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'gps',
        'HOST': '104.196.13.123',
        'USER': 'postgres',
        'PASSWORD': 'est.postgres',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = '/home/lautaro/development/geodjango_test/est/static/'
STATIC_URL = '/static/'

MEDIA_ROOT = '/home/lautaro/development/geodjango_test/est/media/'
MEDIA_URL = '/media/'

#DATABASE_ROUTERS = ['gps.routers.GpsRouter']

#Custom GDAL PATH

#GDAL_LIBRARY_PATH = '/usr/local/lib64/libgdal.so.1'

TASTYPIE_DEFAULT_FORMATS = ['json', 'xml', 'yaml', 'plist', 'jsonp']

CORS_ORIGIN_ALLOW_ALL = True

#CORS_ORIGIN_WHITELIST = ('/hoime/lautaro/development/gps_tracking/Test/DojoJson/', 'localhost','127.0.0.1','localhost:8000','127.0.0.1:8000')

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = (
        'GET',
        'POST',
        'PUT',
        'PATCH',
        'DELETE',
        'OPTIONS'
    )

CORS_ALLOW_HEADERS = (
        'x-requested-with',
        'content-type',
        'accept',
        'origin',
        'authorization',
        'x-csrftoken'
    )

CORS_EXPOSE_HEADERS = (
        'x-requested-with',
        'content-type',
        'accept',
        'origin',
        'authorization',
        'x-csrftoken'
    )

#APPEND_SLASH = False
