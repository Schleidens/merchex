"""merchex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name="homePage"),
    path("resources/", views.resources, name="resources"),
    path('band/<int:id>', views.band_details, name="band-view"),
    path('contact/', views.contact_form, name='contact'),
    path('band/add/', views.create_band, name='create_band'),
    path('band/<int:id>/update/', views.update_band, name='update-band'),
    path('band/<int:id>/delete/', views.delete_band, name='delete-band')
]
