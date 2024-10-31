from django import forms
from .models import Gasto

class FormularioGasto(forms.ModelForm):
    # monto = forms.IntegerField(required=True)
    class Meta:
        model= Gasto
        fields = '__all__'