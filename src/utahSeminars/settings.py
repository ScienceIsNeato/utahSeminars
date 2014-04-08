"""
Django settings for utahSeminars project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

if __name__ == '__main__':
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    import os
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    
    
    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/
    
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'v%dybhvao50f6gi$@m@u1&i8zm_)rwb^x+hb2rub2urivoeymw'
    
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True
    
    TEMPLATE_DEBUG = True
    
    ALLOWED_HOSTS = []
    
    
    # Application definition
    
    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'signups',
    )
    
    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )
    
    ROOT_URLCONF = 'utahSeminars.urls'
    
    WSGI_APPLICATION = 'utahSeminars.wsgi.application'
    
    
    # Database
    # https://docs.djangoproject.com/en/1.6/ref/settings/#databases
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    
    # Internationalization
    # https://docs.djangoproject.com/en/1.6/topics/i18n/
    
    LANGUAGE_CODE = 'en-us'
    
    TIME_ZONE = 'UTC'
    
    USE_I18N = True
    
    USE_L10N = True
    
    USE_TZ = True
    
    
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.6/howto/static-files/
    
    STATIC_URL = '/static/'
    
    # Template location
    TEMPLATE_DIRS = (
        os.path.join(os.path.dirname(BASE_DIR), "static", "templates"),
    )
    
    if DEBUG:
        MEDIA_URL = '/media/'
        STATIC_ROOT =  os.path.join(os.path.dirname(BASE_DIR), "static", "static-only")
        MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "media")
        STATICFILES_DIRS = (os.path.join(os.path.dirname(BASE_DIR), "static", "static"),)
        