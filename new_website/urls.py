from django.urls import path
from .views import *

appname = "new_website"
urlpatterns = [
    path('', index,  name="index"),
    path('resume', resume,  name="resume"),
]
