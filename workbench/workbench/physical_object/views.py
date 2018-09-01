from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, RedirectView, TemplateView
from . import models
from .forms import VESSEL_Form
import os 
import json

 
# Create your views here.


# class HomeTemplateView(TemplateView):
# 	template_name = 'physical_object/home.html'
	
# 	def get_context_data(self, **kwargs):
# 		context = super(HomeTemplateView,self).get_context_data(**kwargs)
# 		return context

class VesselListView(ListView):
	template_name = 'physical_object/vessel_list.html'
	model = models.VESSEL


def vessel_add(request):
	if request.method == 'POST':
		form = VESSEL_Form(request.POST)
		if form.is_valid():
			vessel = form.save()
			return redirect("")
		else:
			pass
	else:
		form = VESSEL_Form()

	template_name = 'physical_object/vessel_add.html'
	context = {'form':form}
	return render(request,template_name,context)

class VesselDetailView(DetailView):
	template_name = 'physical_object/vessel_detail.html'
	slug_url_kwarg = 'slug'
	model = models.VESSEL

	def get_context_data(self,**kwargs):
		context = super(VesselDetailView,self).get_context_data(**kwargs)
		dirname = os.path.dirname(os.path.dirname(__file__)) + "//report//static//report//json//reports_list.json"
		with open(dirname, 'r') as datafile:
			reports_list = json.load(datafile)
		context['reports_list'] = sorted(reports_list,key= lambda report: report['name'])
		#context['reports_list'] = sorted([[report_area['name'],len(report_area['children']),report_area['slug']] for report_area in reports_list],key=lambda tupla: tupla[0])
		return context
