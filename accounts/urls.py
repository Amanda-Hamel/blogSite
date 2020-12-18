#!/usr/bin/env python
__author__ = "Amanda Hamel"

from django.urls import path

from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]