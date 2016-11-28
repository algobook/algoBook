from django.db import models

# Create your models here.
class Algo(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=500)
    lang = models.CharField(max_length=10)
    created_at = models.DateTimeField('created_at')
    updated_at = models.DateTimeField('updated_at')
    code = models.CharField(max_length=10000)
    slug = models.CharField(max_length=256)


from datetime import date
from django.core.urlresolvers import reverse
from django.forms import ModelForm

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

# User information
class User(models.Model):
	username = models.CharField(max_length = 30, primary_key = True, null = False, blank = False)
	first_name = models.CharField(max_length = 20, null = False, blank = False)
	last_name = models.CharField(max_length = 15, null = False, blank = False)
	password = models.CharField(max_length = 30, null = False, blank = False)
    # badges not integrated yet
	#badges = models.ForeignKey(Badges, on_delete = models.DO_NOTHING)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

# Question asked by user, may be here you are representing it by Algo
class Question(models.Model):
	asked_by = models.ForeignKey(User, on_delete = models.DO_NOTHING)
	title = models.CharField(max_length = 30, primary_key = True)
	description = models.TextField(max_length = 1000, null = False, blank = False)
	votes = models.IntegerField()
	tags = models.ManyToManyField(Tags)
	timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

# Answer given by user
class Answer(models.Model):
	answered_by = models.ForeignKey(User, on_delete = models.DO_NOTHING)
	question_is = models.ForeignKey(Question, on_delete = models.DO_NOTHING)
	description = models.TextField(max_length = 1000, null = False, blank = False)
	timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)
	accepted = models.BooleanField(default = False)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

# User form for template
class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'password']

# Question form for template
class QuestionForm(ModelForm):
	class Meta:
		model = Question
fields = ['title', 'description', 'tags']
