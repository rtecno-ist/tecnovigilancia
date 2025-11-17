from django import forms
from .models import Incidente

class IncidenteForm(forms.ModelForm):

    acciones = forms.MultipleChoiceField(
        choices=Incidente.ACCIONES_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    # Campo opcional para el texto de "otro"
    accion_otro_texto = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Incidente
        exclude = ['codigo']  # no se muestra

        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        acciones = cleaned_data.get("acciones", [])
        texto_otro = cleaned_data.get("accion_otro_texto", "")

        # Si marca "otro" pero NO escribe texto
        if "otro" in acciones and not texto_otro:
            self.add_error("accion_otro_texto", "Debe describir la acción 'otro'.")

        return cleaned_data

