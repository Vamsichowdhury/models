from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'music_app/index.html')


def other(request):
	return render(request,'music_app/other.html')


def relative(request):
	return render(request,'music_app/relative_url_template.html')
 