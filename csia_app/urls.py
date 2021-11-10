from django.contrib import admin
from django.urls import path
from .views import adminloginview, adminhomepageview, authenticateadmin,logoutadmin,homepageview,userloginview

urlpatterns = [
    path('admin/',adminloginview,name = 'adminloginpage'),
    path('adminauthenticate/', authenticateadmin),
    path('admin/homepage/',adminhomepageview,name = 'adminhomepage'),
    path('adminlogout/',logoutadmin),
    path('',homepageview, name = "homepage"),
    path('loginuser/', userloginview)
    ]

