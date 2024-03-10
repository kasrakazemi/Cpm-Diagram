################# Libs #################
from django.shortcuts import render
from . import models
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.http import HttpResponse      
from rest_framework import status
from .serializer import PlansSerializer, ProjectSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
########################################


class ProjectsView(ModelViewSet):
    queryset = models.Projects.objects.all()
    serializer_class = ProjectSerializer
    # permission_classes = [IsAuthenticated]

    # def get_permissions(self):
    #     if self.request.method =='GET':
    #         return [AllowAny()]
    #     return [IsAuthenticated()]

    def list(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializer = self.serializer_class(data, many= True)
        response_data = { "projects": serializer.data, "message": "all projects retrieved successfully"}
        return Response(response_data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None, *args, **kwargs):
        project = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(project)
        response_data = { "project": serializer.data,"message": "Project retrieved successfully"}
        return Response(response_data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = { "project": serializer.data,"message": "Project created successfully"}
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            response_data = { "error": serializer.errors,"message": "Project creation  failed"}
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            response_data = { "project": serializer.data,"message": "Project updated successfully"}
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            response_data = { "error": serializer.errors,"message": "Project update  failed"}
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Project deleted successfully"}, status=status.HTTP_204_NO_CONTENT)




class PlansView(ModelViewSet):
    queryset = models.Plans.objects.all()
    serializer_class = PlansSerializer
    # permission_classes = [IsAuthenticated]

    # def get_permissions(self):
    #     if self.request.method =='GET':
    #         return [AllowAny()]
    #     return [IsAuthenticated()]

    def list(self, request):
        data = self.get_queryset()
        serializer = self.serializer_class(data, many= True)
        response_data = { "plans": serializer.data, "message": "All plans retrieved successfully"}
        return Response(response_data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        plan = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(plan)
        response_data = { "Plan": serializer.data,"message": "Plan retrieved successfully"}
        return Response(response_data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = { "Plan": serializer.data,"message": "Plan created successfully"}
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            response_data = { "error": serializer.errors,"message": "Plan creation  failed"}
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            response_data = { "Plan": serializer.data,"message": "Plan updated successfully"}
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            response_data = { "error": serializer.errors,"message": "Plan update  failed"}
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Plan deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
