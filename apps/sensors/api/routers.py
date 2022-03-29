from django.db import router
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from apps.sensors.api.views.views import FeedConductivityViewSet, FeedTemperatureViewSet, MembranePermeateViewSet, MembraneRejectionFlowViewSet, MembraneFeedPressureViewSet, MembraneRejectionPressureViewSet, ConductivityPermeateMembranesViewSet, VesselsPermeateFlowViewSet, VesselsFeedingFlowViewSet, FeedPressureVesselsViewSet, RejectPressureVesselsViewSet, ConductivityPermeateVesselsViewSet, RegisterMembranesViewSet, RegisterVesselsViewSet

router = DefaultRouter()

router.register(r'feedconductivity', FeedConductivityViewSet, basename= 'FeedConductivity')
router.register(r'feedtemperature', FeedTemperatureViewSet, basename= 'FeedTemperature')
router.register(r'membranepermeate', MembranePermeateViewSet, basename= 'MembranePermeate')
router.register(r'membranerejectionflow', MembraneRejectionFlowViewSet, basename= 'MembraneRejectionFlow')
router.register(r'membranefeedpressure', MembraneFeedPressureViewSet, basename= 'MembraneFeedPressure')
router.register(r'membranerejectionpressure', MembraneRejectionPressureViewSet, basename= 'MembraneRejectionPressure')
router.register(r'conductivitypermeatemembranes',ConductivityPermeateMembranesViewSet , basename= 'ConductivityPermeateMembranes')
router.register(r'vesselspermeateflow',VesselsPermeateFlowViewSet , basename= 'VesselsPermeateFlow')
router.register(r'vesselsfeedingflow',VesselsFeedingFlowViewSet , basename= 'VesselsFeedingFlow')
router.register(r'feedpressurevessels',FeedPressureVesselsViewSet , basename= 'FeedPressureVessels')
router.register(r'rejectpressurevessels',RejectPressureVesselsViewSet , basename= 'RejectPressureVessels')
router.register(r'conductivitypermeatevessels',ConductivityPermeateVesselsViewSet , basename= 'ConductivityPermeateVessels')
router.register(r'registermembranes',RegisterMembranesViewSet , basename= 'RegisterMembranes')
router.register(r'registervessels',RegisterVesselsViewSet , basename= 'RegisterVessels')

urlpatterns = router.urls