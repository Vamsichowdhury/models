from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name='pages3/home.html'

class Sem1(TemplateView):
    template_name='pages3/sem1.html'

class Sem2(TemplateView):
    template_name='pages3/sem2.html'
