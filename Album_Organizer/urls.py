from django.urls import path
from .views import *

urlpatterns = [
    path('', show_albums, name="show_albums")
]
