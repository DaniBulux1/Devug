from django import forms
from .models import Tutorial


class TutorialForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields = ['titulo', 'contenido']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del tutorial'}),
            'contenido': forms.Textarea(attrs={
                'class': 'form-control wysiwyg-editor',  # Esto lo usará el frontend para activar el editor
                'placeholder': 'Escribe el contenido aquí...'
            }),
        }
        labels = {
            'titulo': 'Título',
            'contenido': 'Contenido del Tutorial',
        }