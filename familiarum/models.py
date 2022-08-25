from django.db import models

#=======================================================================================================================================
# FAMILIARUM
#---------------------------------------------

class Persona(models.Model):
    ''' Este modelo guarda los datos de las personas. '''
    nombre_completo = models.CharField(max_length=250, null=True, blank=True, default='', verbose_name='Nombre completo')
    # slug = models.SlugField(null=True, blank=True, verbose_name='Slug')
    fecha_nacimiento = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name='Fecha de nacimiento')
    cedula_identidad = models.IntegerField(null=True, blank=True, verbose_name='Cédula Identidad')
    direccion = models.TextField(null=True, blank=True, verbose_name='Dirección')
    observaciones = models.TextField(null=True, blank=True, verbose_name='Observaciones')
    
    # campos de gestión
    #activo = models.BooleanField(null=True, blank=True, default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Fecha de última modificación')
    #deleted = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de desactivación')

    class Meta:
        ''' class Meta:
            Define el nombre singular y plural, y el ordenamiento de los elementos
        '''
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['id']

    def __str__(self):
        ''' Retorna un string con el nombre del objeto en las listas y en el admin. '''
        return str('{}'. format(self.nombre_completo))