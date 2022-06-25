from .models import *
from rest_framework import serializers


class DatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
       model = Data
       fields = ['guid', 'order', 'price', 'date', 'price_rub', ]
