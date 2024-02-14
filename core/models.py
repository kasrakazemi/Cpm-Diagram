################# Libs #################
from django.db import models
from projects.models import Projects,Plans
########################################

class GeneralInfo(models.Model):

    web_app_name = models.CharField(max_length=150, default='Cpm_Diagram_Maker')
    project = models.OneToOneField(Projects, on_delete= models.CASCADE) 
    plan =  models.OneToOneField(Plans, on_delete= models.CASCADE)
    node_ondemand_id = models.IntegerField(default=0)
    edge_ondemand_id = models.IntegerField(default=0)


