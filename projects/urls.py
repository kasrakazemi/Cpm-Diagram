################# Libs #################
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProjectsView,PlansView
########################################

router = DefaultRouter()
router.register('projects',ProjectsView)
router.register('plans',PlansView)

urlpatterns = [
    path('',include(router.urls))
]
