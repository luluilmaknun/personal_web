from django.shortcuts import render
from .models import *

def show_albums(request):
    albums = Album.objects.all()

    for album in albums:
        print(album.cover.photo.url)

    return render(request, 'albums.html', {'albums' : albums})
