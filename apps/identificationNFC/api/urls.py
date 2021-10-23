from django.urls import path
from apps.identificationNFC.api.views.general_views import ActiveModelListAPIView, IdentificationSerializerListAPIView

urlpatterns = [
    path('state/', ActiveModelListAPIView.as_view(), name= 'Estado NFC'),
    path('nfc/', IdentificationSerializerListAPIView.as_view(), name= 'Identificación NFC')
]
