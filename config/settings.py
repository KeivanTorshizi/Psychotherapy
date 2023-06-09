"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from decouple import config



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOGIN_REDIRECT_URL = "account:home"
LOGIN_URL = "login"
LOGOUT_REDIRECT_URL = "login"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7pzizuq4&ni_p6ih3^al35)3$x+ghl%zx+jp0&7^bskbj0%tad'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_jalali',
    'widget_tweaks',
    'bootstrap_modal_forms',
    'crispy_forms',
    'django_gravatar',
    'formtools',
    'psychotherapy',
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
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'data/db.sqlite3'),
    }
}



# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LC_ALL='fa_IR'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

TEMPLATETAGS_URL = '/templatetags/'
TEMPLATETAGS_ROOT = os.path.join(BASE_DIR, 'templatetags')

CRISPY_TEMPLATE_PACK = 'bootstrap4'
# AUTH_USER_MODEL = 'account.User'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = config('EMAIL_HOST')
# EMAIL_USE_TLS = True
# EMAIL_PORT = config('EMAIL_PORT')
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp-mail.outlook.com'
# EMAIL_HOST_USER = 'zandimmigration@outlook.com'
# EMAIL_HOST_PASSWORD = 'eZ@nd2635!'
# EMAIL_PORT = 25

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'dr.zandimmigration@gmail.com'
# EMAIL_HOST_PASSWORD = 'uingerpzehetvyfo'
# EMAIL_USE_TLS = True
# # EMAIL_PORT = 587
# EMAIL_PORT_SSL = 465

FILE_UPLOAD_HANDLERS= [
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]

# DIDAR_INFO={
#     'apikey': 'rs2fbexf33887r1obomwx5da08z057re',
# }
#

# DIDAR_CUSTOM_FIELD_LIST = {
#     "Field_8783_4_24": ['family_applied_in_canada'],
#     "Field_8783_1_29": ['job_offer', 'job_offer_desc'],
#     "Field_8783_1_32": ['reject_visa_in_canada', 'reject_visa_in_canada_desc'],
#     "Field_8783_1_28": ['work_experience_years', 'work_experience'],
#     "Field_8783_1_27": ['wife_work_experience'],
#     "Field_8783_0_30": ['total_budget', 'total_budget_desc'],
#     "Field_8783_0_34": ['services_you_want'],
#     "Field_8783_1_31": ['travel_to_country'],
#     "Field_996_0_1": ['wife_full_name'],
#     "Field_8783_4_33": ['how_know_us'],
#     "Field_8783_0_25": ['family_applied_in_canada_desc'],
# }

APPLICATION_URL = 'http://127.0.0.1:8080'

# DIDAR_FIRST_KARIZ_ID = "629be850-5388-41ec-a40b-15285f00eaa3"
# DIDAR_BIZDOMAINID = "0e1e59b3-0332-4e0c-8d6f-20e88129ac69"