import os
import datetime

# change PROJECT_NAME to your django project name
PROJECT_NAME = 'projectname'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR,'static')
MEDIA_DIR = os.path.join(BASE_DIR,'media')


# URL from which the backend can be accessed from
ALLOWED_HOSTS = ['subdomain.example.com','subdomain1.example.com']


# ...

# Application definition
INSTALLED_APPS = [
    # ...
    # 'django.contrib.messages',
    # 'django.contrib.staticfiles',
    'corsheaders',
    # 'myapp',
    # ...
]

MIDDLEWARE = [
    # 'django.middleware.security.SecurityMiddleware',
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    # 'django.middleware.common.CommonMiddleware',
    # ...
]

# ...

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# if db.cnf is present, use mysql
if os.path.isfile(os.path.join(BASE_DIR, str(PROJECT_NAME)+'/db.cnf')):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'OPTIONS': {
                'read_default_file': os.path.join(BASE_DIR, str(PROJECT_NAME)+'/db.cnf'),
            },
        }
    }


# ...

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [STATIC_DIR,]
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'


# CORS
CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = [
       "https://example.com",
       "https://www.example.com",
       "https://subdomain.example.com",
]


# for dev
if DEBUG:
    ALLOWED_HOSTS.append('localhost')
    ALLOWED_HOSTS.append('example.ap-south-1.elasticbeanstalk.com')

    CORS_ORIGIN_WHITELIST.append("http://localhost:3000")
    CORS_ORIGIN_WHITELIST.append("http://127.0.0.1:3000")
