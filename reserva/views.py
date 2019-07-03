from django.shortcuts import render, get_object_or_404,redirect, reverse, HttpResponseRedirect
from .models import Pedido, Detalle_pedido,Reserva


# Create your views here.
def reserva(request):
    return render(request, "reserva/reserva.html")


def pago(request):
    return render(request, "reserva/pago.html")


def mesa(request):

    if request.method =='POST':

        pdd = Pedido(monto_total=0.0)
        pdd.save()
        reserva = Reserva(fecha=request.POST['datepicker'], pedido=pdd)
        reserva.save()
        return HttpResponseRedirect(reverse('menu', args=[pdd.id]))

    else:

        return render(request, "reserva/mesa.html")


def menu(request, pedido_id):
    from services.models import Service
    pedido = get_object_or_404(Pedido, id=pedido_id)
    servicios = Service.objects.all()


    if request.method =='POST':
        for e in request.POST['elegido']:
            print(e)

    return render(request, "reserva/menu.html",{'servicios':servicios,'pedido':pedido})


def final(request):
    return render(request, "reserva/final.html")
