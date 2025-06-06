from django.urls import path
from . import views

urlpatterns = [
    # Rutas principales
    path('', views.lista_tutoriales, name='lista_tutoriales'),
    path('tutorial/<int:pk>/', views.detalle_tutorial, name='detalle_tutorial'),
    path('publicar/', views.crear_tutorial, name='crear_tutorial'),
    path('editar/<int:pk>/', views.editar_tutorial, name='editar_tutorial'),
    
    # APIs para reacciones
    path('api/reaccion/', views.agregar_reaccion, name='agregar_reaccion'),
    path('api/reacciones/<int:tutorial_id>/', views.obtener_reacciones, name='obtener_reacciones'),
]