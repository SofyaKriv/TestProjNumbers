from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from .tasks import get_data

# вывод всех записей из БД
class DatView(viewsets.ModelViewSet):
    serializer_class = DatSerializer # сериализатор
    queryset = Data.objects.all() # объекты, которые выводим из модели Data
    get_data.delay() # обращение к задаче по расписанию

