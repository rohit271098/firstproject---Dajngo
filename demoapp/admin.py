from django.contrib import admin
from .models import *                   # we import models from the folder

# Register your models here.

admin.site.register(Blog)                   # register models
admin.site.register(Contacts)

# first run -- python manage.py makemigrations
# then run -- python manage.py migrate

# then run server.

# this helps to migrate models tables.

