################# Libs #################
from django.db import models
from django.conf import settings
########################################


class Projects(models.Model):

    project_name = models.CharField(max_length = 255, blank = False)
    owner_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.PROTECT)
    date_created = models.DateTimeField(null=False, blank=False)
    date_modified= models.DateTimeField(null= True, blank= True, auto_now= True)
    
    # change default object names in admin pannel
    def __str__(self):
        return self.project_name


class Plans(models.Model):

    plan_name = models.CharField(max_length=150, blank=False)
    owner_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.PROTECT)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='featured_plans')
    date_created = models.DateTimeField(null=False, blank=False)
    date_modified = models.DateField(null=True, blank=True, auto_now= True)
    
    # change default object names in admin pannel
    def __str__(self):
        return self.plan_name
    





