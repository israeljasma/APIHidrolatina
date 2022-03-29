from django.contrib import admin
from apps.sensors.models import *

# Register your models here.
admin.site.register(FeedConductivity)
admin.site.register(FeedTemperature)
admin.site.register(MembranePermeateFlow)
admin.site.register(MembraneRejectionFlow)
admin.site.register(MembraneFeedPressure)
admin.site.register(MembraneRejectionPressure)
admin.site.register(ConductivityPermeateMembranes)
admin.site.register(VesselsPermeateFlow)
admin.site.register(VesselsFeedingFlow)
admin.site.register(FeedPressureVessels)
admin.site.register(RejectPressureVessels)
admin.site.register(ConductivityPermeateVessels)
admin.site.register(RegisterMembranes)
admin.site.register(RegisterVessels)