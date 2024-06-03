from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Tarea
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Login view
class Logueo(LoginView):
    template_name = "base/login.html"
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('pendings')


# Create your views here.
class ListPendings(LoginRequiredMixin, ListView):
    model = Tarea
    context_object_name = 'tareas'


class DetalleTarea(LoginRequiredMixin, DetailView):
    model = Tarea
    # To give the html object a custom name and avoid using 'object' default calling
    context_object_name = 'tarea'
    # To give the template a custom name and avoid dependency on default name
    template_name = 'base/tarea.html'


# To create a new task from a view
class CrearTarea(LoginRequiredMixin, CreateView):
    model = Tarea
    fields = '__all__'
    success_url = reverse_lazy('pendings')


# To edit a task from a view
class EditarTarea(LoginRequiredMixin, UpdateView):
    model = Tarea
    fields = '__all__'
    success_url = reverse_lazy('pendings')


class EliminarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    context_object_name = 'tarea'
    success_url = reverse_lazy('pendings')
    template_name = 'base/tarea_confirm_delete.html'
