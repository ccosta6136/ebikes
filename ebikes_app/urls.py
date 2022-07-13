


from django.urls import path
from ebikes_app.views import form_usuario, form_bicicleta, form_insumo, form_busqueda


urlpatterns = [
    path('usuario/', form_usuario),
    path('bicicleta/', form_bicicleta),
    path('insumo/', form_insumo),
    path('busqueda/', form_busqueda)
]
