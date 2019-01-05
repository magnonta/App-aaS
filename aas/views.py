from django.shortcuts import render
from rest_framework import viewsets
from .models import aasItem
from .serializers import aasSerializer
# Create your views here.

class aasViewSet(viewsets.ModelViewSet):

    serializer_class = aasSerializer
    queryset = aasItem.objects.all()