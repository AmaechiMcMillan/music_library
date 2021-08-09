SECRET_KEY = 'django-insecure-a^@ht9ukjvx4wfns8l!rw!+e^#^xgy)n6ju8si+d#cqm(1nsz-'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root',
        'PASSWORD': 'Indy#AIM012520',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}