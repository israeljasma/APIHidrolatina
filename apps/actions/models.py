from django.db import models

from simple_history.models import HistoricalRecords

from apps.users.models import User

# Create your models here.
class risk(models.Model):
    id = models.AutoField(primary_key = True)
    risk = models.CharField('Riesgo', max_length = 255, blank = True, null = True)
    state = models.BooleanField('Estado', default=True)
    created_date = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)
    modified_date = models.DateField('Fecha de Modificación', auto_now = True, auto_now_add = False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Risk'
        verbose_name_plural = 'Risks'

    def __str__(self):
        return self.risk

class action(models.Model):
    id = models.AutoField(primary_key = True)
    action = models.CharField('Acción', max_length = 255, blank = True, null = True)
    state = models.BooleanField('Estado', default=True)
    created_date = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)
    modified_date = models.DateField('Fecha de Modificación', auto_now = True, auto_now_add = False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Action'
        verbose_name_plural = 'Actions'
    
    def __str__(self):
        return self.action

class actionDetection(models.Model):
    id = models.AutoField(primary_key = True)
    operator_present = models.BooleanField('Operador Presente')
    action = models.ForeignKey(action, on_delete=models.CASCADE, verbose_name = 'Acción')
    risk = models.ForeignKey(risk, on_delete=models.CASCADE, verbose_name = 'Riesgo')
    hour = models.TimeField('Hora', auto_now = False, auto_now_add = True)
    state = models.BooleanField('estado', default=True)
    date = models.DateField('Fecha', auto_now = False, auto_now_add = True)
    created_date = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)
    modified_date = models.DateField('Fecha de Modificación', auto_now = True, auto_now_add = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Usuario operador')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Action Detection'
        verbose_name_plural = 'Actions Detection'

    def __str__(self):
        return f'{self.user.name}, {self.action}, {self.risk}, {self.hour}'