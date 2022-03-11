from django.db import models

# from simple_history.models import HistoricalRecords

class RejectFlow(models.Model):
    id = models.AutoField(primary_key = True)
    number = models.FloatField()
    unit = models.CharField(max_length=255)
    created_date = models.DateTimeField('Fecha de Creación', auto_now = False, auto_now_add = True)
    modified_date = models.DateTimeField('Fecha de Modificación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Caudal de rechazo'
        verbose_name_plural = 'Caudales de rechazo'



class PermeateFlow(models.Model):
    id = models.AutoField(primary_key = True)
    number = models.FloatField()
    unit = models.CharField(max_length=255)
    created_date = models.DateTimeField('Fecha de Creación', auto_now = False, auto_now_add = True)
    modified_date = models.DateTimeField('Fecha de Modificación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Caudal de permeado'
        verbose_name_plural = 'Caudales de permeado'



class PermeateConductivity(models.Model):
    id = models.AutoField(primary_key = True)
    number = models.FloatField()
    unit = models.CharField(max_length=255)
    created_date = models.DateTimeField('Fecha de Creación', auto_now = False, auto_now_add = True)
    modified_date = models.DateTimeField('Fecha de Modificación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Conductividad de permeado'
        verbose_name_plural = 'Conductividades de permeado'



class RejectionPressure(models.Model):
    id = models.AutoField(primary_key = True)
    number = models.FloatField()
    unit = models.CharField(max_length=255)
    created_date = models.DateTimeField('Fecha de Creación', auto_now = False, auto_now_add = True)
    modified_date = models.DateTimeField('Fecha de Modificación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Presión de rechazo'
        verbose_name_plural = 'Presiones de rechazo'



class FeedConductivity(models.Model):
    id = models.AutoField(primary_key = True)
    number = models.FloatField()
    unit = models.CharField(max_length=255)
    created_date = models.DateTimeField('Fecha de Creación', auto_now = False, auto_now_add = True)
    modified_date = models.DateTimeField('Fecha de Modificación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Conductividad de alimentación'
        verbose_name_plural = 'Conductividades de alimentación'



class DeedingTemperature(models.Model):
    id = models.AutoField(primary_key = True)
    number = models.FloatField()
    unit = models.CharField(max_length=255)
    created_date = models.DateTimeField('Fecha de Creación', auto_now = False, auto_now_add = True)
    modified_date = models.DateTimeField('Fecha de Modificación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Temperatura de alimentación'
        verbose_name_plural = 'Temperaturas de alimentación'



class FeedPressure(models.Model):
    id = models.AutoField(primary_key = True)
    number = models.FloatField()
    unit = models.CharField(max_length=255)
    created_date = models.DateTimeField('Fecha de Creación', auto_now = False, auto_now_add = True)
    modified_date = models.DateTimeField('Fecha de Modificación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Presión de alimentación'
        verbose_name_plural = 'Presiones de alimentación'