"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import dj_database_url
import environ
import os

import cloudinary
import cloudinary.uploader
import cloudinary.api
from datetime import timedelta

from environ import Env
env = Env()
Env.read_env()
ENVIRONMENT = env('ENVIRONMENT', default='production')


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
if ENVIRONMENT == 'development':
    DEBUG = True
else:
    DEBUG = False

# DEBUG = True
ALLOWED_HOSTS = ['*']


# Application definition

    

INSTALLED_APPS = [
    # 'account.apps.AccountConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.sites',
    'account',
    'cloudinary_storage',
    'cloudinary',
    

    'carzz',
    # 'carzz_api',

    'rest_framework',
    'rest_framework.authtoken',

    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'djoser',

    'dj_rest_auth',
    'dj_rest_auth.registration',

    # other apps
    # 'debug_toolbar',
    'tailwind',
    'theme',
    'django_browser_reload',
    # 'social_django',
    # 'django_extensions',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.google',


]

SITE_ID = 1

# ACCOUNT_USER_MODEL_USERNAME_FIELD = None
# ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_UNIQUE_EMAIL = True


# ACCOUNT_FORMS = {
#     'login': 'account.forms.CustomLoginForm',
# }

# SOCIAL_ACCOUNT_PROVIDERS = {
#     "google":{
#         "SCOPE":[
#             "profile",
#             "email"
#         ],
#         "AUTH_PARAMS": {"access_type":"online"}
#     }
# }

TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    "127.0.0.1"
]

NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"

MIDDLEWARE = [
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_browser_reload.middleware.BrowserReloadMiddleware',
    'allauth.account.middleware.AccountMiddleware',

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
                'carzz.context_processors.dealer_profile_context',
                
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

POSTGRES_LOCALLY = False
if ENVIRONMENT == 'production' or POSTGRES_LOCALLY == True:
    DATABASES['default'] = dj_database_url.parse(env('DATABASE_URL'))



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = 'media/'


if ENVIRONMENT == 'production' or POSTGRES_LOCALLY == True:
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    CLOUDINARY_STORAGE = { 
        'CLOUD_NAME': env('CLOUD_NAME'), 
        'API_KEY': env('CLOUD_API_KEY') ,
        'API_SECRET': env('CLOUD_API_SECRET'), 
        'SECURE': True, 
        
    }
    cloudinary.config(
            cloud_name=env('CLOUD_NAME'),
            api_key=env('CLOUD_API_KEY'),
            api_secret=env('CLOUD_API_SECRET'),
        )
else:
    MEDIA_ROOT = BASE_DIR / 'media'

cloudinary.config(
            cloud_name=env('CLOUD_NAME'),
            api_key=env('CLOUD_API_KEY'),
            api_secret=env('CLOUD_API_SECRET'),
        )



# Googl 0Auth
# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = env('GOOGLE_OAUTH2_KEY')
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = env('GOOGLE_OAUTH_SECRET')


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'my_account.CustomUser'




if ENVIRONMENT == 'production' or POSTGRES_LOCALLY == True:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = env('EMAIL_ADDRESS')
    EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    DEFAULT_FROM_EMAIL = f'Carzz {env("EMAIL_ADDRESS")}'
    ACCOUNT_EMAIL_SUBJECT_PREFIX = ''
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    

# INTERNAL_IPS = [
#     '127.0.0.1', 
#     'localhost:8000', # Add your local IPs
# ]

ACCOUNT_USERNAME_BLACKLIST = ['theboss']



# AUTHENTICATION_BACKENDS = [
#     'django.contrib.auth.backends.ModelBackend',  # Default Django backend
#     # 'allauth.account.auth_backends.AuthenticationBackend',  # Allauth backend
# ]


# Use email as the unique identifier
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'optional'  
ACCOUNT_AUTHENTICATION_METHOD = "email" 

ACCOUNT_SIGNUP_REDIRECT_URL = None
ACCOUNT_LOGIN_REDIRECT_URL = None



# SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI = 'https://127.0.0.1:8000/social-auth/complete/google-oauth2/'
# SOCIAL_AUTH_REDIRECT_IS_HTTPS = True

LOGIN_REDIRECT_URL = "/"


# REST_FRAMEWORK = {
#     "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
#     "DEFAULT_AUTHENTICATION_CLASSES": (
#         'rest_framework.authentication.SessionAuthentication',
#         "rest_framework_simplejwt.authentication.JWTAuthentication",
#     ),
# }

# SIMPLE_JWT = {
#     "AUTH_HEADER_TYPES": ("Bearer",),
#     "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
#     "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
#     "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
# }


# DJOSER CONFIG
DJOSER = {
    "LOGIN_FIELD": "email",
    "USER_CREATE_PASSWORD_RETYPE": True,
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "SEND_CONFIRMATION_EMAIL": True,
    # "SET_USERNAME_RETYPE": True,
    "SET_PASSWORD_RETYPE": True,
    "USERNAME_RESET_CONFIRM_URL": "password/reset/confirm/{uid}/{token}",
    "PASSWORD_RESET_CONFIRM_URL": "email/reset/confirm/{uid}/{token}",
    "ACTIVATION_URL": "activate/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": True,
    # "SOCIAL_AUTH_TOKEN_STRATEGY": "djoser.social.token.jwt.TokenStrategy",
    # "SOCIAL_AUTH_ALLOWED_REDIRECT_URIS": [
    #     "your redirect url",
    #     "your redirect url",
    # ],
    "SERIALIZERS": {
        "user_create": "carzz_api.serializers.UserCreateSerializer",  # custom serializer
        "user": "djoser.serializers.UserSerializer",
        "current_user": "djoser.serializers.UserSerializer",
        "user_delete": "djoser.serializers.UserSerializer",
    },
}

DOMAIN = 'localhost:3000'
SITE_NAME = 'Carzz'

# REST_AUTH_REGISTER_SERIALIZERS = {
#     'REGISTER_SERIALIZER': 'carzz_api.serializers.RegistrationSerializer',
# }