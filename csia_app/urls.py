from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('myadmin/',adminloginview,name = 'adminloginpage'),
    path('adminauthenticate/', authenticateadmin),
    path('admin/homepage/',adminhomepageview,name = 'adminhomepage'),
    path('adminlogout/',logoutadmin),
    path('',homepageview, name = "homepage"),
    path('loginuser/', userloginview, name = "userlogin"),
    path('customer/authenticate/', userauthenticate, name = "userauthenticate"),
    path('user/homepage/', userhomepageview, name = 'userhomepage'),
    path('userlogout/', userlogout, name = "userlogout"),
    ]

