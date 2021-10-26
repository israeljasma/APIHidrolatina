from django.db import router
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from apps.identificationNFC.api.views.general_viewsets import IdentificationViewSet, ActiveViewSet

router = DefaultRouter()

router.register(r'nfc', IdentificationViewSet, basename= 'nfcs')
router.register(r'active', ActiveViewSet, basename= 'actives')

urlpatterns = router.urls