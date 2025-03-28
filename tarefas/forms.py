from django import forms
from .models import Tarefa
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'concluida']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500',
                'placeholder': _('Digite o título')
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500',
                'placeholder': _('Digite a descrição'),
                'rows': 4
            }),
            'concluida': forms.CheckboxInput(attrs={
                'class': 'form-checkbox h-5 w-5 text-blue-600'
            })
        }
        labels = {
            'titulo': _('Título'),
            'descricao': _('Descrição'),
            'concluida': _('Concluída')
        }
        help_texts = {
            'titulo': _('Máximo de 200 caracteres'),
            'descricao': _('Opcional - forneça detalhes adicionais')
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500'
            })

    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        if len(titulo) < 3:
            raise ValidationError(_('O título deve ter pelo menos 3 caracteres'))
        return titulo

    def clean(self):
        cleaned_data = super().clean()
        
        # Exemplo de validação customizada
        titulo = cleaned_data.get('titulo')
        descricao = cleaned_data.get('descricao')
        
        if titulo and descricao and len(titulo) > len(descricao):
            # Exemplo de validação (pode ser removida)
            msg = _('A descrição deve fornecer mais contexto que o título')
            self.add_error('descricao', msg)
        
        return cleaned_data