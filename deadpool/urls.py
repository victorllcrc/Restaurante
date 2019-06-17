from django.urls import path
from .views import *

urlpatterns =[
    path('',DeadpoolList.as_view(), name='deadpool'),
]