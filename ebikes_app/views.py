from django.shortcuts import render
from django.http import HttpResponse
from ebikes_app.models import Usuario, Bicicleta, Insumo
from ebikes_app.forms import UsuarioForm, BicicletaForm, InsumoForm, BicicletaBusqueda
# Create your views here.


def form_usuario(request):

    if request.method == "POST":
        
        mi_formulario = UsuarioForm(request.POST)

        if  mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data 
            usuario = Usuario(nombre=datos["nombre"], apellido=datos["apellido"], email=datos["email"])
            usuario.save()
            mi_formulario = UsuarioForm()
            return render(request, "ebikes_app/formulario_usuario.html", {"mensaje":"agregado con exito!", "mi_formulario":mi_formulario})
   
    else:

        mi_formulario = UsuarioForm()
    
    return render(request, "ebikes_app/formulario_usuario.html", {"mi_formulario":mi_formulario})




def form_bicicleta(request):

    if request.method == "POST":
        
        mi_formulario = BicicletaForm(request.POST)

        if  mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data 
            bicicleta = Bicicleta(marca=datos["marca"], modelo=datos["modelo"], rodado=datos["rodado"], precio=datos["precio"])
            bicicleta.save()
            mi_formulario = BicicletaForm ()
            return render(request, "ebikes_app/formulario_bicicleta.html", {"mensaje":"agregado con exito!", "mi_formulario":mi_formulario})
   
    else:

        mi_formulario = BicicletaForm()
    
    return render(request, "ebikes_app/formulario_bicicleta.html", {"mi_formulario":mi_formulario})




    
def form_insumo(request):

    if request.method == "POST":
        
        mi_formulario = InsumoForm(request.POST)

        if  mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data 
            insumo = Insumo(marca=datos["marca"], descripcion=datos["descripcion"], precio=datos["precio"])
            insumo.save()
            mi_formulario = InsumoForm()
            return render(request, "ebikes_app/formulario_insumo.html", {"mensaje":"agregado con exito!", "mi_formulario":mi_formulario})
   
    else:

        mi_formulario = InsumoForm()
    
    return render(request, "ebikes_app/formulario_insumo.html", {"mi_formulario":mi_formulario})



def form_busqueda(request):

    busqueda_formulario = BicicletaBusqueda()

    buscado = False

    if request.GET:    
        busqueda_formulario = BicicletaBusqueda(request.GET)
        if busqueda_formulario.is_valid():
            bicicletas = Bicicleta.objects.filter(marca=busqueda_formulario.cleaned_data.get("criterio")).all()
            return render(request, "ebikes_app/bicicleta_busqueda.html", {"busqueda_formulario": busqueda_formulario, "bicicletas": bicicletas, "buscado" : True})
    
    
    return render(request, "ebikes_app/bicicleta_busqueda.html", {"busqueda_formulario": busqueda_formulario, "buscado":buscado})