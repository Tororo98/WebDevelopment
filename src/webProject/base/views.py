from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Tarea

# Create your views here.
class ListPendings(ListView):
    model = Tarea
    context_object_name = 'tareas'

class DetalleTarea(DetailView):
    model = Tarea
    # To give the html object a custom name and avoid using 'object' default calling
    context_object_name = 'tarea'
    # To give the template a custom name and avoid dependency on default name
    template_name = 'base/tarea.html'
