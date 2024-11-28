
from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='index'),
  path('register', views.register, name='register'), 
  path('my-login', views.my_login, name='my-login'), 
]