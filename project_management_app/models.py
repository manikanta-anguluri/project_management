from django.db import models
from django.contrib.auth.models import User


status = (
    ('1', 'Open'),
    ('2', 'Completed'),
    ('3', 'Cancelled'),
)

active_status = (
    ('1', 'Yes'),
    ('2', 'No'),
)
priority_status = (
    ('1', 'Medium'),
    ('2', 'Low'),
    ('3', 'High'),
)

task_type=(
    ('1', 'internal'),
    ('2', 'external'),
)
class ProjectType(models.Model):
    type=models.CharField(max_length=100)
    
    def __str__(self):
        return(self.type)

class Project(models.Model):
    name = models.CharField(max_length=80)
    project_type = models.ForeignKey(ProjectType, on_delete=models.CASCADE)
    assign = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=status, default=1)
    is_active = models.CharField(max_length=17, choices=active_status, default=1)
    expected_start_date = models.DateField()
    expected_end_date=models.DateField()
    priority=models.CharField(max_length=15, choices=priority_status, default=1)
    description = models.TextField(blank=True)
   
    def __str__(self):
        return (self.name)


class Task(models.Model):
    task_name = models.CharField(max_length=80)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assign = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=status, default=1)
    type = models.CharField(max_length=15, choices=task_type,default=1)
    expected_start_date = models.DateField()
    expected_end_date=models.DateField()
    priority=models.CharField(max_length=15, choices=priority_status, default=1)
    description = models.TextField(blank=True)
    # user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    

    class Meta:
        ordering = ['project', 'task_name']

    def __str__(self):
        return(self.task_name)