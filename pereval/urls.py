from django.urls import path, include
from .views import SubmitData, SubmitDataDetail, SubmitDataUpdate


urlpatterns = [
    path('submitData/', SubmitData.as_view(), name='submit_data'),
    path('submitData/<int:pk>/', SubmitDataDetail.as_view(), name='submit_data_detail'),
    path('submitData/<int:pk>/edit/', SubmitDataUpdate.as_view(), name='submit_data_detail'),
]