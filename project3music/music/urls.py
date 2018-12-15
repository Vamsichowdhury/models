from django.urls import path
from music import views

#TEMPLATE TAGGING

app_name='music'

urlpatterns=[

path('relative',views.relative,name='relative'),
path('other',views.other,name='other'),
path('',views.index,name='index')

] 