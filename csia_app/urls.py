from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

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
    path('usertasks/<int:subject_id>', usertasksview, name = "usertasks"),
    path('savetasks/<int:task_id>', savetask),
    path('createtask/',createtask, name= "createtask"),
    path('admintasks/<int:subject_id>', admintasksview, name = "admintasks"),
    path('updategrade/',updategrade,name= "updategrade"),
    path('updatetask/',updatetask, name="updatetask"),
    path('deletetask/<int:task_id>', deletetask, name= "deletetask")
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

