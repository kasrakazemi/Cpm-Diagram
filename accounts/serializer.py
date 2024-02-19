################# Libs #################
from djoser.serializers import UserCreateSerializer as BaseCreateUserSerailizer
from djoser.serializers import UserSerializer as BaseUserSerializer
from .models import User,Profile,ProfileImage
from rest_framework import serializers
########################################
   
class UserCreateSerializer(BaseCreateUserSerailizer):

    class Meta(BaseCreateUserSerailizer.Meta):
        fields = ['id', 'username', 'password', 'email', 
                  'first_name', 'last_name']



class UserSerializer(BaseUserSerializer):

    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email','first_name', 'last_name']



class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileImage
        fields = ['profile', 'user_image']



class ProfileSerializer(serializers.ModelSerializer):
    #user_id = serializers.IntegerField(read_only = True)
    images = ProfileImageSerializer(many = True, read_only = True)
    class Meta:
        model = Profile
        fields = ['id','name','birth_date','user','family_name','images','phone','language']




        