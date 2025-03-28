from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_tarefas, name='listar_tarefas'),
    path('fixar/<int:id>/', views.fixar_tarefa, name='fixar_tarefa'),
    path('atualizar_ordem/', views.atualizar_ordem_tabela, name='atualizar_ordem_tarefas'),
    path('nova/', views.criar_tarefas, name='criar_tarefa'),
    path('editar/<int:id>/', views.editar_tarefa, name='editar_tarefa'),
    path('deletar/<int:id>/', views.deletar_tarefa, name='deletar_tarefa'),
]