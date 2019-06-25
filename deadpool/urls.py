from django.urls import path
from .views import *

urlpatterns =[
    path('deapool',DeadpoolList.get_object, name='deadpool'),
]