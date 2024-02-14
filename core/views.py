################# Libs #################
from django.shortcuts import render
from . import models
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .serializer import GeneralinfoSerializer
#######################################

class GeneralinfoView(ModelViewSet):
        queryset = models.GeneralInfo.objects.all()
        serializer_class = GeneralinfoSerializer

        