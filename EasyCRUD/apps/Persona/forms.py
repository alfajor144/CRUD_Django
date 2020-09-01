  
from django import forms
from .models import Persona

class PersonaForms(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'nacionalidad', 'descripcion']