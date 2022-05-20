from django.db import router
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from apps.users.api.api import UserViewSet, UserNFCViewSet, GroupViewSet

router = DefaultRouter()

router.register(r'users', UserViewSet, basename="users")
router.register(r'usernfc', UserNFCViewSet, basename="usernfc")
router.register(r'usergroup', GroupViewSet, basename="groupuser")

urlpatterns = router.urls