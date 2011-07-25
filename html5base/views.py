from django.views.generic.simple import direct_to_template

def page_not_found(request):
	return direct_to_template(request, '404.html')
