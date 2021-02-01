from django.db import models

class Task(models.Model):
    
    department=models.CharField("Department", max_length=150,null=False)
    stage = models.CharField("Stage",max_length=150,   null=True)
    assigned = models.BooleanField("Assigned", default=False)
    team= models.CharField( "Team", max_length = 120, null=True)
    Date = models.DateField("Date", auto_now=False, auto_now_add=False, null=False)
    Status = models.CharField("Status",max_length=150, null=False)
    Action = models.CharField("Action", max_length=150,null=True)

    def __str__(self):
        return self.department
