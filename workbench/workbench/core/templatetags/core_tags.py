from django.template import Library

register = Library()

@register.inclusion_tag('core/templatetags/page_header.html')
def build_page_header(title,headline):
	context = {
		'title':title,
		'headline':headline
	}
	return context
