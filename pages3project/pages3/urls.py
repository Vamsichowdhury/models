
from django.urls import path,include
from .views import Home,Sem1,Sem2
app_name='pages3'
urlpatterns = [

    path("",Home.as_view(),name='home'),
    path("sem1/",Sem1.as_view(),name='sem1'),
    path("sem2/",Sem2.as_view(),name='sem2'),

]
