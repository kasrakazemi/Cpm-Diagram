################# Libs #################
from djoser.serializers import UserCreateSerializer as BaseCreateUserSerailizer
from djoser.serializers import UserSerializer as BaseUserSerializer
from .models import User,Profile
from rest_framework import serializers
########################################
   
class UserCreateSerializer(BaseCreateUserSerailizer):

    class Meta(BaseCreateUserSerailizer.Meta):
        fields = ['id', 'username', 'password', 'email', 
                  'first_name', 'last_name']



class UserSerializer(BaseUserSerializer):

    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email','first_name', 'last_name']



class ProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only = True)
    class Meta:
        model = Profile
        fields = ['id','name','birth_date','user_id','family_name','phone','language']


