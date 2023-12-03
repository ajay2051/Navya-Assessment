from django.urls import path
from . import views
from .views import GeneratePdf

urlpatterns = [
    path("", views.information, name='information'),
    path("generate-pdf/", GeneratePdf.as_view(), name='generate_pdf'),
]
