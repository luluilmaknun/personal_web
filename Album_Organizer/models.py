from django.db import models

class Photo(models.Model):
	desc = models.CharField(max_length=300, null=True, blank=True)
	photo = models.ImageField(upload_to='media/Album_Organizer/')
	album_id = models.IntegerField()

class Album(models.Model):
	title = models.CharField(max_length=50, null=True, blank=True)
	desc = models.CharField(max_length=300, null=True, blank=True)
