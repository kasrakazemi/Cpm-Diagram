################# Libs #################
from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import User, Profile
from .serializer import ProfileSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
########################################

class ProfileView(CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.request.method =='GET':
            return [AllowAny()]
        return [IsAdminUser()]
    
    @action(detail=False, methods=['GET', 'PUT'])
    def me (self, request):
        (user_profile, created) = Profile.objects.get_or_create(user_id = request.user.id)

        if request.method =='GET':
            serializer = ProfileSerializer(user_profile)
            return Response(serializer.data)
        
        elif request.method =='PUT':
            serializer = ProfileSerializer(user_profile, data= request.data)
            serializer.is_valid(raise_exception= True)
            serializer.save()
            return Response(serializer.data)
         