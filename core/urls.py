################# Libs #################
from django.urls import path,include
from django.views.generic import TemplateView
from . import views
from rest_framework.routers import SimpleRouter,DefaultRouter
#######################################

router = DefaultRouter()
router.register('generalinfo',views.GeneralinfoView)

urlpatterns = [
    path('', TemplateView.as_view(template_name= 'core/index.html')),
    path('app/',include(router.urls)),
    path('send_email/', views.SendEmail),
    path('test_get/', views.TestCaching),
]


