from .models import deadpool
from rest_framework import serializers

class DeadpoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = deadpool
        fields = ('id','name','apellido','telefono')

