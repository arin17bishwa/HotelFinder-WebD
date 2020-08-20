"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from .views import (
    welcome_view,
    home_search_view,
    all_results_view,
    hotel_action_view,
)

app_name='personal'

urlpatterns = [
    path('',home_search_view,name='home'),
    path('results/',all_results_view,name='all_results'),
    path('actions/',hotel_action_view,name='actions'),
    path('welcome/', welcome_view, name='welcome'),

]
