################# Libs #################
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProfileView, ProfileImageView
from rest_framework_nested import routers
########################################

main_router = routers.SimpleRouter()
main_router.register('profile',ProfileView)
#main_router.register('images', ProfileImageView)

image_router = routers.NestedDefaultRouter(
    main_router,
    r'profile',
    lookup='profile')

image_router.register(r'images', 
                      ProfileImageView,
                        basename='profile-images')

urlpatterns = [
    path('',include(main_router.urls)),
    path('', include(image_router.urls))
]
