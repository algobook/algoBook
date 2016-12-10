from django import template
from ..models import Votes
from django.db.models import Sum
register = template.Library()

@register.filter
def count( code ):
	# print( (Votes.objects.filter(code=code).aggregate(Sum('vote'))).vote__sum);
	# total = Votes.objects.filter(code=code).aggregate(Sum('vote'))
	total = code.code_votes.aggregate(Sum('vote'))

	if total.get("vote__sum") != None:
		return total.get('vote__sum',"0");
	else:
		return '0'

@register.simple_tag(takes_context=True)
def isUp( context, code ):
	print( code.code_votes.filter( user=context['request'].user ) )
	# return code.code_votes.filter( user=context['request'].user )
