
from django.db.models import F
from django.shortcuts import render
from django.views import generic

from .models import * 



class TypeView(generic.ListView):
    model = Game_Type
    paginate_by = 100  # Amount of shown objects
    template_name = 'game_type_index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class GameListView(generic.ListView):
    model = Game
    paginate_by = 100  # Amount of shown objects
    template_name = 'game_list_index.html'
    context_object_name = 'games_list'
    def get_queryset(self):
        return Game.objects.filter(title=self.kwargs['title']).order_by('title')