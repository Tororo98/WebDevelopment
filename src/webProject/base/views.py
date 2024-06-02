from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Tarea
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


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


# To create a new task from a view
class CrearTarea(CreateView):
    model = Tarea
    fields = '__all__'
    success_url = reverse_lazy('pendings')

# To edit a task from a view
class EditarTarea(UpdateView):
    model = Tarea
    fields = '__all__'
    success_url = reverse_lazy('pendings')

class EliminarTarea(DeleteView):
    model = Tarea
    context_object_name = 'tarea'
    success_url = reverse_lazy('pendings')
    template_name = 'base/tarea_confirm_delete.html'
