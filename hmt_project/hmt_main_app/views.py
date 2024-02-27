from django.shortcuts import render
from hmt_main_app.models import *
from django.http import HttpResponse

def home_page(request):
    try:
        obj = HomePage.objects.all().values()[0]
        return render(request, 'index.html', {'obj': obj})
    except:
        if len(HomePage.objects.all())==0:
            return HttpResponse("<h1>Don't have data in the database, please do migrations or check in the admin page</h1>")

def contact_page(request):
    return render(request,'contact.html')