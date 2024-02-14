################# Libs #################
from rest_framework import serializers
from . import models
#######################################

class GeneralinfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.GeneralInfo
        fields = ['web_app_name','project','plan','node_ondemand_id','edge_ondemand_id']