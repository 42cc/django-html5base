from django import template
from html5base import settings
import re

register = template.Library()

@register.inclusion_tag('html5base/includes/google_analytics.html', takes_context=True)
def google_analytics(context):
    context.update({'id': settings.DEFAULT_SETTINGS.get('google_analytics_id'),\
                    'site': settings.DEFAULT_SETTINGS.get('google_analytics_site')})
    return context

@register.inclusion_tag('html5base/includes/google_webmaster.html', takes_context=True)
def google_webmaster(context):
    context.update({'id': settings.DEFAULT_SETTINGS.get('google_vrfy')})
    return context

@register.inclusion_tag('html5base/includes/alexa.html', takes_context=True)
def alexa(context):
    context.update({'id': settings.DEFAULT_SETTINGS.get('alexa_vrfy')})
    return context

@register.inclusion_tag('html5base/includes/yandex_metrics.html', takes_context=True)
def yandex_metrics(context):
    context.update({'id': settings.DEFAULT_SETTINGS.get('yandex_metrika_id')})
    return context

@register.inclusion_tag('html5base/includes/yandex_webmaster.html', takes_context=True)
def yandex_webmaster(context):
    context.update({'id': settings.DEFAULT_SETTINGS.get('yandex_vrfy')})
    return context
