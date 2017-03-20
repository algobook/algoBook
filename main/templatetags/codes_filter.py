from django import template
from ..models import Votes
from django.db.models import Sum
import pprint
register = template.Library()

@register.simple_tag(takes_context=True)
def showDelete( context, code ):
	if not context['request'].user.is_authenticated():
		return 0

	if context['request'].user == code.user:
		return 1
	else:
		return 0

@register.filter
def noDefault( lang ):
	if lang == "default":
		return ""
	return lang


