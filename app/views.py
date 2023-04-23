from django.shortcuts import render
from rest_framework import viewsets
from . models import Fraud
from . serializers import FraudSerializer
# Create your views here.

class FraudViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Fraud.objects.all()
    serializer_class = FraudSerializer
    #permission_classes = [IsAccountAdminOrReadOnly]