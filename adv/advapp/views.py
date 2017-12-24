from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,ListView,DetailView,
									CreateView,UpdateView,DeleteView)
from advapp import models

class indexTemplate(TemplateView):
	template_name= 'index.html'

class SchoolListViews(ListView):
	context_object_name = 'schools'
	model = models.school

class SchoolDetailViews(DetailView):
	context_object_name = 'school_detail'
	model= models.school
	template_name='advapp/school_details.html'

class SchoolCreateView(CreateView):
	fields= ('name','principle','location')
	model = models.school
	success_url = reverse_lazy("advapp:list")

class SchoolUpdateViews(UpdateView):
	fields = ('name','principle')
	model = models.school

class SchoolDeleteView(DeleteView):
	model= models.school
	success_url = reverse_lazy("advapp:list")

