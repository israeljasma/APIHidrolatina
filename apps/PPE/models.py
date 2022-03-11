from django.db import models

from simple_history.models import HistoricalRecords

from apps.users.models import User

# Create your models here.

class detectionPPE(models.Model):
    id = models.AutoField(primary_key = True)
    helmet = models.BooleanField('Casco')
    headphones = models.BooleanField('Audifonos')
    goggles = models.BooleanField('Antiparras')
    gloves = models.BooleanField('Guantes')
    boots = models.BooleanField('Botas')
    state = models.BooleanField('estado', default=True)
    date = models.DateTimeField('Fecha', auto_now = False, auto_now_add = True, null = True)
    created_date = models.DateTimeField('Fecha de Creación', auto_now = False, auto_now_add = True)
    modified_date = models.DateTimeField('Fecha de Modificación', auto_now = True, auto_now_add = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Usuario detectado', blank = True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'detecion PPE'
        verbose_name_plural = 'detecciones PPE'