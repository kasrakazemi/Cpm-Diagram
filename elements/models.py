################# Libs #################
from django.db import models
from projects.models import Plans,Projects
########################################

# model to save different types of nodes
class NodeTypes(models.Model):
    
    Activity = 0
    Milestone = 1
    Risk = 2
    Note = 3
    Test = 4
    
    NodeChoices = [
                       (Activity,'Activity'),
                       (Milestone,'Milestone'),
                       (Risk,'Risk'),
                       (Note,'Note'),
                       (Test,'Test')
                       ]
    node_type = models.IntegerField(default=Activity,choices= NodeChoices)
    node_name = models.CharField(max_length=150)

    class Meta:
        pass

    def __str__(self):
        if self.node_type ==0 :
            return 'Activity'
        elif self.node_type == 1:
            return 'Milestone'
        elif self.node_type ==2:
            return 'Risk'
        elif self.node_type == 3:
            return 'Test'
        else:
            return 'Note'
        
# mode to save activity forms
class ActivityNode(models.Model):
    # define different types of selectable durations
    DurationTypes = [
        ('D', 'Day'),
        ('W', 'Week'),
        ('M', 'Month'),
    ]

    activity_name = models.CharField(max_length=150, default='cpm_activity', blank=True)
    activity_startdate = models.DateField(null=True, blank=True)
    activity_enddate = models.DateField(null=True, blank=True)
    activity_duration_type = models.CharField(max_length=1, choices=DurationTypes, default='D')
    activity_p10 = models.IntegerField(default=0, null=True, blank=True)
    activity_base = models.IntegerField(default=0, null=True, blank=True)
    activity_p90 = models.IntegerField(default=0, null=True, blank=True)
    activity_note_low = models.TextField(default='', null=True, blank=True)
    activity_note_base = models.TextField(default='', null=True, blank=True)
    activity_note_high = models.TextField(default='', null=True, blank=True)
    plan = models.ForeignKey(Plans, on_delete=models.CASCADE)

    class Meta:
        pass

    def __str__(self):
        return self.activity_name

# model to save milestone forms
class MilestoneNode(models.Model):
    # define different types of selectable constrains
    ConstrainTypes = [
        ('H', 'Hard'),
        ('NLT', 'No Later Than')
    ]
   
    milestone_name = models.CharField(max_length=150, default='cpm_milestone', blank=True)
    milestone_type = models.CharField(max_length=3, choices=ConstrainTypes, default='H')
    milestone_date = models.DateField(null=True, blank=True)
    milestone_note = models.TextField(default='', null=True, blank=True)
    plan = models.ForeignKey(Plans, on_delete=models.CASCADE)

    class Meta:
        pass

    def __str__(self):
        return self.milestone_name

 # model to save risk forms
class RiskNode(models.Model):
    risk_name = models.CharField(max_length=150, default='cpm_risk', blank=True)
    risk_note = models.TextField(default='', null=True, blank=True)
    plan = models.ForeignKey(Plans, on_delete=models.CASCADE)

    class Meta:
        pass

    def __str__(self):
        return self.risk_name

# model to save note values
class NoteNode(models.Model):
    note_value = models.TextField(default='', null=True, blank=True)
    plan = models.ForeignKey(Plans, on_delete=models.CASCADE)

    class Meta:
        pass
    
# model to save all nodes 
class NodesList(models.Model):
    type = models.ForeignKey(NodeTypes, default=1, blank=False, on_delete=models.CASCADE)
    node_position = models.JSONField(default=dict, blank=True)
    node_data = models.JSONField(default=dict, blank=True)
    plan = models.ForeignKey(Plans, on_delete=models.CASCADE)

    class Meta:
       pass

    def __str__(self):
        return NodeTypes.__str__(self.type)


# model to save all edges
class EdgesList(models.Model):
    edge_source = models.IntegerField(blank=False, null=False)
    edge_target = models.IntegerField(blank=False, null=False)
    # field to save lag(delay) of an edge
    edge_lag = models.PositiveIntegerField(default=0)
    # field to related plan
    plan = models.ForeignKey(Plans, on_delete=models.CASCADE)

    class Meta:
        pass
    
