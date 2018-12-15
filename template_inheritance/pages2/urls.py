from django.urls import path,include
from .views import Tollysongs,Bollysongs,Index
app_name='pages2'

urlpatterns = [
    path('tollysongs/',Tollysongs.as_view(),name='tollysongs' ),
    path('bollysongs/',Bollysongs.as_view(),name='bollysongs'),
    path('',Index.as_view(),name='index'),

]
