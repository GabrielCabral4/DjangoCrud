# Generated by Django 5.1.7 on 2025-03-28 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0002_tarefa_pinned'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
