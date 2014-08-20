"""
Django settings for coral project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, sys
sys.path.append('./models')
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SITE_ROOT = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^o*t*qdm@2^_)68yl-qvt4fn!+mfhu6u4cn_$7p%5g+@9x09uc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # apps
    'coral',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
#DATABASES = {
#    'default': {
#        'ENGINE':   'django.db.backends.mysql',
#        'NAME':     'coral',
#        'USER':     'root',
#        'PASSWORD': 'coral',
#        'HOST':     'localhost',
#        'PORT':     3306,
#    }
#}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(SITE_ROOT, 'data.db'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(SITE_ROOT,'static')
STATICFILES_DIRS = (
    ("js", os.path.join(STATIC_ROOT,'js')),
    ("css", os.path.join(STATIC_ROOT,'css')),
    ("img", os.path.join(STATIC_ROOT,'img')),
    ("admin", os.path.join(STATIC_ROOT,'admin')),
    ("fonts", os.path.join(STATIC_ROOT,'fonts')),
    ("sound", os.path.join(STATIC_ROOT,'sound')),
    #("bootstrap3", os.path.join(STATIC_ROOT, 'bootstrap3')),
    )

# user uploads
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(SITE_ROOT, 'uploads')   



# html template path
TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates'),
    )


# automatic load custome templatetags
from django import template 
template.add_to_builtins('coral.templatetags.coral_tags')
template.add_to_builtins('django.contrib.staticfiles.templatetags.staticfiles')









