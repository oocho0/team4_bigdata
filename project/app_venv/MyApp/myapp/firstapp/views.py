from django.shortcuts import render
from django.db.models import Avg


def mapPage(request):
    return render(request, 'map.html')