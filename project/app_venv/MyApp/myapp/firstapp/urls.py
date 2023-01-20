from django.urls import path
from .views import *

app_name = 'mapPage'

urlpatterns = [
    path('', mapPage, name='mapPage'),
]