from django.urls import path
from .views import DocumentoCreate


urlpatterns = [
    path('novo', DocumentoCreate.as_view(), name='create_documento'),
    #path('deletar/<int:pk>', DocumentoDelete.as_view(), name='delete_documento'),
]
