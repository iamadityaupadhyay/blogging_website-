
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent
AUTH_USER_MODEL = 'myapp.UserImage'

SECRET_KEY = 'django-insecure-qk(98ujy)7fv(w#iz7a2+_75dde9wk8^x2!4@^wn01o#lt_56d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
import os

# Use the PORT env var in development
PORT = os.environ.get('PORT', '8000')
ALLOWED_HOSTS =['*']
  # Defaults to 8000 if PORT is not set

# Application definition
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ]
    }
}
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_BASEPATH = "/my_static/ckeditor/ckeditor/"
INSTALLED_APPS = [
    # 'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'ckeditor',
    'ckeditor_uploader',
    'rest_framework',
    'cloudinary',
    'cloudinary_storage',
    'django.contrib.sites',  # Make sure 'django.contrib.sites' is added
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
]
import os

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
       'django.contrib.auth.backends.ModelBackend',
       'allauth.account.auth_backends.AuthenticationBackend',
]
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True

SOCIALACCOUNT_PROVIDERS = {
    # 'google': {
    #     'APP': {
    #         'client_id': os.getenv('GOOGLE_CLIENT_ID'),
    #         'secret': os.getenv('GOOGLE_CLIENT_SECRET'),
    #         'key': ''
    #     }
    # },
    'github': {
        'APP': {
            'client_id': "Ov23liDNlII97CLP87o9",
            'secret':"705d2ca353c9b1fdca852247203608a4fc50cdb0",
            'key': ''
        }
    }
}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'template')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',

            ],
        },
    },
]

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://root:6PCfNuw8TfFyFOMlYyyiylHCmKk4CfJ3@dpg-cs4cn2t2ng1s739i0s80-a.singapore-postgres.render.com/blogging_jumc',
        conn_max_age=600, 
    )
}
SESSION_ENGINE = 'django.contrib.sessions.backends.db'


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # where collectstatic will copy files

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'public/static'),  # where your static files are located during development
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,"public/static")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

import cloudinary
import cloudinary.uploader
import cloudinary.api

cloudinary.config( 
  cloud_name = "djahxpuyx", 
  api_key = "888441744137892", 
  api_secret = "9L9gKxQjrQIHsfY5OFsaOAfKwyE" 
)
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': "djahxpuyx",
    'API_KEY': "888441744137892",
    'API_SECRET': "9L9gKxQjrQIHsfY5OFsaOAfKwyE",
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'