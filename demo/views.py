from django.shortcuts import render

#from django.http import HttpResponse

#from .models import Question

def demo(request):
    return render(request, 'demo/index.html')

def home(request):
	return render(request, 'demo/home.html')

def contacts(request):
	return render(request, 'demo/contacts.html')