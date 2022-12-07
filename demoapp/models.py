from django.db import models
from datetime import datetime

# Create your models here.              first python manage.py migrate is to be run before creating superuser.

# Username : rohit
# password : 1431104584ssc
# gmail : rohitgajula27@gmail.com

class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")           # images folder is created automatically in media folder
    description  = models.TextField()
    author = models.CharField(max_length=100)
    created_on = models.DateTimeField(default=datetime.now)

    def __str__(self):                          # used to build tables
        return self.title                       # here title is shown as main table label

class Contacts(models.Model):
    name = models.CharField(max_length=20)
    number = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name

