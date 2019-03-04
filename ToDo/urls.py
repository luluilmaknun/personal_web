from django.urls import path
from .views import *

urlpatterns = [
    path('', show_event, name="show_event"),
    path('get_cal/', get_cal, name="get_cal")
]
