################# Libs #################
from . import models
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .serializer import NodeTypeSerializer, NodesListSerializer, EdgesListSerializer, ActivitySerializer, MilestoneSerializer, RiskSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
########################################


class NodeTypeView(ModelViewSet):
    serializer_class = NodeTypeSerializer
    queryset = models.NodeTypes.objects.all()
    permission_classes = [IsAuthenticated]


class NodesListView(ModelViewSet):
    serializer_class = NodesListSerializer
    queryset = models.NodesList.objects.all()
    permission_classes = [IsAuthenticated]


class EdgesListView(ModelViewSet):
    serializer_class = EdgesListSerializer
    queryset = models.EdgesList.objects.all()
    permission_classes = [IsAuthenticated]


class ActivityView(ModelViewSet):
    serializer_class = ActivitySerializer
    queryset = models.ActivityNode.objects.all()
    permission_classes = [IsAuthenticated]

class MilestoneView(ModelViewSet):
    serializer_class = MilestoneSerializer
    queryset = models.MilestoneNode.objects.all()
    permission_classes = [IsAuthenticated]


class RiskView(ModelViewSet):
    serializer_class = RiskSerializer
    queryset = models.RiskNode.objects.all()
    permission_classes = [IsAuthenticated]


class NoteView(ModelViewSet):
        serializer_class = NoteSerializer
        queryset = models.NoteNode.objects.all()
        permission_classes = [IsAuthenticated]

        