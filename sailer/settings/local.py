from .base import *

SECRET_KEY = 'i8!x)4msj!_cw46$b(zcn%8t-wh9^@_)nmn8)^87zd^*ks7p29'
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(BASE_DIR), 'db.sqlite3'),
#         'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
    }
}
