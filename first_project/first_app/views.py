from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
	context={ 

	'data':'you can find songs here'
	}
	return render(request,'first_app/index.html',context)