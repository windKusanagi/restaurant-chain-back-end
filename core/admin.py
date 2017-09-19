from django.contrib import admin
from .models import *

# register models to manipulate data in admin page
admin.site.register(Restaurant)
admin.site.register(Employee)
admin.site.register(Recipe)