from django import forms

class ProductosFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    precio = forms.IntegerField()