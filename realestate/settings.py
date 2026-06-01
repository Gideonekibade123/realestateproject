import os
from pathlib import Path
from dotenv import load_dotenv
from datetime import timedelta
from corsheaders.defaults import default_headers
import dj_database_url

# ------------------------------------------------
# Base Directory
# ------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

# ------------------------------------------------
# Environment Variables
# ------------------------------------------------
PAYSTACK_PUBLIC_KEY = os.getenv("PAYSTACK_PUBLIC_KEY", "")
PAYSTACK_SECRET_KEY = os.getenv("PAYSTACK_SECRET_KEY", "")

# ------------------------------------------------
# Security
# ------------------------------------------------

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = [
    "backendlastproject.onrender.com",
    ".onrender.com",
]

CSRF_TRUSTED_ORIGINS = [
    "https://backendlastproject.onrender.com",
    "https://estatehhub.netlify.app",  # ✅ correct URL
]

# ------------------------------------------------
# Installed Apps
# ------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Project apps
    'accounts.apps.AccountsConfig',
    'listings.apps.ListingsConfig',
    'payments',
    'enquiries',

    # Third-party
    'rest_framework',
    'corsheaders',
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
]

# ------------------------------------------------
# Django REST Framework
# ------------------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

# ------------------------------------------------
# JWT Settings
# ------------------------------------------------
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "AUTH_HEADER_TYPES": ("Bearer",),
}

# ------------------------------------------------
# Middleware
# ------------------------------------------------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# CORS Settings
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:5173",
#     "https://estatehhub.netlify.app",  # ✅ add this
# ]

FRONTEND_URL = "https://estatehhub.netlify.app"

CORS_ALLOWED_ORIGINS = [
    "https://estatehhub.netlify.app",
]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = list(default_headers) + [
    "authorization",
    "content-type",
]

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]
# URL Configuration

ROOT_URLCONF = 'realestate.urls'


# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI
WSGI_APPLICATION = 'realestate.wsgi.application'

# Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# import dj_database_url

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

AUTH_USER_MODEL = 'accounts.CustomUser'  # ✅ add here

# Password Validators
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
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True
USE_TZ = True

# Static Files
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Media Files (Images)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Email Configuration
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'gekibade@gmail.com'
# EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", "gekibade@gmail.com")
# FRONTEND_URL = os.getenv("FRONTEND_URL", "https://estatehhub.netlify.app")


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'gekibade@gmail.com'
# EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
# EMAIL_PORT = 465        # ✅ changed from 587 to 465
# EMAIL_USE_TLS = False   # ✅ changed to False
# EMAIL_USE_SSL = True    # ✅ add this
# DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", "gekibade@gmail.com")
# FRONTEND_URL = os.getenv("FRONTEND_URL", "https://estatehhub.netlify.app")


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'gekibade@gmail.com'
# EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
# EMAIL_PORT = 587        # ✅ change from 465 to 587
# EMAIL_USE_TLS = True    # ✅ change to True
# EMAIL_USE_SSL = False   # ✅ change to False
# DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", "gekibade@gmail.com")


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'gekibade@gmail.com'
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
DEFAULT_FROM_EMAIL = 'EstateHub <gekibade@gmail.com>'




RESEND_API_KEY = os.getenv("RESEND_API_KEY")  # ✅ add here


# Default Primary Key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

