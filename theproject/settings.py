import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#9d)zxy!nyp4vtxtj9mj@_9k#zj_3p$@dqj)3a(7&rk^la9c&+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['myapp.herokuapp.com', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework', # new
    'rest_framework.authtoken', # new
    'rest_auth', # new
    'django.contrib.sites', # new
    'allauth', # new
    'allauth.account', # new
    'allauth.socialaccount', # new
    'rest_auth.registration', # new
    'corsheaders', # new

    "theapp",
    "accounts",
    "crispy_forms",
    "ckeditor",

    # 'theapp.apps.ApiConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "corsheaders.middleware.CorsMiddleware", # New
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'theproject.urls'
AUTH_USER_MODEL = 'accounts.CustomUser'

CORS_ALLOW_ALL_ORIGINS = True


# Django All Auth config. 
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
AUTHENTICATION_BACKENDS = (    
    "django.contrib.auth.backends.ModelBackend",    
    "allauth.account.auth_backends.AuthenticationBackend",
)
SITE_ID = 1 
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_UNIQUE_EMAIL = True 

# Rest Framework config.
REST_FRAMEWORK = {    
'DATETIME_FORMAT': "%m/%d/%Y %I:%M%P",    
'DEFAULT_AUTHENTICATION_CLASSES': [        
    'rest_framework.authentication.TokenAuthentication',    
],
}
##### END NEW

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'theproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Production Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'NAME': 'PasteNameHere',
#             'USER': 'PasteUserHere',
#             'PASSWORD': 'PastePasswordHere',
#             'HOST': 'ec2-34-235-31-124.compute-1.amazonaws.com',
#             'PORT': '5432',
#         }
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Crispy Forms CSS Settings
# CRISPY_TEMPLATE_PACK="bootstrap4"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Redirect Must Be Specified For Heroku to Work
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = None