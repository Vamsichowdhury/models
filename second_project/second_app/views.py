from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def songs(request):
	context={ 

	'data':"you are in views.py in second_app"
	}
	return render(request,'second_app/music_index.html',context)
