
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
	path("first_app/",views.index,name="index"),
	path('songs/',views.index,name="index"),
]
