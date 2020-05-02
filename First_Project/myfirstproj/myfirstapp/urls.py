from django.contrib import admin
from django.urls import path
from myfirstapp import views

app_name = 'myfirstapp'

urlpatterns = [
    path('', views.test , name="test"),
    path('contactus/', views.contactUs, name="Contact_Us"),
    path('signup/', views.signup, name="Sign_Up"),
    path('login/', views.user_login, name="User_Login"),
    path('special/', views.special, name="special"),
    path('logout/', views.user_logout, name="logout"),
]
