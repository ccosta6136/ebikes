#Descripción
 Desarrollar una WEB Django con patrón MVT subida a Github.

#Correr App Ebikes
 Ingresar en un terminal y poner >> python manage.py runserver    
 Ej : Django version 4.0.5, using settings 'ebikes.settings'
     Starting development server at http://127.0.0.1:8000/


#Accesos 
 Raiz: http://127.0.0.1:8000/

 Para ingresar a la  Home:
 Home: http://127.0.0.1:8000/usuario 
 Se puede navegar desde esta acceso.

 Para ingresar al formulario de carga de forma individual :
  -Usuario:                 http://127.0.0.1:8000/usuario
  -bicicleta:               http://127.0.0.1:8000/bicileta
  -Insumo:                  http://127.0.0.1:8000/insumo

  Formulario de busqueda de bicicletas
  -Busqueda Bicicletas:     http://127.0.0.1:8000/busqueda


#Funcionalidades
 3 clases de Modelos
 --------------------

  class Usuario(models.Model):
  class Bicicleta(models.Model)
  class Insumo(models.Model):

 4 Formulario (forms.py)
 --------------------------

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


  
  
  
 
