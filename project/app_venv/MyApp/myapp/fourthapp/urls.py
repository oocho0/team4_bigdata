from django.urls import path
from .views import *

app_name = 'accumulate'

urlpatterns = [
    path('', accumulate, name='accumulate'),
]