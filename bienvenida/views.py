from django.shortcuts import render

from django.http import HttpResponse


from .models import Producto

# Create your views here.
def inicio(request):
    return render(request, 'home.html')

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista.html', {'productos': productos})
