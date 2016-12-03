from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaultfilters import slugify
import urllib

from .models import  ( 
	Algo, 
	Code, 
	Tags
)

from .forms import (
	UserForm,
	ProfileForm
	)

# Create your views here.
def index(request):
	return render(request, 'main/index.html')

def show(request, id):
    return render(request, "main/algo/view.html")

def search(request, query):
	query = query.replace("+", " ")
	algos = Algo.objects.filter(name__contains = query)
	return render(request, 'main/search.html', {'algos' : algos, 'query': query})


@login_required
def create_algo(request):
	user = request.user
	tags = []
	
	for tag in request.POST.get("name").split(""):
		t,created = Tags.objects.get_or_create(slug=slugify(tag))
		t.slug = slugify(tag)
		t.name = tag
		t.save()
		tags.append(t);


	lang = Tags.objects.get(slug=slugify(request.POST.lang))
	lang.isLang = 1;
	lang.save()

	algoname = request.POST.get("name")
	
	algo = Algo(
			name = algoname,
			slug = slugify(algoname),
			Tags = tags
		)

	algo.save();


@login_required
def add_code_to_algo(request):
	user = request.user
	algo = Algo.objects.get(pk=request.POST.get("algo_id"))
	lang = Tags.objects.filter(name=request.POST.get("lang")).filter(isLang=1);
	
	code = Code(
			user=user,
			algo=algo,
			code=request.POST.get("code"),
			upvotes=0,
			downvotes=0,
			lang=lang
		)
	code.save();


@login_required
@transaction.atomic
def update_profile(request):
	if request.method == 'POST':
		user_form = UserForm(request.POST, instance = request.user)
		profile_form = ProfileForm(request.POST, instance = request.user.profile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, _('Your profile was successfully updated!'))
			return redirect('settings:profile')
		else:
			messages.error(request, _('Please correct the error below.'))
	else:
		user_form = UserForm(instance = request.user)
		profile_form = ProfileForm(instance = request.user.profile)
	return render(request, 'auth/update_profile.html', {
		'user_form': user_form,
		'profile_form': profile_form
    })
