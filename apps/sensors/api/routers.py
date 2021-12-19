from django.db import router
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from apps.sensors.api.views.views import RejectFlowViewSet, PermeateFlowViewSet, PermeateConductivityViewSet, RejectionPressureViewSet, FeedConductivityViewSet, DeedingTemperatureViewSet, FeedPressureViewSet

router = DefaultRouter()

router.register(r'rejectflow', RejectFlowViewSet, basename= 'RejectFlow')
router.register(r'permeateflow', PermeateFlowViewSet, basename= 'PermeateFlow')
router.register(r'permeateconductivity', PermeateConductivityViewSet, basename= 'PermeateConductivity')
router.register(r'rejectionpressure', RejectionPressureViewSet, basename= 'RejectionPressure')
router.register(r'feedconductivity', FeedConductivityViewSet, basename= 'FeedConductivity')
router.register(r'deedingtemperature', DeedingTemperatureViewSet, basename= 'DeedingTemperature')
router.register(r'feedpressure', FeedPressureViewSet, basename= 'FeedPressure')

urlpatterns = router.urls