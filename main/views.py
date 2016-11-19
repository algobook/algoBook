from django.shortcuts import render
from django.http import HttpResponse
import urllib 

from .models import Algo

# Create your views here.
def index(request):
	return render(request, 'main/index.html')

def show(request, algo_slug):
	return HttpResponse(" You Requested to open this algo " % algo_slug)

def search(request, query):
	query =query.replace("+", " ")
	algos = Algo.objects.filter(name__contains=query)
	return render(request, 'main/search.html', {'algos' : algos, 'query': query})


