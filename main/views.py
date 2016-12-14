from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.template.defaultfilters import slugify
import urllib

from .models import  (
	Algo,
	Code,
	Tags,
	Votes
)

from .forms import (
	UserForm,
	ProfileForm
	)

# Create your views here.
def index(request):
	return render(request, 'main/index.html')

def show(request, slug):

	algo = Algo.objects.get(slug=slugify(slug))
	codes = Code.objects.filter(algo=algo)

	# TODO: Add a check if algo is not created before
	lang = request.GET.get("lang", "default")
	data = {
		'algo' 	: algo,
		'lang' 	: lang,
		'codes' : codes
	}
	return render(request, "main/algo/view.html", data)

def gen_search_query(request,q):
	if request.GET.get("lang"):
		return q + " in " + request.GET.get("lang")
	else:
		return q;

def search(request, query):
	query = " ".join( list(query.split("+")))
	algos = Algo.objects.filter(name__icontains = query)
	contributors = {}
	for algo in algos:
		users = list ( set( code.user.username for code in Code.objects.filter(algo=algo) ) )
		users = ", ".join(users)
		contributors[algo.id] = users
	return render(request, 'main/search.html', 
				{ 
					'algos' : algos,
					'query': gen_search_query(request, query), 
					'contributors': contributors
				}
			)

def api_search(request,query):
	query = " ".join( list(query.split("+")))
	algos = Algo.objects.filter(name__icontains = query)

	if not len(algos):
		return HttpResponseNotFound("Not Found")

	contributors = {}
	data = {}
	for algo in list(algos):
		users = list ( set( code.user.username for code in Code.objects.filter(algo=algo)))
		users = ", ".join(users)
		data[algo.id] = {
				'id' : algo.id,
				'name' : algo.name,
				'description' : algo.description,
				'slug': algo.slug,
				'contribs' : users
			}
	
	results = { 'algos' : data}

	return JsonResponse({ 'results': results })

	# TODO: tag system in second stage
	# for tag in query.split("+"):
		# tags.append( uglify() )


@login_required
def create_algo(request):
	user = request.user

	# TODO : tags in second stage
	# tags = []

	# for tag in request.POST.get("name").split():
	# 	t,created = Tags.objects.get_or_create(slug=slugify(tag))
	# 	t.slug = slugify(tag)
	# 	t.name = tag
	# 	t.save()
	# 	tags.append(t);
	#
	if not request.GET.get("name"):
		return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

	langOpted = request.GET.get("lang", "default")

	lang, created = Tags.objects.get_or_create( slug=slugify( langOpted ) )
	lang.name = langOpted
	lang.save()

	algoname = request.GET.get("name")

	algo,created = Algo.objects.get_or_create( slug = slugify( algoname ) )
	algo.name = algoname

	algo.save();

	return HttpResponseRedirect("/algo/" + algo.slug + "?lang=" + langOpted)


@login_required
def add_code_to_algo(request):

	print(request.POST.get("lang"))
	user = request.user
	algo = Algo.objects.get(pk=request.POST.get("algo_id"))
	lang = Tags.objects.get(slug=slugify(request.POST.get("lang")));

	code = Code(
			user=user,
			algo=algo,
			code=request.POST.get("code"),
			lang=lang
		)
	code.save();
	return HttpResponseRedirect("/algo/" + algo.slug + "?lang=" + lang.name)

@login_required
def add_description_to_algo(request):

	algo_id = request.GET.get("algo_id")
	desc = request.GET.get("desc")

	algo = Algo.objects.get( pk=algo_id )
	algo.description = desc
	algo.save()

	return JsonResponse({ 'response' : 1})

@login_required
def add_vote_to_code(request, code_id):

	code = Code.objects.get(pk=code_id)
	user = request.user
	vote = request.GET.get("add")

	check = Votes.objects.filter(user=user).filter(code=code)

	if not check:
		v = Votes(user=user, code=code, vote=vote)
		v.save()
	else:
		check = check[0]
		if int(check.vote) == int(vote):
			check.delete()
		else:
			check.vote = vote
			check.save()
	return HttpResponseRedirect( request.META.get('HTTP_REFERER') )

@login_required
def delete_code( request, code_id ):

	code = Code.objects.get(pk=code_id)
	
	if code.user == request.user:
		code.delete()

	return HttpResponseRedirect( request.META.get('HTTP_REFERER') )

@login_required
def user_profile(request, name):
	return render(request, 'main/user_profile.html')

#TODO: To be implemented later
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
