from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth, messages
import datetime as dt
import pytz
import simplejson as json
from . import models


# Create your views here.

def home(request):
    if request.user.is_authenticated is True:
        return HttpResponseRedirect("/user_page")

    else:
        return render(request, 'main/index.html')


@csrf_exempt
def add_planit(request):
    content = request.POST["content"]
    timezone = pytz.timezone('Africa/Lagos')
    read_file = open('db.json')
    read_json = json.load(read_file)
    read_json[str(request.user)]['main'][str(dt.datetime.now(timezone))] = content
    print(read_json['victor'], type(read_json))

    with open('db.json', 'w') as write_file:
        json.dump(read_json, write_file)
    return HttpResponseRedirect("/user_page")


@csrf_exempt
def delete_planit(request):
    time = request.POST["time"]
    read_file = open('db.json')
    read_json = json.load(read_file)
    user_data = read_json[str(request.user)]['main']
    user_data.pop(time)

    with open('db.json', 'w') as write_file:
        json.dump(read_json, write_file)


    return HttpResponseRedirect("/user_page")


@csrf_exempt
def login(request):
    return render(request, "main/login.html")


@csrf_exempt
def log_in(request):
    login_username = request.POST.get("login_username")
    login_password = request.POST.get("login_password")

    user = auth.authenticate(username=login_username, password=login_password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        print('logged in')
        return HttpResponseRedirect('/user_page')
    else:
        print('not logged in')
        message = 'You are not Logged in'
        stuff = {'message': message}
        # Show an error page
        return render(request, "main/login.html", stuff)


def signup(request):
    return render(request, 'main/signup.html')


@csrf_exempt
def sign_up(request):
    signup_username = request.POST.get("signup_username")
    print(signup_username)
    return HttpResponseRedirect('/signup')


def user_page(request):
    if request.user.is_authenticated is True:
        shown_items = []
        read_file = open('db.json')
        read_json = json.load(read_file)
        user_data = read_json[str(request.user)]['main']
        b = read_json[str(request.user)]['main'].values()

        for key in user_data:
            shown_items.append([key, user_data.get(key)])

        shown_items.reverse()
        print(shown_items)

        return render(request, 'Users/user_page.html', {"planit_items": shown_items})

    else:
        message = 'You are logged out you need to log in to continue'
        stuff = {'message': message}
        return render(request, "main/login.html", stuff)

