#!/usr/bin/python
from .base import *
import dj_database_url

# Turn off the debug mode.
DEBUG = False

# Set up the secret key
SECRET_KEY = get_env_var('DJANGO_SECRET_KEY')

#... Set this up if you can take over the proxy server I thought.
SECURE_PROXY_SSL_HEADER=('HTTP_X_FORWARDED_PROTO','https')

# root directory of the static files.
STATIC_ROOT= 'static'

# set up the database 
DATABASES={
	'default': dj_database_url.config()
}

# Allow connections to this site.
ALLOWED_HOSTS = [*]