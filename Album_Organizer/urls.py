from django.urls import path
from .views import *

urlpatterns = [
    path('', show_albums, name="show_albums"),
    path('album_detail/<int:pk>', album_detail, name="album_detail")
]
