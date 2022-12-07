from django.shortcuts import render
from django.http import HttpResponse
from .models import *           # to extract data from database/model // import Blog func from models
                                # we are extracting every data from models/database


# Create your views here.

        #   function home sends data from database/models to html page.
def home(request):
    post = Blog.objects.all()       # all objects data is stored in post variable
                                    # we are posting data from models/database to views

    return render(request, "base.html", {'post':post})      # sending data from post var to html page

       #    function demo sends data directly from views to html page.
def demo(request):

    post1 = Contacts.objects.all()

    return render(request, "demo.html",{'post1':post1})        # we should create different dictionary for different function
                        # to render html page. to send this data dynamically, DICTIONARY is used

