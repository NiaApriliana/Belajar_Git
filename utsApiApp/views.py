from django.shortcuts import render
from utsApiApp.models import jadwalModels
from rest_framework.response import Response
from utsApiApp.serializers import jadwalSerializer
from rest_framework import viewsets

# rest framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
class jadwalViewset(viewsets.ModelViewSet):
    queryset = jadwalModels.objects.all()
    serializer_class = jadwalSerializer

