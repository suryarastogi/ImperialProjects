"""
Django settings for ghostapi project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_l$(8(+o$kips0d+nv@9p#@stnu$vg=6jx3sa&v3xt+ms7*4+6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# For asynchronous execution or synchronous
ASYNCH_EXEC = False

# Celery Settings
#BROKER_URL = "amqp://aew13:bubbler420@146.169.45.142:5672"
#BROKER_URL = "amqp://guest:guest@146.169.47.40:5672//"
#BROKER_URL = "amqp://guest:guest@146.169.47.94:5672//"
BROKER_URL = "amqp://guest:guest@localhost:5672//"


CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend'
CELERY_DEFAULT_QUEUE = "ghostapi"
CELERY_DEFAULT_EXCHANGE = "ghostapi"
CELERY_DEFAULT_EXCHANGE_TYPE = "direct"
CELERY_DEFAULT_ROUTING_KEY = "ghostapi"

CORS_ORIGIN_ALLOW_ALL = True

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'csvImporter',
    'rest_framework',
    'djcelery',
    'openapi',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
)

ROOT_URLCONF = 'ghostapi.urls'

WSGI_APPLICATION = 'ghostapi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
    #'default': {
    #    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #    'NAME': 'sr3213',                      
    #    'USER': 'sr3213',
    #    'PASSWORD': ,
    #    'HOST': 'db-new.doc.ic.ac.uk',
    #    'PORT': '5432',
    #}
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
