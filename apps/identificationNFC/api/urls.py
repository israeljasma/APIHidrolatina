from django.urls import path
from apps.identificationNFC.api.views.general_views import ActiveModelListAPIView, IdentificationSerializerListAPIView, IdentificationCreateAPIView

urlpatterns = [
    path('state/', ActiveModelListAPIView.as_view(), name= 'Estado NFC'),
    path('nfc/', IdentificationSerializerListAPIView.as_view(), name= 'Identificación NFC'),
    path('nfc/create/', IdentificationCreateAPIView.as_view(), name= 'Create Identificación NFC')
]
