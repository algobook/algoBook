from django.db import models
from datetime import date
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.
class Algo(models.Model):
	name = models.CharField(max_length = 256)
	description = models.CharField(max_length = 500, default="")
	created_at = models.DateTimeField('created_at', auto_now = True)
	updated_at = models.DateTimeField('updated_at', auto_now = True)
	slug = models.CharField(max_length = 256)
	tags = models.ManyToManyField('Tags')

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name
#TODO:
# Add fields for upvotes



# User will get badges
# TODO: Keep this for second stage
class Badges(models.Model):
	name = models.CharField(max_length = 30)
	description = models.TextField(max_length = 200, null = False, blank = False)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

# Question will have tags
class Tags(models.Model):
	name = models.CharField(max_length = 30)
	description = models.TextField(max_length = 100, null = False, blank = False)
	#tags are searchable
	slug = models.CharField(max_length = 30, unique = True, null = False)
	isLang = models.BooleanField(default=False)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name


class Profile(models.Model):
	user = models.OneToOneField(User, primary_key = True, on_delete = models.CASCADE)
	bio = models.TextField(max_length = 500, blank = True)
	location = models.CharField(max_length = 30, blank = True)
	birth_date = models.DateField(null = True, blank = True)
	badges = models.ForeignKey(Badges, null = True, blank = True, on_delete = models.DO_NOTHING)

	def __unicode__(self):
		return self.user.username

	def __str__(self):
		return self.user.username

class Code(models.Model):
	user = models.ForeignKey(User)
	algo = models.ForeignKey(Algo, on_delete = models.CASCADE)
	code = models.TextField(max_length = 20000, null = False)
	lang = models.ForeignKey(Tags)

	def __unicode__(self):
		return self.user.username

	def __str__(self):
		return self.user.username

class Votes(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	code = models.ManyToManyField(Code, related_name="code_votes")
	vote = models.IntegerField(default = 0)
	def __unicode__(self):
		return self.user.username

	def __str__(self):
		return self.user.username


# Example Query I want to generate
#Select from Algos with codes where tags in [Tags_Array];
#This is possible in Laravel as Algos::get()->withCodes()->tags()->wherein(tags_Array);
# Now our javascript will show algos with tag having language flag is true
#  results : [
#	{
#               #Algo Object
#		"title" : "Sometitle",
#		"..." : "..."
#		"codes" : [
#				{
#					"name": "sdsd",
#					"...": "..."
#					"tags" : [
#							{	"..." : "..."
#								"type" : "lang"
#							},
#							{
#								"..." : "..."
#								"type" : "default"
#							}
#						]
#				},
#				{ ... }
#			]
#	}
#}
#
#
