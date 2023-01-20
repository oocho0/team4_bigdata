from django.urls import path
from . import views

urlpatterns = [
    path('', views.mapPage, name='mapPage'),
]