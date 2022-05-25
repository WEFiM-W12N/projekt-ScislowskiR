from django.shortcuts import render
from django.views import generic
from .models import * 



class TypeView(generic.ListView):
    model = Game_Type
    template_name = 'types_list_prop.html'
    def get_queryset(self):
        return Game_Type.objects.all()


class ListView(generic.ListView):
    model = Game
    template_name = 'games_list_prop.html'
    def get_queryset(self):
        return Game.objects.all()


class DetailView(generic.DetailView):
    model = Game
    template_name = 'details.html'
    slug_field = 'shortcut'
    def list(request, title):
         modes = Game.objects.get(title=title)
         context = {
             'modes': modes
         }
         return render(request, 'details.html', context)