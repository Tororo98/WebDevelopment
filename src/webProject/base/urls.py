from django.urls import path
from . import views
from .views import ListPendings, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea, Logueo
from django.contrib.auth.views import LogoutView

urlpatterns = [path('', ListPendings.as_view(), name='pendings'),
               path('login/', Logueo.as_view(), name='login'),
               path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
               path('tarea/<int:pk>', DetalleTarea.as_view(), name='tarea'),
               path('crear-tarea/', CrearTarea.as_view(), name='crear-tarea'),
               path('editar-tarea/<int:pk>', EditarTarea.as_view(), name='editar-tarea'),
               path('eliminar-tarea/<int:pk>', EliminarTarea.as_view(), name='eliminar-tarea')]