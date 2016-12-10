from django import template
from ..models import Votes
from django.db.models import Sum
import pprint
register = template.Library()

# TODO: Fix so much queries here...
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
	if not context['request'].user.is_authenticated():
		return '0'
	vote = Votes.objects.filter(code=code).filter( user=context['request'].user ).values("vote")
	if vote:
		if vote[0].get("vote") == 1:
			return '1'
		else:
			return '0'
	else:
		return '0'

@register.simple_tag(takes_context=True)
def isDown( context, code ):
	if not context['request'].user.is_authenticated():
		return '0'
	vote = Votes.objects.filter(code=code).filter( user=context['request'].user ).values("vote")
	if vote:
		if vote[0].get("vote") == -1:
			return '1'
		else:
			return '0'
	else:
		return '0'


