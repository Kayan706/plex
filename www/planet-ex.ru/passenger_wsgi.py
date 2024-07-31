import os, sys
sys.path.insert(0, '/var/www/u2582988/data/www/planet-ex.ru/ex')
sys.path.insert(1, '/var/www/u2582988/data/djangoenv/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'ex.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()