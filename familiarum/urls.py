from django.urls import path
import familiarum.views

urlpatterns = [

    #Personas
    path('', familiarum.views.listar_personas, name='listar_personas'),
    # path('listar_personas/', familiarum.views.listar_personas, name='listar_personas'),
    # path('crear_persona/', familiarum.views.crear_persona, name='crear_persona'),
    # path('ver_persona/<int:id>/', familiarum.views.ver_persona, name='ver_persona'),
    # path('modificar_persona/<int:id>/', familiarum.views.modificar_persona, name='modificar_persona'),
    # path('eliminar_persona/<int:id>/', familiarum.views.eliminar_persona, name='eliminar_persona'),

]