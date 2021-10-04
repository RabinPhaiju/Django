from django.contrib import admin
from django.urls import path,include
from django.urls.conf import include
from Shortner import views
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Shortner.urls')),
    path('templatee/',include('templatee.urls'))
]
