from django.contrib import admin
from django.urls import path
from uyelik import views

app_name="uyelik"

urlpatterns = [
    path('register/',views.register,name="register"),
    path('login/',views.loginUser,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('profil',views.profil,name="profil")
    
    
]