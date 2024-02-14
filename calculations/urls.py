from django.urls import path,include
from . import views
from rest_framework.routers import SimpleRouter,DefaultRouter
# URLConf
router = DefaultRouter()
router.register('collections',views.CollectionViewset)

urlpatterns = [

    path('product_list/', views.ProductList.as_view(),name='ssss'),
    path('product_details/<int:id>/',views.Product_Details.as_view()),
    path('',include(router.urls))

]
# urlpatterns = router.urls