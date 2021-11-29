from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.
class actionDetection(models.Model):
    id = models.AutoField(primary_key = True)
    