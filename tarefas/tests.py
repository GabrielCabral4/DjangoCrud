from django.test import TestCase
from django.urls import reverse
from .models import Tarefa
from .forms import TarefaForm

class TarefaModelTest(TestCase):
    def test_criacao_tarefa(self):
        tarefa = Tarefa.objects.create(
            titulo='Teste de Tarefa',
            descricao='Descrição de teste',
            concluida=False
        )
        
        self.assertEqual(tarefa.titulo, 'Teste de Tarefa')
        self.assertEqual(tarefa.descricao, 'Descrição de teste')
        self.assertFalse(tarefa.concluida)
        self.assertIsNotNone(tarefa.data_criacao)

    def test_str_representacao(self):
        tarefa = Tarefa.objects.create(titulo='Tarefa Teste')
        self.assertEqual(str(tarefa), 'Tarefa Teste')

class TarefaFormTest(TestCase):
    def test_form_valido(self):
        form_data = {
            'titulo': 'Nova Tarefa',
            'descricao': 'Descrição da nova tarefa',
            'concluida': True
        }
        form = TarefaForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalido(self):
        form_data = {
            'titulo': '',
            'descricao': 'Descrição da tarefa'
        }
        form = TarefaForm(data=form_data)
        self.assertFalse(form.is_valid())

class TarefaViewsTest(TestCase):
    def setUp(self):
        self.tarefa1 = Tarefa.objects.create(
            titulo='Tarefa 1', 
            descricao='Descrição 1',
            concluida=False
        )
        self.tarefa2 = Tarefa.objects.create(
            titulo='Tarefa 2', 
            descricao='Descrição 2',
            concluida=True
        )

    def test_listar_tarefas(self):
        response = self.client.get(reverse('listar_tarefas'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Tarefa 1')
        self.assertContains(response, 'Tarefa 2')
        self.assertEqual(len(response.context['tarefas']), 2)

    def test_criar_tarefa(self):
        response = self.client.post(reverse('criar_tarefa'), {
            'titulo': 'Nova Tarefa',
            'descricao': 'Descrição da nova tarefa',
            'concluida': True
        })
        
        self.assertRedirects(response, reverse('listar_tarefas'))
        
        self.assertTrue(Tarefa.objects.filter(titulo='Nova Tarefa').exists())

    def test_editar_tarefa(self):
        response = self.client.post(reverse('editar_tarefa', args=[self.tarefa1.id]), {
            'titulo': 'Tarefa 1 Editada',
            'descricao': 'Descrição editada',
            'concluida': True  # Explicitamente definindo como True
    })
    
        self.assertRedirects(response, reverse('listar_tarefas'))
    
        tarefa_atualizada = Tarefa.objects.get(id=self.tarefa1.id)
        self.assertEqual(tarefa_atualizada.titulo, 'Tarefa 1 Editada')
        self.assertEqual(tarefa_atualizada.descricao, 'Descrição editada')
        self.assertTrue(tarefa_atualizada.concluida)

    def test_deletar_tarefa(self):
        response = self.client.post(reverse('deletar_tarefa', args=[self.tarefa1.id]))
        
        self.assertRedirects(response, reverse('listar_tarefas'))
        
        self.assertFalse(Tarefa.objects.filter(id=self.tarefa1.id).exists())

    def test_deletar_tarefa_get(self):
        response = self.client.get(reverse('deletar_tarefa', args=[self.tarefa1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Tarefa 1')