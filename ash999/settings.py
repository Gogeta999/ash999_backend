from pathlib import Path
import  os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#TODO Change Your SECRET_KEY. SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-py$39if+#a&(fa9&247132o2p6fxgy#*2b(a%tr^%q*e)3u=1u'

#TODO Change To False If you deploy SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#TODO Add your server ip before you deploy or vim edite this settings after you push in server/ Mine Is '188.166.234.99','2400:6180:0:d0::111c:e001'
ALLOWED_HOSTS = ['188.166.234.99','2400:6180:0:d0::111c:e001','127.0.0.1','localhost','[::1]']


# Application definition
#coreheaders for Apollo
INSTALLED_APPS = [
    'account',
    'blog',
    'corsheaders',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'graphene_django',
]

GRAPHENE = {
    'SCHEMA': 'blog.schema.schema' # Where your Graphene schema lives
}


#From md editor
X_FRAME_OPTIONS = 'SAMEORIGIN' 

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = (
#     'http://localhost:3000',
# )


ROOT_URLCONF = 'ash999.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'ash999.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
if not DEBUG:
# For Deployment
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'yourProject',
            'USER': 'yourUserName',
            'PASSWORD': 'yourPassword',
            'HOST': 'localhost',
            'PORT': '',
        }
    }

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

#Define Your Auth Model
AUTH_USER_MODEL = 'account.User'

STATIC_URL = '/static/'
# Add Below If You Need
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/'),]
if not DEBUG: 
    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Just want BigAutoField
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#Just prefer below Time Formats
TIME_FORMAT = '%d-%m-%Y %H:%M:%S'
DATE_TIME_FORMAT = '%d-%m-%Y'