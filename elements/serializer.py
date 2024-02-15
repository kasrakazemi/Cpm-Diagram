################# Libs #################
from rest_framework import serializers
from . import models
########################################

class NodeTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.NodeTypes
        fields = ['node_type','node_name']

    
class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ActivityNode
        fields = ['activity_name','activity_startdate','activity_enddate','activity_duration_type',
                  'activity_p10','activity_base','activity_p90','activity_note_low',
                  'activity_note_base','activity_note_high','plan']


class MilestoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MilestoneNode
        fields = ['milestone_name','milestone_type','milestone_date','milestone_note','plan']


class RiskSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RiskNode
        fields = ['risk_name','risk_note','plan']


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.NoteNode
        fields = ['note_value','plan']


class NodesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.NodesList
        fields = ['type','node_position','node_data','plan']


class EdgesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.EdgesList
        fields = ['edge_source','edge_target','edge_lag','plan']