from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('firstapp/', include('firstapp.urls')),
    path('secondapp/', include('secondapp.urls')),
    path('thirdapp/', include('thirdapp.urls')),
    path('fourthapp/', include('fourthapp.urls'))
]
