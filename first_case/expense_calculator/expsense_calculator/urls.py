"""expsense_calculator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.db import router
from rest_framework import routers
from django.urls import path,include

# create a router for expenses
from rest_framework.routers import DefaultRouter

from expenses import views

# create the router
router = DefaultRouter()
# create router to view set
router.register(r'expenses', views.ExpenseViewSet)

urlpatterns = [
    #add api url to router
    path('api/', include('router.urls')),
    path('admin/', admin.site.urls),
]

# this will change the admin site title
# http://127.0.0.1:8000/admin/
admin.site.site_header = "Expense Calculator"
