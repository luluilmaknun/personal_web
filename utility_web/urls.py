"""utility_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.core.exceptions import ImproperlyConfigured
from django.conf.urls.static import static
from django.conf import settings
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Main.urls') )
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

for app in settings.INSTALLED_APPS:
    try:
        if app != 'Main':
            urlpatterns.append(
                path('%s/' % app if app!=os.environ.get('ROOT_URL_APP') else '', include('%s.urls' % app))
            )
    except ImportError as e:
        print('Warning! ImportError: %s' % e)
        print('URLconf from %s will be skipped' % app)
        print()
