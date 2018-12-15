from  django.contrib import admin
from django.urls import path
from second_app import views

urlpatterns=[

path('',views.songs,name="songs"),
path('admin/',admin.site.urls),
 ]

