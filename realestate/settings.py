import os
from pathlib import Path
from dotenv import load_dotenv
from datetime import timedelta
from corsheaders.defaults import default_headers

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
SECRET_KEY = 'django-insecure-6njj80&q2@=vux7e_rn#2&4ms(all8s_%b4^9y=s!@8#4m5mv!'

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
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "https://estatehhub.netlify.app",  # ✅ add this
]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = list(default_headers) + [
    "authorization",
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
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'gekibade@gmail.com'
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Default Primary Key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

