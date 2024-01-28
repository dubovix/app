from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('create', views.create, name="create"),
    path('contacts', views.contacts, name="contacts"),
]
