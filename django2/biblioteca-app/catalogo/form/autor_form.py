from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from catalogo.models.autor import Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 
                'apellido', 
                'nacionalidad'] 
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control'}),
        }

    '''    #clean identifica a un método para validar
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre:
            nombre = nombre.strip()
        if not nombre:
            raise ValidationError("El nombre no puede estar vacío.")
        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data.get('apellido')
        if apellido:
            apellido = apellido.strip()
        if not apellido:
            raise ValidationError("El apellido no puede estar vacío.")
        return apellido

    def clean_nacionalidad(self):
        nacionalidad = self.cleaned_data.get('nacionalidad')
        if nacionalidad:
            nacionalidad = nacionalidad.strip()
        if not nacionalidad:
            raise ValidationError("La nacionalidad no puede estar vacía.")
        return nacionalidad '''
