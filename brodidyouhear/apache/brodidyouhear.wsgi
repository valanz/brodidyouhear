import os 
import sys

path = '/srv/www/brodidyouhear.com'
if path not in sys.path:
    sys.path.insert(0, '/srv/www/brodidyouhear.com')

os.environ['DJANGO_SETTINGS_MODULE'] = 'brodidyouhear.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
