################# Libs #################
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import NodesListView,NodeTypeView, ActivityView, MilestoneView, RiskView, NoteView, EdgesListView
########################################

router = DefaultRouter()
router.register('nodetypes',NodeTypeView)
router.register('nodeslist',NodesListView)
router.register('activity',ActivityView)
router.register('milestone',MilestoneView)
router.register('risk',RiskView)
router.register('note',NoteView)
router.register('edges',EdgesListView)

urlpatterns = [
    path('',include(router.urls))
]
