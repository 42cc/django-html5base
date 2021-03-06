from django.conf.urls import patterns
from django.views.generic import TemplateView

urlpatterns = patterns('',
    (r'crossdomain.xml', TemplateView.as_view(template_name="html5base/crossdomain.xml")),
    (r'robots.txt', TemplateView.as_view(template_name="html5base/robots.txt")),
)
