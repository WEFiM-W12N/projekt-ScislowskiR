from django.urls import path
from .views import *


app_name = 'mlmodele'

urlpatterns = [
    path('', model_form_view),
    path('processing', ProcessingView.as_view(), name='type-list'),
    path('processing', ProcessingView.as_view(), name='type-list'),
    path('processing', ProcessingView.as_view(), name='type-list'),
    path('processing', ProcessingView.as_view(), name='type-list'),
    path('processing', ProcessingView.as_view(), name='type-list'),
    path('titles', ListView.as_view(), name='type-list'),
    path('<slug:slug>/', DetailView.as_view(), name='type-list'),
]

