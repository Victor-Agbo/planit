from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView
from django.conf.urls import url


from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user_page/add_planit/', views.add_planit,),
    path('user_page/delete_planit/', views.delete_planit),
    path('login/', views.login),
    path('log_in/', views.log_in, name='log_in'),
    path('signup/', views.signup),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('user_page/', views.user_page, name='user_page'),
    path('favicon.ico', RedirectView.as_view(url='/static/images/favicon.ico')),
]
    

urlpatterns += staticfiles_urlpatterns()

