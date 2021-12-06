from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import activity, activity_name
import datetime
from datetime import datetime, timedelta
from django.utils.timezone import utc
import pytz

from objectiva1.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
import socket
import  os
import smtplib

# socket .getaddrinfo('localhost',8080)
# HOST = "debep.net"
# REAL_HOST = HOST.replace("http://","").replace("https://","").split(":")[0]
# PORT = 8080
# server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# server.connect((REAL_HOST,PORT))
#
# print("REAL_HOST: ",REAL_HOST)
# print(server)


def home1(request):

    return render (request,'objectiva/home_index1.html')
def home2(request):
    activity1=activity.objects.all()
    user1=User.objects.all()
    return render(request,'objectiva/activity.html',{'activity1': activity1,'users':user1} )
def activity_frm1(request):
    if request.method == 'POST':
        activity1=activity()
        activity1.activityName = request.POST.get('activity_name')
        activity1.description = request.POST.get('description1')
        activity1.startingTime = request.POST.get('start_date')
        activity1.endingTime = request.POST.get('end_date')
        activity1.notificationMode = request.POST.get('notificationMode')
        activity1.save();
        request.user.Activity.add(activity1)
        # request.user.Activity.add(activity1.description)
        # request.user.Activity.add(activity1.notificationMode)
        return redirect('activity')
    return render(request,'objectiva/activity_form.html')


def done_a(request):
    complete=activity.complete
    return render(request,'objectiva/done_activity.html',{'complet':complete})
def not_d(request):

    return render (request,'objectiva/not_done.html')
def manage_p(request):

    return render(request,'objectiva/manage_page.html')
def about1(request):

    return render(request,'objectiva/about.html')
def contact1(request):

    return render(request,'objectiva/contact.html')
def reference1(request):

    return render(request,'objectiva/references.html')

def sign_up1(request):
    if request.method== 'POST':
        username = request.POST['userName']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User name already in use. ')
                return redirect('sign_up')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already used ')
                return redirect('sign_up')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save();
                return redirect('login_page')
        else:
            messages.info(request,'passwords not matched')
    else:
        return render(request, 'objectiva/sign_up.html')


def login1(request):
    if request.method=='POST':
        username=request.POST['userName']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None :
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
    else:
        return render(request, 'objectiva/login_page.html')
def logout1(request):
    auth.logout(request)

    return redirect('login_page')
def change_account(request):
    auth.logout(request)
    return redirect('sign_up')

def notify_user(request):

    if notify_time == datetime.datetime.now:
        activity.objects = True
        # subject = 'Activity notification'
        # message = 'The activity {% activity.activityName %} is about to begin'
        Emails = User.objects.filter(is_active=True).exclude(email='').values_list('email', flat=True)
        recipient = str(Emails)
        # send_mail(subject,message,EMAIL_HOST_USER,[recipient],fail_silently=False)

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.echlo()
            smtp.startls()
            smtp.echlo()

            # smtp.login( ' ', ' ')

            Email_subject = 'Activity notification'
            Email_body = 'The activity {% activity.activityName %} is about to begin'
            msg = f'subject:{Email_subject}\n\n{Email_body}'
            smtp.sendmail('shallileroi@gmail.com', recipient, msg)
        return render(request, 'objectiva/notify.html',
                      {'recipient': recipient})



