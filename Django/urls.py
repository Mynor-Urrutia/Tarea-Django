"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from view.MainView import MainView

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', MainView.home, name='home'),
    path('F_Registro/', MainView.fregistro, name='fregistro'),
    path('F_Productos/', MainView.fproductos, name='fproductos'),
    path('F_Clientes/', MainView.fclientes, name='fclientes'),
    path('R_Personal/', MainView.rpersonal, name='rpersonal'),
    path('R_Vehiculos/', MainView.rvehiculos, name='rvehiculos')
]