from django.urls import path
from .views import *

urlpatterns = [
    path('', show_cal, name="show_cal")
]
