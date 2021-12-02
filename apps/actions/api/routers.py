from django.db import router
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from apps.actions.api.views.views import actionDetectionViewSet

router = DefaultRouter()

router.register(r'action', actionDetectionViewSet, basename= 'actions')

urlpatterns = router.urls