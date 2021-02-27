from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth, messages

from . import models

# Create your views here.

 
def home(request):
    planit_items = models.User.planit.objects.all().order_by("-added_date")
    return render(request, 'main/index.html', {"planit_items" : planit_items})

@csrf_exempt
def add_planit(request):
    added_date = timezone.now()
    content = request.POST["content"]
    created_obj = models.User.planit.objects.create(added_date=added_date, text=content)
    print(created_obj)
    print(created_obj.id)
    length_of_planits=models.planit.objects.all().count()
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
    next = request.GET.get("next")
    user = auth.authenticate(username=login_username, password=login_password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        print('loggedin')
        return HttpResponseRedirect('/user_page')
    else:
        print('not loggedin')
        # Show an error page
        error = 'Invalid login'
        return render(request, "main/login.html", {'error':error})

def user_page(request, login_username2):
    login_username2 = request.POST.get('login_username2')
    print(login_username)
    #return render(request, login_username+'.html')
    return HttpResponseRedirect("/")
