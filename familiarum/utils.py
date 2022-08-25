from django.db.models import Q
from familiarum.models import Persona
from datetime import datetime, date, timedelta


def buscar_personas(request, *args, **kwargs):
    ''' Función para buscar personas '''

    buscar = ''
    if request.GET.get('buscar'):
        buscar = request.GET.get('buscar')
        # print(buscar)

        # queryset = Persona.objects.distinct().filter(
        #     Q(nombre_completo__icontains=buscar) |  
        #     Q(cedula_identidad__icontains=buscar) 
        #     )
        queryset = Persona.objects.filter(nombre_completo__icontains=buscar)

    else:
        queryset = Persona.objects.all() # Lista de objetos
        # queryset = Persona.objects.distinct() # Lista de objetos

    return queryset, buscar

    # MODO DE USO
    #queryset, buscar = buscar_personas(request, *args, **kwargs)
    pass




def averigua_bisiesto(year, *args, **kwargs):
    '''Función para calcular si un año es bisiesto o no'''
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    # MODO DE USO
    # bisiesto = averigua_bisiesto(year, *args, **kwargs)
    pass




def armar_lista_fecha(fecha = datetime.now(), feriados = [], *args, **kwargs):
    '''Función que entrega información de una fecha string ('%Y-%m-%d').'''
    #fecha = str(fecha)
    #now = datetime.now()
    if type(fecha) == str:
        fecha = datetime.strptime(fecha, '%Y-%m-%d').date()

    if len(feriados) > 0: 
        for dia in feriados: 
            # print(dia)
            if dia['fecha'] == fecha:
                feriado = True
                # print("THIS")
                break
            else:
                feriado = False
    else:
        feriado = False
                
    year = fecha.year
    month = fecha.month
    day = fecha.day
    weekday = fecha.isoweekday()

    if weekday == 1: 
        weekday_str = 'Lunes'
    elif weekday == 2: 
        weekday_str = 'Martes'
    elif weekday == 3: 
        weekday_str = 'Miércoles'
    elif weekday == 4: 
        weekday_str = 'Jueves'
    elif weekday == 5: 
        weekday_str = 'Viernes'
    elif weekday == 6: 
        weekday_str = 'Sábado'
    elif weekday == 7: 
        weekday_str = 'Domingo'
    else:
        print('No es un día de semana')

    fecha_str = str(fecha)

    partes = fecha_str.split('-')
    # partes = partes[::-1]
    fecha_str_es = partes[2] + '/' + partes[1] #+ '/' + partes[0]
    bisiesto = averigua_bisiesto(year)

    fecha_armada = {'fecha': fecha, 
                    'anio': year,
                    'mes': month,
                    'dia': day,
                    'fecha_str': fecha_str,
                    'fecha_str_es': fecha_str_es,
                    'dia_semana': weekday,
                    'dia_semana_str': weekday_str[:3],
                    'feriado': feriado,
                    'bisiesto': bisiesto,
                    }

    #return fecha, year, month, day, fecha_str, weekday, weekday_str, bisiesto
    return fecha_armada

    # MODO DE USO
    # fecha_armada = armar_lista_fecha(fecha_inicio, *args, **kwargs)

    # fecha_armada_inicio = descomponer_fecha('2022-01-24', *args, **kwargs)
    # print(fecha_armada_inicio.fecha)

    # print('==================')
    pass

