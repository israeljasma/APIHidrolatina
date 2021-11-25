from django.db import router
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from apps.PPE.api.views.views import detectionPPEViewSet

router = DefaultRouter()

router.register(r'ppe', detectionPPEViewSet, basename= 'ppes')

urlpatterns = router.urls