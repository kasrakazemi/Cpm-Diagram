################# Libs #################
from django.contrib import admin
from . import models
########################################

@admin.register(models.Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display= ['project_name','owner_user','date_created','date_modified']
    list_editable =['project_name','date_created']
    list_filter = ['owner_user']
    list_display_links = ['owner_user']


@admin.register(models.Plans)
class PlansAdmin(admin.ModelAdmin):
    list_display= ['plan_name','owner_user','project','date_created','date_modified']
    list_editable =['owner_user', 'date_created']
    list_filter = ['owner_user', 'project']
    list_display_links = ['plan_name']
