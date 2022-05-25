from django.urls import path
from .views import *


app_name = 'games'

urlpatterns = [
    path('',game_form_view),
    path('types', TypeView.as_view(), name='type-list'),
    path('titles', ListView.as_view(), name='type-list'),
    path('<slug:slug>/', DetailView.as_view(), name='type-list'),
]

