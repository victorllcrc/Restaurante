from rest_framework import generics
from .models import deadpool
from .serializers import DeadpoolSerializer
from django.shortcuts import get_object_or_404

class DeadpoolList(generics.ListCreateAPIView):

    queryset = deadpool.objects.all()
    serializer_class = DeadpoolSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['id'],
        )
        return obj

