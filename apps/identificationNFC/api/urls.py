from django.urls import path
from apps.identificationNFC.api.views.general_views import ActiveModelListAPIView, IdentificationSerializerListAPIView, IdentificationCreateAPIView, IdentificationRetrieveAPIView, IdentificationDestroyAPIView, IdentificationUpdateAPIView

urlpatterns = [
    path('state/', ActiveModelListAPIView.as_view(), name= 'Estado NFC'),
    path('nfc/', IdentificationSerializerListAPIView.as_view(), name= 'List Identificación NFC'),
    path('nfc/create/', IdentificationCreateAPIView.as_view(), name= 'Create Identificación NFC'),
    path('nfc/<int:pk>/', IdentificationRetrieveAPIView.as_view(), name= 'Retrieve Identificación NFC'),
    path('nfc/<int:pk>/destroy/', IdentificationDestroyAPIView.as_view(), name= 'Destroy Identificación NFC'),
    path('nfc/<int:pk>/update/', IdentificationUpdateAPIView.as_view(), name= 'Update Identificación NFC')
]
