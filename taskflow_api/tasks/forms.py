from django import forms
from .models import PlanDietetico

class PlanDieteticoForm(forms.ModelForm):
    class Meta:
        model = PlanDietetico
        fields = ['paciente', 'titulo', 'descripcion', 'calorias_diarias']