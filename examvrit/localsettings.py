DEBUG = True

# database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myprojectdb',
        'USER': 'examvrit',
        'PASSWORD': 'Kritagya1234@',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Secret Key
SECRET_KEY = 'django-insecure-zp-9adc7793@!y0zcxom1j5l-28n+&amak4vb)r=)+=sw%=4y1'