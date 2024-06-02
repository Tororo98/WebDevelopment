from django.urls import path
from . import views
from .views import ListPendings, DetalleTarea, CrearTarea, EditarTarea

urlpatterns = [path('', ListPendings.as_view(), name='pendings'),
               path('tarea/<int:pk>', DetalleTarea.as_view(), name='tarea'),
               path('crear-tarea/', CrearTarea.as_view(), name='crear-tarea'),
               path('editar-tarea/<int:pk>', EditarTarea.as_view(), name='editar-tarea')]