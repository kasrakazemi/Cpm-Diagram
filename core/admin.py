################# Libs #################
from django.contrib import admin
from . import models
########################################

@admin.register(models.GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    list_display= ['web_app_name','project','plan','node_ondemand_id','edge_ondemand_id']
    list_editable =['web_app_name','project']
    list_filter = ['plan']
    list_display_links = ['plan']


    