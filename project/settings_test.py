#coding: utf-8
from settings import *

USE_TZ = False
DATABASE_NAME = 'simpleblog_test.db'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABASE_NAME,
    }
}