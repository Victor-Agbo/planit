from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_planit/', views.add_planit,),
    path('delete_planit/<int:planit_id>/', views.delete_planit),
    path('login/', views.login),
    path('log_in/', views.log_in, name='log_in'),
    #path('user_page/', views.user_page, name='user_page'),
    path(r'user_page/(.+)', views.user_page, name='user_page')
]
    

urlpatterns += staticfiles_urlpatterns()