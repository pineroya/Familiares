from django.urls import include, path
from .views import listado_familia

urlpatterns = [
    path('familiares/', listado_familia)
]