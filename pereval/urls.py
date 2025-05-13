from django.urls import path, include
from .views import SubmitData


urlpatterns = [
    path('submitData/', SubmitData.as_view(), name='submit_data'),
]