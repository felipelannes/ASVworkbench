from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, RedirectView, TemplateView
from . import models


# Create your views here.

def weightsheet(request,report_area):
	template_name = 'report/{:s}/weightsheet.html'.format(report_area)
	context = {}
	return render(request, template_name, context)
