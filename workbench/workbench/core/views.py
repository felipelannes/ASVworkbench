from django.shortcuts import render
from workbench.physical_object.models import VESSEL

# Create your views here.


def home(request):
	all_vessel = VESSEL.objects.all()
	#print (all_vessel)
	context={'all_vessel':all_vessel}
	return render(request, 'home.html' ,context)
