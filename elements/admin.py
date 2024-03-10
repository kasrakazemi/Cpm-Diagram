################# Libs #################
from django.contrib import admin
from . import models
from django.db.models.query import QuerySet
from rangefilter.filters import DateRangeQuickSelectListFilterBuilder
########################################

@admin.register(models.NodeTypes)
class NodeTypesAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'node_name' : ['node_type']
    }
    list_display = ['node_name', 'node_type']
    search_fields = ['node_name__istartwith']

@admin.register(models.NodesList)
class NodesAdmin(admin.ModelAdmin):
    list_display= ['type','node_position','node_data','plan']
    list_filter = ['type']
    list_per_page = 30
    list_editable = ['node_position', 'node_data']
    actions = ['clear_nodes_list']
   
    @admin.action(description= 'Select One Node Then Delete All Nodes')
    def clear_nodes_list(self, request, queryset):
         delete_all_queryset = models.NodesList.objects.all()
         delete_all_queryset.delete()

@admin.register(models.EdgesList)
class EdgesAdmin(admin.ModelAdmin):
    list_display= ['edge_source','edge_target','edge_lag','plan']
    list_filter = ['edge_source','edge_target']
    list_per_page = 30
    list_editable = ['edge_source', 'edge_target','edge_lag', 'plan']
    list_display_links = None
    
@admin.register(models.ActivityNode)
class ActivityNodeAdmin(admin.ModelAdmin):
    list_display= ['activity_name','activity_startdate','activity_enddate','activity_duration_type','plan']
    search_fields = ['activity_name__istartswith']
    list_filter = [('activity_startdate', DateRangeQuickSelectListFilterBuilder()),
                   ('activity_enddate',DateRangeQuickSelectListFilterBuilder())
                   ]

@admin.register(models.MilestoneNode)
class MilestoneNodeAdmin(admin.ModelAdmin):
    list_display= ['milestone_name','milestone_type','milestone_date','plan']
    search_fields = ['milestone_name__istartswith']
    list_filter = [('milestone_date', DateRangeQuickSelectListFilterBuilder())]
    
@admin.register(models.RiskNode)
class RiskNodeAdmin(admin.ModelAdmin):
    list_display= ['risk_name','plan']
    search_fields = ['risk_name__istartswith']

@admin.register(models.NoteNode)
class NoteNodeAdmin(admin.ModelAdmin):
    list_display= ['note_value','plan']