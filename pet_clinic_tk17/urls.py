"""
URL configuration for pet_clinic_tk17 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django import views
from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import TemplateView



urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home",),
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('auth/', include('authentication.urls')),
    path('jenis-hewan/', include('jenis_hewan.urls')),
    path('hewan-peliharaan/', include('hewan_peliharaan.urls')),
    path('manajemenvaksin/', include('manajemen_vaksin.urls')),
    path('datavaksin/', include('datavaksin.urls', namespace='datavaksin')),
    path('dataklien/', include('dataklien.urls')),
    path('perawatan-hewan/', include('perawatan_hewan.urls')),
    path('kunjungan/', include('kunjungan.urls')),
]