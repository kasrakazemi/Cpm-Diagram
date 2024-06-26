######################################### import modules
from django.contrib import admin
from django.urls import path,include
import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
#####################################################
admin.site.site_header = 'CPM Refactor Admin Panel'
admin.site.index_title = 'Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', include('core.urls')),
    path('projects/', include('projects.urls')),
    path('accounts/', include('accounts.urls')),
    path('elements/', include('elements.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

if settings.DEBUG :
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
