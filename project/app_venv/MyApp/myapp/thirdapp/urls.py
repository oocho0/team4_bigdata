from django.urls import path
from .views import *

app_name = 'homePage'

urlpatterns = [
    path('', homePage, name='homePage'),
]