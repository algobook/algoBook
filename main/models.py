from django.db import models
from datetime import date
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.
class Algo(models.Model):
	name = models.CharField(max_length = 256)
	description = models.CharField(max_length = 500)
	lang = models.CharField(max_length = 10)
	created_at = models.DateTimeField('created_at', auto_now = True)
	updated_at = models.DateTimeField('updated_at', auto_now = True)
	code = models.CharField(max_length = 10000)
	slug = models.CharField(max_length = 256)
	tags = models.ManyToManyField('Tags')

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name
#TODO:
# Add fields for upvotes



# User will get badges
class Badges(models.Model):
	name = models.CharField(max_length = 30)
	description = models.TextField(max_length = 200, null = False, blank = False)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

# Question will have tags
class Tags(models.Model):
	name = models.CharField(max_length = 30, primary_key = True)
	description = models.TextField(max_length = 100, null = False, blank = False)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name


class MyUser(User):
	badges = models.ForeignKey(Badges, on_delete = models.DO_NOTHING)

	def __unicode__(self):
		return self.username
	
	def __str__(self):
		return self.username
