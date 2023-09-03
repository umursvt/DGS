from django.contrib import admin
from django.urls import path
from dersler import views

app_name="dersler"

urlpatterns = [
    path('temel-mantik/',views.temel_mantik,name="temel_mantik"),
    path('matematik/',views.matematik,name="matematik"),
    path('matematik/<str:video_id>/', views.matematik_detay, name='ders_detay'),
    path('geometri/',views.geometri,name="geometri"),
    path('hakkimizda',views.hakkimizda,name="hakkimizda"),
    path("iletisim/",views.iletisim,name="iletisim"),
    path('youtube-live/', views.youtube_live, name='youtube-live'),
    path('search/', views.dersler_search, name='dersler_search'),
    path('begenilen_videolar/', views.begenilen_videolar, name='begenilen_videolar'),
    
]
    

