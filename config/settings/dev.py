from .base import *


DEBUG = True


CORS_ALLOW_ALL_ORIGINS = True


ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR+"/../", 'db.sqlite3'),
    }
}
