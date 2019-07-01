from django.shortcuts import render


# Create your views here.
def reserva(request):
    return render(request, "reserva/reserva.html")


def pago(request):
    return render(request, "reserva/pago.html")


def mesa(request):
    return render(request, "reserva/mesa.html")


def menu(request):
    from services.models import Service
    servicios = Service.objects.all()
    return render(request, "reserva/menu.html",{'servicios':servicios})


def final(request):
    return render(request, "reserva/final.html")
