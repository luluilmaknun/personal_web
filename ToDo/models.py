from django.db import models
import datetime

FREQ = {('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
        ('One time', 'One time')}

class Event(models.Model):
    title = models.CharField(max_length=100)
    dates = models.DateTimeField()
    freq =  models.CharField(max_length=50, choices=FREQ)
    file = models.FileField(upload_to="uploads/tasks/files", blank=True, null=True)
    desc = models.TextField()
