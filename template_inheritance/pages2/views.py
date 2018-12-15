
from django.views.generic import TemplateView
# Create your views here.
class Tollysongs(TemplateView):
    template_name='pages2/tollysongs.html'

class Bollysongs(TemplateView):
    template_name='pages2/bollysongs.html'

class Index(TemplateView):
    template_name='pages2/index.html'
