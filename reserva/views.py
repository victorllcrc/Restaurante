from django.shortcuts import render

# Create your views here.
def reserva(request):
    return render(request, "reserva/reserva.html")


def pago(request):
    return render(request, "reserva/pago.html")


def mesa(request):
    return render(request, "reserva/mesa.html")


def menu(request):
    return render(request, "reserva/menu.html")


def final(request):
    return render(request, "reserva/final.html")
