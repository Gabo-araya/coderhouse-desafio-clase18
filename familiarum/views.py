from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from familiarum.models import Persona
from familiarum.utils import buscar_personas

import calendar, datetime
from datetime import datetime, date, timedelta

#==========================================================================================================
#
# Personas
#
#==========================================================================================================


def listar_personas(request, *args, **kwargs):
    '''Lista de elementos activos con las que se pueden realizar acciones.'''

    #queryset, buscar = buscar_personas(request, *args, **kwargs)

    queryset = Persona.objects.all()

    context = {
        'page' : 'Personas',
        'icon' : 'person',
        #'buscar' : buscar,
        'lista_personas': queryset
    }
    return render(request, 'familiarum/listar_personas.html', context)
