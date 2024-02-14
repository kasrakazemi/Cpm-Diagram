################# Libs #################
from rest_framework import serializers
from . import models
########################################

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Projects
        fields = ['project_name','owner_user','date_created','date_modified']


class PlansSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Plans
        fields = ['plan_name','owner_user','project','date_created','date_modified']

