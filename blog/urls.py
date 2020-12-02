#!/usr/bin/env python
__author__ = "Amanda Hamel"

from django.urls import path

from .views import BlogListView

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
]