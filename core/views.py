from django.shortcuts import render

# Create your views here.
def home (request):
    return render (request,"core/home.html")

def about (request):
    return render (request,"core/about.html")

def store (request):
    return render (request,"core/store.html")

def reserva (request):
    return render (request,"core/reserva.html")

def pago (request):
    return render (request,"core/pago.html")
    
def mesa (request):
    return render (request,"core/mesa.html")

def menu (request):
    return render (request,"core/menu.html")
def final (request):
    return render (request,"core/final.html")

