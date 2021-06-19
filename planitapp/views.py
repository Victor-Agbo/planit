from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth, messages
import datetime

from . import models

# Create your views here.

 
def home(request):
    if request.user.is_authenticated == True:
        print('True')
    
    else: 
        print('False')

    return render(request, 'main/index.html') 
    
@csrf_exempt
def add_planit(request):
    current_user = request.user
    creator = models.planner.objects.get(account=current_user)
    print(type(creator.data))
    content = request.POST["content"]
    creator.data = creator.data+'║'+content
    creator.time = creator.time+'║'+datetime.datetime.now()
    print(creator.data)
    creator.save()
    print(creator.time)
    return HttpResponseRedirect("/user_page")

@csrf_exempt
def delete_planit(request, planit_id):
    models.planit.objects.get(id=planit_id).delete()
    return HttpResponseRedirect("/user_page")

@csrf_exempt 
def login(request):
    return render(request, "main/login.html")

@csrf_exempt
def log_in(request):
    login_username = request.POST.get("login_username")
    login_password = request.POST.get('login_password')

    user = auth.authenticate(username=login_username, password=login_password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        print('loggedin')
        return HttpResponseRedirect('/user_page')
    else:
        print('not loggedin')
        message = 'You are not Logged in'
        stuff ={'message':message}
        # Show an error page
        return render(request, "main/login.html", stuff)
#, {"planit_items" : planit_items}
def signup(request):
    return render('main/login.html')
def user_page(request):
    #planit_items = models.User.planit.objects.all().order_by("-added_date")

    if request.user.is_authenticated:
        print(request.user)
    user = str(request.user)
    userpage = 'Users/'+user+'.html'
    return render(request, userpage)
    #, {"planit_items" : planit_items}
