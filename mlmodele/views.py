from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from .models import * 
from .forms import ModelForm


class ProcessingView(generic.ListView):
    model = Processing
    template_name = 'model_processing.html'
    def get_queryset(self):
        return Public.objects.all()


class DeepLearningView(generic.ListView):
    model = Deep_Learning
    template_name = 'model_deep_learning.html'
    def get_queryset(self):
        return Public.objects.all()


class OperationsView(generic.ListView):
    model = Operations
    template_name = 'model_operations.html'
    def get_queryset(self):
        return Public.objects.all()


class PublicView(generic.ListView):
    model = Public
    template_name = 'model_public.html'
    def get_queryset(self):
        return Public.objects.all()


class CustomView(generic.ListView):
    model = Custom
    template_name = 'model_custom.html'
    def get_queryset(self):
        return Public.objects.all()


class ListView(generic.ListView):
    model = Model
    template_name = 'model_deep_learning.html'
    def get_queryset(self):
        return Model.objects.all()


class DetailView(generic.DetailView):
    model = Model
    template_name = 'details.html'
    slug_field = 'shortcut'
    def list(request, title):
         modes = Model.objects.get(title=title)
         context = {
             'modes': modes
         }
         return render(request, 'details.html', context)


def model_form_view(request):
    form = ModelForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "summarise.html", context)