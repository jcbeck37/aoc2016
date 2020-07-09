"""aoc2016 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from aoc2016.views import day01, day02, day03, day04, day05, day06, day07, day08, day09

urlpatterns = [
    path('admin/', admin.site.urls),
    path('days/1', day01.process),
    path('days/2', day02.process),
    path('days/3', day03.process),
    path('days/4', day04.process),
    path('days/5', day05.process),
    path('days/6', day06.process),
    path('days/7', day07.process),
    path('days/8', day08.process),
    path('days/9', day09.process)
]
