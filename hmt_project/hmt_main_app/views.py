from django.shortcuts import render
from hmt_main_app.models import *
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages

    
def home_page(request):
    try:
        homedata = HomePage.objects.all().values()[0]
        return render(request, 'index.html', {'homedata': homedata})
    except Exception as e:
        if len(HomePage.objects.all())==0:
            return HttpResponse("<h2>Don't have data in the database, please do migrations or check in the admin page</h2>")
        else:
            return HttpResponse('<h2> Error in Home page and here is the error '+ str(e) + '</h2>')

def contact_page(request):
    try:
        homedata = HomePage.objects.all().values()[0]
        if request.POST:
            try:
                subject = request.POST['name'] + " :: " + request.POST['subject'] + " :: " + request.POST['phone']
                message =  request.POST['message']
                from_email = request.POST['email']
                recipient_list = ['Email List']
                messages.success(request,f'Email has been successfully sent!')
                homedata.update({
                    'messages':messages
                })
                # send_mail(subject, message, from_email, recipient_list)
            except Exception as e:
                errorRaised = '<h2>'+' Error in sending email and here is the error '+ str(e) +'</h2>'
                return HttpResponse(errorRaised)
        return render(request,'contact.html',{'homedata': homedata})
    except Exception as e:
        return HttpResponse('<h2> Error in contact page and here is the error '+ str(e) + '</h2>')
    
def doctors_page(request):
    homedata = HomePage.objects.all().values()[0]
    return render(request,'doctors.html',{'homedata': homedata})

def services_page(request):
    homedata = HomePage.objects.all().values()[0]
    return render(request,'services.html',{'homedata': homedata})

def highlights_page(request):
    homedata = HomePage.objects.all().values()[0]
    return render(request,'highlights.html',{'homedata': homedata})

def appointments_page(request):
    homedata = HomePage.objects.all().values()[0]
    return render(request,'appointment.html',{'homedata': homedata})