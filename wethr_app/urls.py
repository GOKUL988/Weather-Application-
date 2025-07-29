from django.urls import path 
from .import views 
urlpatterns= [
    path("", views.home, name="home.html") ,
    path("main/<search_city>", views.main, name="main.html")
]