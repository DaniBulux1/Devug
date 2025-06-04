from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tutoriales, name='lista_tutoriales'),
    path('tutorial/<int:pk>/', views.detalle_tutorial, name='detalle_tutorial'),
    path('publicar/', views.crear_tutorial, name='crear_tutorial'),
]