from django.urls import path
from .views import *

app_name = 'indexPage'

urlpatterns = [
    path('', indexPage, name='indexPage'),
]