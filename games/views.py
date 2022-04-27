from django.shortcuts import render
from django.views import generic
from django.contrib.contenttypes.models import ContentType
from .models import * 



class TypeView(generic.ListView):
    model = Game_Type
    template_name = 'types_list_prop.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ListView(generic.ListView):
    model = Game
    template_name = 'games_list_prop.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context

class DetailView(generic.DetailView):
    template_name = 'details.html'
    model = Game
    slug_field = 'title'
