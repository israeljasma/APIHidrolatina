from django.db import models
from simple_history.models import HistoricalRecords

class activeModel(models.Model):
    id = models.AutoField(primary_key = True)
    active = models.BooleanField('Estado', default = True)
    description = models.CharField('Descripción', max_length = 255, blank = True, null = True)
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

        verbose_name = 'Estado Autentificación NFC'
        verbose_name_plural = 'Estado Autenticaciones NFC'

    def __str__(self):
        if self.active:
            return f'{"Activo"} {self.description}'
        else:
            return f'{"Inactivo"} {self.description}'
    # def __str__(self):
    #     return f'{self.active} {self.description}'

class identification(models.Model):
    id = models.AutoField(primary_key = True)
    NFC = models.CharField('NFC',max_length = 255, unique = True)
    state = models.BooleanField('Activo', default = True)
    created_date = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)
    modified_date = models.DateField('Fecha de Modificación', auto_now = True, auto_now_add = False)
    active = models.ForeignKey(activeModel, on_delete=models.CASCADE, verbose_name = 'Estado Autentificación NFC')
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'NFC'
        verbose_name_plural = 'NFCs'

    def __str__(self):
        return self.NFC
