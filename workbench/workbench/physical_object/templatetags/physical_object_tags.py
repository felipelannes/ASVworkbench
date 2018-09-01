from django.template import Library

register = Library()

from workbench.physical_object.models import VESSEL

@register.simple_tag()
def get_all_vessels_tag():
	return VESSEL.objects.all()


@register.inclusion_tag('physical_object/templatetags/vessel_summary.html')
def build_vessel_summary(slug):
	vessel = VESSEL.objects.get(slug=slug)
	context = {
		'vessel':vessel
	}
	return context

