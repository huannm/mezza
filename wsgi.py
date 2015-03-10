from __future__ import unicode_literals

import os
import sys
sys.path.append('/home/huannm/site')
sys.path.append('/home/huannm/site/mezza')
os.environ.setdefault("PYTHON_EGG_CACHE", "/home/huannm/site/mezza/egg_cache")
#os.environ["LC_LANG"] = 'us_en.UTF-8'
#os.environ["LANG"] = 'us_en.UTF-8'
#os.environ["PYTHONIOENCODING"]='utf-8'

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
settings_module = "%s.settings" % PROJECT_ROOT.split(os.sep)[-1]
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mezza.settings")
#settings_module)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
