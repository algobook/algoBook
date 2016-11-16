from django.shortcuts import render
from django.http import HttpResponse

from .models import Algo

# Create your views here.
def index(request):
	return render(request, 'main/index.html')

def show(request, algo_slug):
	algo = Algo.objects.filter(slug__contains=algo_slug)
	return HttpResponse(" You Requested to open this algo " % algo_slug)

def search(request):
	return render(request, 'main/search.html')