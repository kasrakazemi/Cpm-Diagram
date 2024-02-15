######################################### import modules
from django.contrib import admin
from django.urls import path,include
import debug_toolbar
#####################################################
admin.site.site_header = 'CPM Refactor Admin Panel'
admin.site.index_title = 'Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('core/', include('core.urls')),
    path('projects/', include('projects.urls')),
    path('accounts/', include('accounts.urls')),
    path('elements/', include('elements.urls')),
    path('auth/', include('djoser.urls')),
     path('auth/', include('djoser.urls.jwt')),
]


