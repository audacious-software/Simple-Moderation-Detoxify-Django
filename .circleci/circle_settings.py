# pylint: skip-file

"""
Settings.py for testing on Travis CI.
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import tempfile

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'foobar' # nosec

DEBUG = False
ADMINS = [('Chris Karr', 'chris@audacious-software.com')]

ALLOWED_HOSTS = ['example.com']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'prettyjson',
    'quicksilver',
    'django_dialog_engine',
    'django_dialog_engine_builder',
    'simple_moderation',
    'simple_moderation_detoxify',
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'sm.urls'

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

WSGI_APPLICATION = 'pdk.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE':   'django.contrib.gis.db.backends.postgis',
        'NAME':     'circle_test',
        'USER':     'root',
        'PASSWORD': '',
        'HOST':     'localhost',
        'PORT':     '',
    }
}

# if 'test' in sys.argv or 'test_coverage' in sys.argv: #Covers regular testing and django-coverage
#    DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.spatialite'
#     SPATIALITE_LIBRARY_PATH = 'mod_spatialite'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = str(BASE_DIR) + '/media/'

SIMPLE_DASHBOARD_SITE_NAME = 'Simple Messaging Testing'

SIMPLE_DATA_EXPORTER_OBFUSCATE_IDENTIFIERS = True
SIMPLE_DATA_EXPORTER_SITE_NAME = 'Simple Messaging Site'
SIMPLE_MESSAGING_SECRET_KEY = 'changeme' # nosec

SIMPLE_MESSAGING_COUNTRY_CODE = 'US'

SITE_URL = 'https://' + ALLOWED_HOSTS[0]

QUICKSILVER_LOCK_DIR =  tempfile.gettempdir()
