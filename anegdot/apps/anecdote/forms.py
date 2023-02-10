from django.forms import ModelForm, Textarea, TextInput
from .models import Anecdote

class AnecdoteForm(ModelForm):
    class Meta:
        model = Anecdote
        fields = ['anecdot_title', 'anecdot_text']
        
        widgets = {
            'anecdot_title': TextInput(attrs={
                'class': 'text-name_input',
                'placeholder': 'Назва гуморески'
            }),
            'anecdot_text': Textarea(attrs={
                'placeholder': 'Teкст...'
            })
        }
