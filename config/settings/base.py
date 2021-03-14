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

    'social_django',

    'core',
    'users',
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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
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
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id,name,email', 
}

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)


LOGIN_URL = 'home'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'home'


SOCIAL_AUTH_FACEBOOK_KEY = get_secret('FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = get_secret('FACEBOOK_SECRET')

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = get_secret('GOOGLE_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = get_secret('GOOGLE_SECRET')


AUTH_USER_MODEL = 'users.User'


LANGUAGE_CODE = 'en-ca'

TIME_ZONE = 'America/Montreal'

USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = '/static/'
