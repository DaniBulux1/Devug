from django import forms
from .models import Tutorial

class TutorialForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields = ['titulo', 'contenido']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Título del tutorial',
                'required': True
            }),
            'contenido': forms.Textarea(attrs={
                'class': 'form-control wysiwyg-editor',
                'placeholder': 'Escribe el contenido aquí...',
                'rows': 10,
                'required': True,
                'id': 'id_contenido'  # Importante para el JS de formato
            }),
        }
        labels = {
            'titulo': 'Título',
            'contenido': 'Contenido del Tutorial',
        }
    
    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if len(titulo.strip()) < 5:
            raise forms.ValidationError('El título debe tener al menos 5 caracteres.')
        return titulo.strip()
    
    def clean_contenido(self):
        contenido = self.cleaned_data.get('contenido')
        if len(contenido.strip()) < 10:
            raise forms.ValidationError('El contenido debe tener al menos 10 caracteres.')
        return contenido