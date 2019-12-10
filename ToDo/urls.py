from django.urls import path
from .views import *

urlpatterns = [
    path('', show_event, name="show_event"),
    path('add_event', add_event, name="add_event")
]
