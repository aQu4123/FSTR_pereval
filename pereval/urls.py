from django.urls import path, include
from .views import SubmitData, SubmitDataDetail


urlpatterns = [
    path('submitData/', SubmitData.as_view(), name='submit_data'),
    path('submitData/<int:pk>/', SubmitDataDetail.as_view(), name='submit_data_detail'),
]