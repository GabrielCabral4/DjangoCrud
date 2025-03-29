from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from .forms import TarefaForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required  
import json

@login_required
def listar_tarefas(request):
    tarefas = Tarefa.objects.filter(owner=request.user).order_by('-pinned', 'order')
    return render(request, 'tarefas/lista.html', {'tarefas': tarefas})

@login_required
def criar_tarefas(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.owner = request.user
            tarefa.save()
            return redirect('listar_tarefas')
    else:
        form = TarefaForm()
    return render(request, 'tarefas/formulario.html', {'form': form})

@login_required
def editar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, owner=request.user)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('listar_tarefas')
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'tarefas/formulario.html', {'form': form})

@login_required
def deletar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, owner=request.user)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('listar_tarefas')
    return render(request, 'tarefas/confirmar_delecao.html', {'tarefa': tarefa})

@login_required
def fixar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, owner=request.user)
    tarefa.pinned = not tarefa.pinned
    tarefa.save()
    return redirect('listar_tarefas')

@login_required
@require_POST
def atualizar_ordem_tabela(request):
    data = json.loads(request.body)
    ordem_ids = data.get('ordem', [])
    for index, tarefa_id in enumerate(ordem_ids):
        tarefa = get_object_or_404(Tarefa, id=tarefa_id, owner=request.user)
        tarefa.order = index
        tarefa.save()

    return JsonResponse({'status': 'ok'})
