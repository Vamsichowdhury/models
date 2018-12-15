
from django.urls import path,include
from .views import HomePageView,AboutPageView

app_name='pages'
urlpatterns = [
    path('home/',HomePageView.as_view(),name='home'),
    path('about/',AboutPageView.as_view(),name='about')

]
