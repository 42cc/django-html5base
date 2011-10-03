from django.conf.urls.defaults import *

urlpatterns = patterns('django.views.generic.simple',
    (r'crossdomain.xml', 'direct_to_template', {'template': 'html5base/crossdomain.xml'}),
    (r'robots.txt', 'direct_to_template', {'template': 'html5base/robots.txt'}),
    (r'PIE.htc', 'direct_to_template', {'template': 'html5base/PIE.htc'}),
)
