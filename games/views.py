from multiprocessing import context
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import * 


class Game_Type_View(generic.ListView):
    def index(request):
        game_type = Game_Type.objects.all()
        return HttpResponse(game_type)

class Game_Modes_View(generic.ListView):
    def index(request):
        game_mode = Game_Modes.objects.all()
        return HttpResponse(game_mode)

class Game_View(generic.TemplateView):
    template_name = "game_index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['games'] = Game.objects.all()
        return context


