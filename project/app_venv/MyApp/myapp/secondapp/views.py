from django.shortcuts import render


def indexPage(request):
    return render(request, 'frontend.html')
