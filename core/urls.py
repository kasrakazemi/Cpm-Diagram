################# Libs #################
from django.urls import path,include
from . import views
from rest_framework.routers import SimpleRouter,DefaultRouter
#######################################

router = DefaultRouter()
router.register('generalinfo',views.GeneralinfoView)

urlpatterns = [
    path('',include(router.urls))
]