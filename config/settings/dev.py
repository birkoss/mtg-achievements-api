from .base import *


DEBUG = True


CORS_ALLOW_ALL_ORIGINS = True


ALLOWED_HOSTS = ['192.168.0.120', 'localhost']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR+"/../", 'db.sqlite3'),
    }
}
