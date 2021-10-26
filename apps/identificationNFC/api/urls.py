from django.urls import path
from apps.identificationNFC.api.views.general_viewsets import ActiveModelListAPIView, IdentificationCreateListAPIView, IdentificationRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('state/', ActiveModelListAPIView.as_view(), name= 'Estado NFC'),
    path('nfc/', IdentificationCreateListAPIView.as_view(), name= 'Create_List Identificación NFC'),
    path('nfc/<int:pk>/', IdentificationRetrieveUpdateDestroyAPIView.as_view(), name= 'Retrieve_Update_Destroy Identificación NFC')
]
