"""apihidrolatina URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.users.views import CustomObtainAuthToken, Login, Logout, LoginNFC

schema_view = get_schema_view(
   openapi.Info(
      title="Hidrolatina API",
      default_version='v1',
      description="Maqueta HRC",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="-"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('login/', Login.as_view(), name = 'Login'),
    path('nfclogin/', LoginNFC.as_view(), name = 'Login_NFC'),
    path('logout/', Logout.as_view(), name = 'Logout'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/renew/', CustomObtainAuthToken.as_view(), name='token'),
    path('users/', include('apps.users.api.routers')),
    path('identifications/', include('apps.identificationNFC.api.routers')),
    path('ppes/', include('apps.PPE.api.routers')),
    path('actiondetections/', include('apps.actions.api.routers')),
    path('sensors/', include('apps.sensors.api.routers')),
]
