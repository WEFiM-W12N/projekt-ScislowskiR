from django.shortcuts import render
from django.views import generic
from django.contrib.contenttypes.models import ContentType
from .models import * 



class TypeView(generic.ListView):
    model = Game_Type
    paginate_by = 100  # Amount of shown objects
    template_name = 'types_list_prop.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class GameListView(generic.ListView):
    model = Game
    template_name = 'games_list_prop.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context

class Game_Type_ListView(generic.ListView):
    model = Game
    template_name = 'types_list_prop.html'
    context_object_name = 'games'

    def StockSummaryPage(request, type):
        game_data = Game.objects.filter(type=type)
        return render(request, 'types_list_prop.html', {'game_data': game_data})