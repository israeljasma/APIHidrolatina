from django.contrib import admin
from apps.sensors.models import *

# Register your models here.
admin.site.register(RejectFlow)
admin.site.register(PermeateFlow)
admin.site.register(PermeateConductivity)
admin.site.register(RejectionPressure)
admin.site.register(FeedConductivity)
admin.site.register(DeedingTemperature)
admin.site.register(FeedPressure)