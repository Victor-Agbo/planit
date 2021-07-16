from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth, messages
import datetime
from . import models

# Create your views here.
 
def home(request):
    if request.user.is_authenticated == True:
        return HttpResponseRedirect("/user_page")
    
    else: 
        return render(request, 'main/index.html') 

    
@csrf_exempt
def add_planit(request):
    current_user = request.user
    creator = models.planner.objects.get(account=current_user)
    content = request.POST["content"]
    print(str(datetime.datetime.now())[10])
    time = str(datetime.datetime.now())
    time=time[0:10]+'_'+time[11:]
    creator.data = creator.data+time+'ʭ'+content+'ʬ'
    print(content)
    creator.save()
    return HttpResponseRedirect("/user_page")

@csrf_exempt
def delete_planit(request):
    time = request.POST["time"]
    current_user = request.user
    creator = models.planner.objects.get(account=current_user)
    creator.data = creator.data
    a=creator.data[creator.data.index(time):]
    b=creator.data.index(a)
    c=a.index('ʬ')
    d=b+c+1
    e = creator.data[b:d]
    creator.data = creator.data.replace(e, '')
    print(creator.data)
    creator.save()


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
        print('loggedin')
        return HttpResponseRedirect('/user_page')
    else:
        print('not loggedin')
        message = 'You are not Logged in'
        stuff ={'message':message}
        # Show an error page
        return render(request, "main/login.html", stuff)

def signup(request):
    return render(request, 'main/signup.html')

@csrf_exempt
def sign_up(request):
    pass
    
def user_page(request):
    planit_items = models.planner.objects.get(account=request.user).data
    planit_items = planit_items.split('ʬ')
    planit_items.pop()
    planit_items.reverse()

    shown_items = []

    for planit_item in planit_items:
        main_items = planit_item.split('ʭ')
        shown_items.append(main_items)
    

    if request.user.is_authenticated:
        print(request.user)
    user = str(request.user)
    userpage = 'Users/'+user+'.html'

    return render(request, userpage, {"planit_items" : shown_items})
