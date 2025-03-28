from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    concluida = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    pinned = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.titulo