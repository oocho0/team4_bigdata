from django.shortcuts import render

def mapPage(request):
    return render(request, 'map.html')