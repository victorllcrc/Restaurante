from django.urls import path
from . import views

urlpatterns = [
    path('reserva/', views.reserva, name="reserva"),
    path('pago/', views.pago, name="pago"),
    path('mesa/', views.mesa, name="mesa"),
    path('menu/', views.menu, name="menu"),
    path('final/', views.menu, name="final")

]




