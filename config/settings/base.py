import json
import os

from django.core.exceptions import ImproperlyConfigured


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


try:
    with open('secrets.json') as f:
        secrets = json.load(f)
except FileNotFoundError:
    raise ImproperlyConfigured('Fill the secrets.json file')


def get_secret(setting, secrets=secrets):
    '''
    Get the secret variable or return explicit exception.
    '''
    try:
        return secrets[setting]
    except KeyError:
        error_msg = 'Set the {0} environment 􏰁→ variable'.format(setting)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_secret('SECRET_KEY')


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',

    'core',
    'users',

    'achievements',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'config.urls'


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

WSGI_APPLICATION = 'config.wsgi.application'


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # nopep8
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # nopep8
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # nopep8
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # nopep8
    },
]


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)


LOGIN_URL = 'home'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'


AUTH_USER_MODEL = 'users.User'


LANGUAGE_CODE = 'en-ca'

TIME_ZONE = 'America/Montreal'

USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = '/static/'
