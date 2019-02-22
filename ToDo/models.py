from django.db import models

FREQ = {('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
        ('One time', 'One time')}

class Event(models.Model):
    title = models.CharField(max_length=100)
    freq =  models.CharField(max_length=50, choices=FREQ)
    file = models.FileField(upload_to="uploads/tasks/files")
    desc = models.TextField()
