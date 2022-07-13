from django import forms

class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()


class BicicletaForm(forms.Form):
    marca = forms.CharField(max_length=40)
    modelo = forms.CharField(max_length=40)
    rodado = forms.IntegerField()
    precio = forms.IntegerField()


class InsumoForm(forms.Form):
    marca = forms.CharField(max_length=40)
    descripcion = forms.CharField(max_length=40)
    precio = forms.IntegerField() 


class BicicletaBusqueda(forms.Form):
    criterio = forms.CharField()