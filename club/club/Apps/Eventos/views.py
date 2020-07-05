from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Eventos
# Create your views here.

class EventosLista(ListView):
    model = Eventos
    context_object_name = 'Eventos'
    template_name = 'Eventos/Lista_Eventos'

