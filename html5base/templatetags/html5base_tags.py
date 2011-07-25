from django import template
from django.conf import settings
import re

register = template.Library()

"""
@register.inclusion_tag('includes/google_analytics.html', takes_context=True)
def google_analytics(context, ga_tracking_code):
	pass

@register.inclusion_tag('includes/google_webmaster.html', takes_context=True)
def google_webmaster(context, ga_webmaster_code):
	pass

@register.inclusion_tag('includes/yandex_metrics.html', takes_context=True)
def yandex_metrics(context, ya_tracking_code):
	pass

@register.inclusion_tag('includes/yandex_webmaster.html', takes_context=True)
def yandex_webmaster(context, ya_webmaster_code):
	pass
"""
