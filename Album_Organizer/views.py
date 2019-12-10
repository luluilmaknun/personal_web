from django.shortcuts import render
from .models import *

def show_albums(request):
    albums = Album.objects.all()

    return render(request, 'albums.html', {'albums' : albums})

def album_detail(request, pk):
    photos = Photo.objects.all()

    return render(request, 'photos.html', {'photos' : photos, 'album_pk' : pk})
