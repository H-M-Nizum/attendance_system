from django.shortcuts import render
from . import forms
from .import models 
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.urls import reverse_lazy
# for class base view login required
from django.utils.decorators import method_decorator
# Create your views here.


@method_decorator(login_required, name='dispatch')
class Addstudent(CreateView):
    model = models.StudentModel
    form_class = forms.StudentForm
    template_name = 'add_student.html'
    #  reverse_lazy work like redirect
    # print('bal')
    success_url = reverse_lazy('add_student')
    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)




# Create your views here.

def showstudent(request, class_slug = None):
    data = models.StudentModel.objects.all()
    if class_slug is not None:
        className = models.classModel.objects.get(slug = class_slug)
        data = models.StudentModel.objects.filter(className = className)
    
    classnames = models.classModel.objects.all()
    
    return render(request, 'showstudent.html', {'data': data, 'classname': classnames})
    