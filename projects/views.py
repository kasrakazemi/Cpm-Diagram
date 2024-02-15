################# Libs #################
from django.shortcuts import render
from . import models
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .serializer import PlansSerializer, ProjectSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
########################################


class ProjectsView(ModelViewSet):
    queryset = models.Projects.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    # def get_permissions(self):
    #     if self.request.method =='GET':
    #         return [AllowAny()]
    #     return [IsAuthenticated()]

class PlansView(ModelViewSet):
    queryset = models.Plans.objects.all()
    serializer_class = PlansSerializer
    permission_classes = [IsAuthenticated]

    # def get_permissions(self):
    #     if self.request.method =='GET':
    #         return [AllowAny()]
    #     return [IsAuthenticated()]

    