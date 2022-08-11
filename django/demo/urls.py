import imp
from pipes import Template
from django import template, views
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from demoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('page1/', views.homepage),
    path('page2/', TemplateView.as_view(template_name="page2.html")),
]