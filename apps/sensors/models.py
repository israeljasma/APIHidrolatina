from django.db import models

# from simple_history.models import HistoricalRecords


class FeedConductivity(models.Model):
    id = models.AutoField(primary_key = True)
    number = models.FloatField(null = False)
    unit = models.CharField(max_length=255)
    time = models.DateTimeField('Fecha', null = False)
    created_date = models.DateTimeField('Fecha de Creación', auto_now = False, auto_now_add = True)
    modified_date = models.DateTimeField('Fecha de Modificación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Conductividad de alimentación'
        verbose_name_plural = 'Conductividades de alimentación'

class FeedTemperature(models.Model):
    id = models.AutoField(primary_key = True)
    number = models.FloatField(null = False)
    unit = models.CharField(max_length=255)
    time = models.DateTimeField('Fecha', null = False)
    created_date = models.DateTimeField('Fecha de Creación', auto_now = False, auto_now_add = True)
    modified_date = models.DateTimeField('Fecha de Modificación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Temperatura de alimentación'
        verbose_name_plural = 'Temperaturas de alimentación'

class MembranePermeateFlow(models.Model):
    id = models.AutoField(primary_key = True)
    number = models.FloatField(null = False)
    unit = models.CharField(max_length=255)
    time = models.DateTimeField('Fecha', null = False)
    created_date = models.DateTimeField('Fecha de Creación', auto_now = False, auto_now_add = True)
    modified_date = models.DateTimeField('Fecha de Modificación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Caudal de permeado de membranas'
        verbose_name_plural = 'Caudales de permeado de membranas'

class MembraneRejectionFlow(models.Model):
    id = models.AutoField(primary_key = True)
    number = models.FloatField(null = False)
    unit = models.CharField(max_length=255)
    time = models.DateTimeField('Fecha', null = False)
    created_date = models.DateTimeField('Fecha de Creación', auto_now = False, auto_now_add = True)
    modified_date = models.DateTimeField('Fecha de Modificación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Caudal de rechazo de membranas'
        verbose_name_plural = 'Caudales de rechazo de membranas'

class MembraneFeedPressure(models.Model):
    id = models.AutoField(primary_key = True)
    number = models.FloatField(null = False)
    unit = models.CharField(max_length=255)
    time = models.DateTimeField('Fecha', null = False)
    created_date = models.DateTimeField('Fecha de Creación', auto_now = False, auto_now_add = True)
    modified_date = models.DateTimeField('Fecha de Modificación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Presión de alimentación de membranas'
        verbose_name_plural = 'Presiones de alimentación de membranas'

class MembraneRejectionPressure(models.Model):
    id = models.AutoField(primary_key = True)
    number = models.FloatField(null = False)
    unit = models.CharField(max_length=255)
    time = models.DateTimeField('Fecha', null = False)
    created_date = models.DateTimeField('Fecha de Creación', auto_now = False, auto_now_add = True)
    modified_date = models.DateTimeField('Fecha de Modificación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Presión de rechazo de membranas'
        verbose_name_plural = 'Presiones de rechazo de membranas'

class ConductivityPermeateMembranes(models.Model):
    id = models.AutoField(primary_key = True)
    number = models.FloatField(null = False)
    unit = models.CharField(max_length=255)
    time = models.DateTimeField('Fecha', null = False)
    created_date = models.DateTimeField('Fecha de Creación', auto_now = False, auto_now_add = True)
    modified_date = models.DateTimeField('Fecha de Modificación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Conductividad de permeado de membranas'
        verbose_name_plural = 'Conductividades de permeado de membranas'

class VesselsPermeateFlow(models.Model):
    id = models.AutoField(primary_key = True)
    number = models.FloatField(null = False)
    unit = models.CharField(max_length=255)
    time = models.DateTimeField('Fecha', null = False)
    created_date = models.DateTimeField('Fecha de Creación', auto_now = False, auto_now_add = True)
    modified_date = models.DateTimeField('Fecha de Modificación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Flujo de permeado de vasijas'
        verbose_name_plural = 'Flujos de permeado de vasijas'

class VesselsFeedingFlow(models.Model):
    id = models.AutoField(primary_key = True)
    number = models.FloatField(null = False)
    unit = models.CharField(max_length=255)
    time = models.DateTimeField('Fecha', null = False)
    created_date = models.DateTimeField('Fecha de Creación', auto_now = False, auto_now_add = True)
    modified_date = models.DateTimeField('Fecha de Modificación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Caudal de alimentación de vasijas'
        verbose_name_plural = 'Caudales de alimentación de vasijas'

class FeedPressureVessels(models.Model):
    id = models.AutoField(primary_key = True)
    number = models.FloatField(null = False)
    unit = models.CharField(max_length=255)
    time = models.DateTimeField('Fecha', null = False)
    created_date = models.DateTimeField('Fecha de Creación', auto_now = False, auto_now_add = True)
    modified_date = models.DateTimeField('Fecha de Modificación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Presión de alimentación de vasijas'
        verbose_name_plural = 'Presiones de alimentación de vasijas'

class RejectPressureVessels(models.Model):
    id = models.AutoField(primary_key = True)
    number = models.FloatField(null = False)
    unit = models.CharField(max_length=255)
    time = models.DateTimeField('Fecha', null = False)
    created_date = models.DateTimeField('Fecha de Creación', auto_now = False, auto_now_add = True)
    modified_date = models.DateTimeField('Fecha de Modificación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Presión de rechazo de vasijas'
        verbose_name_plural = 'Presiones de rechazo de vasijas'

class ConductivityPermeateVessels(models.Model):
    id = models.AutoField(primary_key = True)
    number = models.FloatField(null = False)
    unit = models.CharField(max_length=255)
    time = models.DateTimeField('Fecha', null = False)
    created_date = models.DateTimeField('Fecha de Creación', auto_now = False, auto_now_add = True)
    modified_date = models.DateTimeField('Fecha de Modificación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Conductividad de permeado de vasijas'
        verbose_name_plural = 'Conductividades de permeado de vasijas'

class RegisterMembranes(models.Model):
    id = models.AutoField(primary_key = True)
    register = models.BooleanField(null = False)
    time = models.DateTimeField('Fecha', null = False)
    created_date = models.DateTimeField('Fecha de Creación', auto_now = False, auto_now_add = True)
    modified_date = models.DateTimeField('Fecha de Modificación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Registro de membranas'
        verbose_name_plural = 'Registros de membranas'

class RegisterVessels(models.Model):
    id = models.AutoField(primary_key = True)
    register = models.BooleanField(null = False)
    time = models.DateTimeField('Fecha', null = False)
    created_date = models.DateTimeField('Fecha de Creación', auto_now = False, auto_now_add = True)
    modified_date = models.DateTimeField('Fecha de Modificación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Registro de vasijas'
        verbose_name_plural = 'Registros de vasijas'