from django.http import HttpResponse
from django.template.loader import get_template


class MainView():
    def home(self):
        plantilla = get_template('index.html')
        return  HttpResponse(plantilla.render())

    def fregistro(self):
        plantilla = get_template('F_Registro.html')
        return  HttpResponse(plantilla.render())

    def fproductos(self):
        plantilla = get_template('F_Productos.html')
        return  HttpResponse(plantilla.render())
    def fclientes(self):
        plantilla = get_template('F_Clientes.html')
        return HttpResponse(plantilla.render())
    def rpersonal(self):
        plantilla = get_template('R_Personal.html')
        return HttpResponse(plantilla.render())
    def rvehiculos(self):
        plantilla = get_template('R_Vehiculos.html')
        return HttpResponse(plantilla.render())