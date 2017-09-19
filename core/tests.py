import os
import django
from django.test import TestCase
# Django specific settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

### Have to do this for it to work in 1.9.x!
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
#############

# Your application specific imports
from core.models import *

#Add user
# user = Restaurant(name="someone", email="someone@example.com")
# user.save()

# Application logic
first_restaurant = Restaurant.objects.all()[0]
print first_restaurant

