
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar_marca/', views.cadastrar_marca, name='cadastrar_marca'),
    path('listar_marca/', views.listar_marca, name='listar_marca'),
    path('editar_marca/<int:pk>', views.editar_marca, name='editar_marca'),
    path('remover_marca/<int:pk>', views.remover_marca, name='remover_marca')
]