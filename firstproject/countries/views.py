from django.shortcuts import render
from rest_framework import viewsets
from .models import Country
from .serializers import CountrySerializer

# Create your views here.
class CountryView(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()