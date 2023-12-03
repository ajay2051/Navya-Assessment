from django.urls import path

from api.views import InformationAPIView

urlpatterns = [
    path('information/', InformationAPIView.as_view(), name='information')
]
