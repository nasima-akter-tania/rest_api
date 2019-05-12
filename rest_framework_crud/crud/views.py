from django.shortcuts import render
from .models import CrudModel
from .serializer import CrudSerializer
from rest_framework import viewsets


# Create your views here.
class CrudView(viewsets.ModelViewSet):
    queryset = CrudModel.objects.all()
    serializer_class = CrudSerializer
